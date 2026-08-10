#!/usr/bin/env python3
"""OpenClaw API Proxy on :18790 → openclaw gateway :18789 (with model alias fix)"""
import json,time
from urllib.request import Request,urlopen
from http.server import HTTPServer,BaseHTTPRequestHandler

GATEWAY = "http://127.0.0.1:18789"
TOKEN   = "160c64e7d9519970cb6aaef77996b619cc71413355a2fb4b"

class H(BaseHTTPRequestHandler):
    def _log(self,msg):
        print(f"[proxy] {msg}",flush=True)
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin","*")
        self.send_header("Access-Control-Allow-Methods","*")
        self.send_header("Access-Control-Allow-Headers","*")
    def do_OPTIONS(self):
        self.send_response(200);self._cors();self.end_headers()
    def do_GET(self):
        if self.path=="/v1/models":
            return self._json({"object":"list","data":[{"id":"gpt-4o"},{"id":"gpt-4"},{"id":"deepseek-chat"},{"id":"openclaw"}]})
        if self.path.startswith("/v1/"):
            return self._forward("GET")
        return self._json({"ok":True})
    def do_POST(self):
        body=self.rfile.read(int(self.headers.get("Content-Length",0))).decode()
        req=json.loads(body) if body else {}
        # Fix model name: clawdbot:main → openclaw
        orig_model=req.get("model","")
        if orig_model=="clawdbot:main":
            req["model"]="openclaw"
            self._log(f"Fixed model: clawdbot:main → openclaw")
        new_body=json.dumps(req).encode()
        # Forward to gateway
        target=f"{GATEWAY}{self.path}"
        headers={
            "Authorization":f"Bearer {TOKEN}",
            "Content-Type":"application/json",
            "Content-Length":str(len(new_body))
        }
        try:
            r=Request(target,data=new_body,headers=headers,method="POST")
            with urlopen(r,timeout=180) as resp:
                data=resp.read()
                self.send_response(resp.status)
                self._cors()
                self.send_header("Content-Type",resp.headers.get("Content-Type","application/json"))
                self.send_header("Content-Length",str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            self._log(f"Forward error: {e}")
            self._json({"error":{"message":str(e),"type":"proxy_error"}})
    def _forward(self,method):
        body=self.rfile.read(int(self.headers.get("Content-Length",0))) if "Content-Length" in self.headers else b""
        target=f"{GATEWAY}{self.path}"
        headers={"Authorization":f"Bearer {TOKEN}"}
        if body:
            headers["Content-Type"]="application/json"
            headers["Content-Length"]=str(len(body))
        try:
            r=Request(target,data=body,headers=headers,method=method)
            with urlopen(r,timeout=30) as resp:
                data=resp.read()
                self.send_response(resp.status)
                self._cors()
                self.send_header("Content-Type",resp.headers.get("Content-Type","text/plain"))
                self.send_header("Content-Length",str(len(data)))
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            self._json({"error":{"message":str(e),"type":"proxy_error"}})
    def _json(self,d):
        b=json.dumps(d,ensure_ascii=False).encode()
        self.send_response(200)
        self.send_header("Content-Type","application/json; charset=utf-8")
        self._cors()
        self.send_header("Content-Length",str(len(b)))
        self.end_headers();self.wfile.write(b)

print("[proxy] OpenClaw API Proxy on :18790 → :18789")
HTTPServer(("127.0.0.1",18790),H).serve_forever()
