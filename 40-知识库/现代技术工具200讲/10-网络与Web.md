# 第10组：网络与 Web

## 91. curl

**前世今生：** curl 由瑞典程序员 Daniel Stenberg 于 1997 年创建，最初叫 "httpget"，只是一个从命令行下载货币汇率的小工具。Stenberg 当时在 IBM 工作，需要一个能自动抓取汇率的脚本工具。1998 年改名为 "curl"（"see URL" 的谐音），并逐步增加了 FTP、SMTP、LDAP 等协议支持。curl 的独特架构在于其核心库 libcurl——一个高度可移植、线程安全的 URL 传输库，被 MySQL、PHP、Git、Docker、K8s 等数万个项目内嵌使用。据估算，全球超过 200 亿台设备上运行着 libcurl。2020 年 curl 获得瑞典 Polhem 奖（工程界的诺贝尔）。Stenberg 至今仍是唯一维护者，是开源界最著名的"独行侠"之一。

**使用方法与案例：**

安装：几乎所有系统预装。Windows 10 build 17063+ 自带 curl.exe。

**案例1：REST API 调试——GET 请求**
```bash
# 基础 GET
curl https://api.github.com/users/torvalds

# 带认证头
curl -H "Authorization: Bearer $TOKEN" \
     https://api.example.com/v1/data

# 查看完整请求/响应头（调试必备）
curl -v https://api.example.com/health
```

**案例2：POST JSON 数据**
```bash
curl -X POST https://api.example.com/items \
  -H "Content-Type: application/json" \
  -d '{"name":"test","value":42}' \
  -w "\nHTTP Status: %{http_code}\nTime: %{time_total}s\n"
```
`-w` 输出自定义格式：状态码、总耗时、DNS 解析时间等。

**案例3：文件上传/下载与断点续传**
```bash
# 断点续传下载
curl -C - -O https://releases.example.com/bigfile.tar.gz

# 上传文件（multipart）
curl -F "file=@report.pdf" -F "description=生产日报" \
     https://api.example.com/upload

# 下载并限速（防止占满带宽）
curl --limit-rate 1M -O https://example.com/large.iso
```

**进阶技巧：**
- `.curlrc` 配置文件：`-w "\n%{http_code}"` 永久加到每次请求
- `--resolve example.com:443:1.2.3.4` 绕过 DNS，直接指定 IP（测试新服务器）
- `--connect-to` 重定向连接到不同主机（比 /etc/hosts 灵活）
- `curl -s https://httpstat.us/500` 测试各种 HTTP 状态码的响应

---

## 92. wget

**前世今生：** wget 由 Hrvoje Nikšić 于 1996 年创建，名字取自 "World Wide Web" + "get"。wget 的设计哲学与 curl 完全不同：curl 是"交互式数据传输"，wget 是"非交互式批量下载"。wget 原生支持递归下载整个网站、自动重试、断点续传、镜像站点。它没有 libcurl 那样的库形态，就是一个纯粹的命令行工具。虽然 curl 功能更广（支持更多协议），但 wget 在批量下载和网站镜像场景中仍然是首选。GNU 项目于 1997 年接管了 wget 的维护。

**使用方法与案例：**

安装：
```bash
apt install wget        # Linux
brew install wget       # macOS
# Windows: 下载 wget.exe 或用 choco install wget
```

**案例1：递归下载整个文档站**
```bash
wget --recursive --level=3 --no-parent \
     --convert-links --page-requisites \
     https://docs.example.com/v2/
```
`--convert-links` 把下载后的 HTML 里链接转为本地相对路径，离线可浏览。

**案例2：批量下载 URL 列表**
```bash
# urls.txt 内容：
# https://example.com/file1.csv
# https://example.com/file2.csv
wget -i urls.txt -P ./downloads/
```

**案例3：定时抓取 + 条件下载**
```bash
# 只在文件更新时才下载（基于时间戳）
wget --timestamping https://example.com/daily_report.pdf

# 后台下载 + 日志
wget -b -o download.log https://example.com/10GB_file.iso
# -b: 后台运行，tail -f download.log 看进度
```

**进阶技巧：**
- `--mirror` = `-r -N -l inf --no-remove-listing`，一键镜像站点
- `--user-agent "Mozilla/5.0"` 伪装浏览器，某些服务器限制非浏览器 UA
- `--wait=1 --random-wait` 降低请求频率，避免被 ban
- `--spider` 不下载内容，只检查链接有效性（死链检测）

---

## 93. httpie

**前世今生：** httpie（发音 "aitch-tee-tee-pie"）由爱沙尼亚开发者 Jakub Roztočil 于 2012 年创建。Roztočil 对 curl 繁琐的 `-H "Content-Type: application/json" -d '{...}'` 语法感到沮丧，决定做一个"对人有好"的 HTTP 客户端。httpie 的核心创新是用简单的键值对语法替代 JSON 原始字符串，自动着色输出、自动识别格式。httpie 很快在 Python 社区流行起来，截至 2024 年 GitHub 已超 34k stars。2023 年推出了 Rust 重写版（HTTPie 3.0），性能大幅提升。httpie 的定位是"日常交互式 API 调试"，而 curl 更偏向脚本和自动化。

**使用方法与案例：**

安装：
```bash
pip install httpie           # Python 版
apt install httpie           # Debian/Ubuntu
brew install httpie          # macOS
cargo install httpie-cli     # Rust 版本
```

**案例1：GET 请求——自动格式化**
```bash
http GET https://api.github.com/users/torvalds
# 自动 JSON 高亮 + 响应头表格
# 等价于: curl ... | python -m json.tool（但更优雅）
```

**案例2：POST JSON——键值对语法**
```bash
http POST https://api.example.com/items \
     name="生产报表" \
     date=2026-07-05 \
     values:='[85, 92, 78]' \
     metadata:='{"owner":"simon"}'
# := 表示原始 JSON（非字符串），= 表示字符串
```

**案例3：会话保持 + 认证**
```bash
# 创建会话（自动保存 Cookie）
http --session=./session.json POST https://api.example.com/login \
     username=admin password=secret

# 后续请求自动带 Cookie
http --session=./session.json GET https://api.example.com/dashboard
```

**进阶技巧：**
- `http --offline :3000/api/users` 打印请求但不发送（类似 dry-run）
- `http --download URL` 下载文件并显示进度条
- `http --form POST ...` 发送 `multipart/form-data`（文件上传）
- 管道：`cat body.json | http POST api.example.com/items`

---

## 94. mitmproxy

**前世今生：** mitmproxy 由德国开发者 Aldo Cortesi 于 2010 年创建，名字来自 "Man In The Middle Proxy"。Cortesi 在做 Web 安全研究时需要拦截和分析 HTTPS 流量，但当时没有好的开源工具（Fiddler 只支持 Windows）。mitmproxy 的核心机制是作为中间人代理，动态生成 TLS 证书来解密 HTTPS 流量。它支持三种界面：mitmproxy（TUI）、mitmweb（浏览器 Web UI）、mitmdump（命令行非交互）。mitmproxy 是 API 调试、安全测试、隐私审计的标配工具，被 Dropbox、Spotify 等公司用于内部安全审计。

**使用方法与案例：**

安装：
```bash
pip install mitmproxy
# 或 brew install mitmproxy
```

**案例1：拦截并查看手机 App 的网络请求**
```bash
# 1. 启动代理
mitmweb --listen-port 8080
# 2. 手机设置代理: <电脑IP>:8080
# 3. 手机浏览器访问 mitm.it 安装 CA 证书
# 4. 浏览器打开 http://localhost:8081 查看所有请求
```
这个流程对调试微信小程序、移动端 API 极其有用——能看到小程序向服务器发了什么请求、返回了什么数据。

**案例2：用 Python 脚本修改流量**
```python
# modify_response.py
from mitmproxy import http

def response(flow: http.HTTPFlow):
    if "api.example.com/data" in flow.request.pretty_url:
        # 修改响应体——注入测试数据
        import json
        data = json.loads(flow.response.text)
        data['test_mode'] = True
        flow.response.text = json.dumps(data)

def request(flow: http.HTTPFlow):
    # 添加自定义头
    flow.request.headers["X-Debug"] = "true"
```
```bash
mitmproxy -s modify_response.py
```

**案例3：录制 API 调用序列用于回放**
```bash
mitmdump -w api_traffic.flow    # 录制
mitmdump -n -r api_traffic.flow  # 回放（自动重发所有请求）
```

**进阶技巧：**
- `mitmproxy --mode upstream:http://corp-proxy:8080` 链式代理
- `--ignore-hosts` 排除不需要拦截的域名
- `mitmproxy --mode transparent` 透明代理模式（网关处无需配置客户端）
- mitmproxy 的 map remote/map local 功能就像 Charles Proxy 的免费替代

---

## 95. tailscale

**前世今生：** tailscale 由 Avery Pennarun（apenwarr）于 2019 年创立。Pennarun 之前参与过 Google Fiber 项目，对网络 NAT 穿透有深刻理解。tailscale 基于 WireGuard 协议，但解决了 WireGuard 的两大痛点：密钥分发和 NAT 穿透。tailscale 的创新在于使用开源的 DERP（Detoured Encrypted Routing Protocol）中继服务器处理对称 NAT 场景，用 coordination server 自动管理密钥交换。用户只需 `tailscale up`，不必理解任何网络概念。2022 年 tailscale 开源了全部客户端代码。截至 2024 年拥有超过 1 万付费企业客户，包括 Instacart、Canva、Vercel。

**使用方法与案例：**

安装：
```bash
curl -fsSL https://tailscale.com/install.sh | sh   # Linux
brew install --cask tailscale                       # macOS
# Windows: 下载 .msi 安装包
```

**案例1：组网——任何地点访问办公室服务器**
```bash
# 在办公室服务器上
tailscale up --advertise-routes=192.168.1.0/24

# 在外地笔记本上
tailscale up
# 现在可以直接 ping 到办公室服务器:
ping 100.x.x.x  # Tailscale 分配的 IP
ssh 100.x.x.x   # 直接 SSH 进去
```
不需要公网 IP、不需要端口映射、不需要配置防火墙。

**案例2：车间设备远程接入**
```bash
# 在车间网关（如树莓派）上
tailscale up --advertise-routes=10.0.0.0/24
# 在 Tailscale Admin 控制台批准子网路由
# 现在可以在家访问所有车间PLC/摄像头/传感器 IP
```
比传统的 VPN + 端口映射方案安全且简单得多。

**案例3：临时共享服务**
```bash
# 分享本地服务给同事（无需部署到公网）
tailscale serve 3000   # 同事通过 tailscale IP 访问你的本地 3000 端口
tailscale funnel 3000  # 甚至通过公网 URL 分享（Funnel 功能）
```

**进阶技巧：**
- `tailscale exit-node` 将某个节点设为出口（所有流量经它出去）
- `tailscale lock` 签名节点防止未授权设备加入
- MagicDNS：`ping hermes-desktop` 直接用主机名而非 IP
- ACL 精细控制：哪些用户/设备能访问哪些服务

---

## 96. frp

**前世今生：** frp（Fast Reverse Proxy）由中国开发者 fatedier（宋佳佳）于 2015 年创建，名字来自 "fast reverse proxy"。在 ngrok 2.0 闭源收费后，国内缺少免费好用的内网穿透工具，frp 填补了这个空白。frp 用 Go 编写，设计简洁——`frps`（服务端，部署在公网 VPS）+ `frpc`（客户端，部署在内网机器）。通过配置文件映射端口，内网服务直接暴露到公网。frp 支持 TCP/UDP/HTTP/HTTPS/STCP（安全加密），性能远超 ngrok 1.x。截至 2024 年 GitHub 已超 90k stars，是中国开源生态中最成功的网络工具之一。

**使用方法与案例：**

安装：
```bash
# 从 GitHub releases 下载对应架构
wget https://github.com/fatedier/frp/releases/download/v0.58.0/frp_0.58.0_linux_amd64.tar.gz
tar xzf frp_*.tar.gz && cd frp_*
```

**案例1：暴露内网 Web 服务**
```ini
# 服务端 frps.toml（VPS 上）
bindPort = 7000
vhostHTTPPort = 8080
```
```ini
# 客户端 frpc.toml（内网机器上）
serverAddr = "x.x.x.x"    # VPS 公网 IP
serverPort = 7000

[[proxies]]
name = "mes-dashboard"
type = "http"
localPort = 3000
customDomains = ["mes.yourdomain.com"]
```
现在 `http://mes.yourdomain.com:8080` 直通内网 3000 端口的 MES 仪表盘。

**案例2：远程桌面暴露**
```ini
[[proxies]]
name = "rdp"
type = "tcp"
localIP = "192.168.1.100"
localPort = 3389
remotePort = 6000
```
VPS 的 6000 端口 → 内网 Windows 的 3389（RDP），`mstsc /v <VPS_IP>:6000` 即可远程。

**案例3：安全隧道（不暴露端口，仅点对点）**
```ini
[[proxies]]
name = "secret_shell"
type = "stcp"
secretKey = "abc123"
localPort = 22
```
访客端也用 frpc 配置相同的 `secretKey`，只有持有密钥才能连接，公网看不到端口。

**进阶技巧：**
- `dashboardAddr = "0.0.0.0"` + `dashboardPort = 7500` 开启 Web 管理面板
- `transport.tls.enable = true` 加密所有 frpc→frps 通信
- 负载均衡：同一服务配多个 `localPort`，frp 自动轮询
- `healthCheck` + `healthCheckTimeout` 自动剔除不可用的后端

---

## 97. ngrok

**前世今生：** ngrok 由 Alan Shreve 于 2014 年创建。Shreve 当时在 Twilio 做开发者体验，他发现让开发者在本地调试 Webhook 回调极其痛苦——要么部署到公网，要么繁琐地配路由器端口转发。ngrok 把这个过程简化为一行命令。2015 年 ngrok 2.0 商业化，1.x 开源版本停止维护。ngrok 的核心功能是"即时公网 URL"——`ngrok http 3000` 就给你一个 `https://xxx.ngrok.io` 的地址。2019 年后增加了 TCP 隧道、TLS 终止、OAuth 认证、请求重放等企业功能。2022 年完成 5000 万美元 A 轮融资。ngrok 已成为开发者体验（DX）领域的标志性产品。

**使用方法与案例：**

安装（需注册 ngrok.com 免费账号）：
```bash
brew install ngrok          # macOS
choco install ngrok         # Windows
snap install ngrok          # Linux
ngrok config add-authtoken <your_token>
```

**案例1：本地 Web 服务即时公网访问**
```bash
ngrok http 3000
# 输出:
# Forwarding  https://abc123.ngrok.io -> http://localhost:3000
```
把这个 URL 发给同事或配置为 Webhook 回调地址，即时可用。免费版有带宽限制但开发够用。

**案例2：固定域名 + 自定义子域名**
```bash
# 免费版和付费版都支持
ngrok http --domain=simon-prod.ngrok-free.app 3000
# 每次启动都是同一个 URL（免费版域名后缀固定为 ngrok-free.app）
```

**案例3：检查 Webhook 流量**
启动 ngrok 后，访问 `http://127.0.0.1:4040` 打开内置的 Web Inspector，可以看到所有请求的完整内容、重放请求、过滤特定路径。

**进阶技巧：**
- `ngrok tcp 22` 创建 TCP 隧道（临时 SSH 访问）
- `ngrok.yml` 配置文件启动多个隧道
- `--oauth google` 给隧道加 OAuth 认证（防止未授权访问）
- API 编程化管理：`curl localhost:4040/api/tunnels` 获取当前状态

---

## 98. cloudflared

**前世今生：** cloudflared 是 Cloudflare 于 2018 年开源的 Tunnel 客户端，最初代号 "Argo Tunnel"。与 ngrok 不同，Cloudflare Tunnel 利用了 Cloudflare 的全球边缘网络——流量从用户 → 最近的 Cloudflare 数据中心 → 加密隧道 → 你的内网服务器。这意味着免费享受了 Cloudflare 的 DDoS 防护、CDN 缓存、全球加速。Cloudflare Tunnel 是完全免费的（无带宽限制），且客户端完全开源。2020 年 Argo Tunnel 更名为 Cloudflare Tunnel 并解除付费限制。对于需要长期稳定内网穿透的场景（比如你车间的 MES 看板），cloudflared 比 ngrok 更合适。

**使用方法与案例：**

安装：
```bash
# macOS
brew install cloudflare/cloudflare/cloudflared
# Linux
curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
chmod +x cloudflared && sudo mv cloudflared /usr/local/bin/
# Windows: 下载 .msi 安装包
```

**案例1：创建永久隧道**
```bash
# 1. 登录（浏览器完成认证）
cloudflared tunnel login
# 2. 创建隧道
cloudflared tunnel create mes-dashboard
# 3. 配置 DNS
cloudflared tunnel route dns mes-dashboard mes.yourdomain.com
# 4. 运行
cloudflared tunnel run --url http://localhost:3000 mes-dashboard
```
现在 `https://mes.yourdomain.com` 永久指向你的本地 MES，自带 HTTPS 和 Cloudflare WAF。

**案例2：配置文件持久化（作为 systemd 服务）**
```yaml
# ~/.cloudflared/config.yml
tunnel: mes-dashboard
credentials-file: /home/user/.cloudflared/xxx.json
ingress:
  - hostname: mes.yourdomain.com
    service: http://localhost:3000
  - hostname: docs.yourdomain.com
    service: http://localhost:8080
  - service: http_status:404   # 默认拒绝
```
```bash
cloudflared tunnel install  # 自动创建 systemd 服务，开机启动
```

**案例3：零信任访问（无需公网暴露）**
```bash
# 限制只有登录 Cloudflare Access 的授权用户才能访问
cloudflared tunnel run --url http://localhost:3000 mes-dashboard
# 在 Cloudflare Zero Trust 面板配置 Access Policy：只允许公司邮箱
```
完美场景：车间 MES 只允许公司员工看，不需要向公网开放。

**进阶技巧：**
- `cloudflared access ssh` 通过 Cloudflare 安全地 SSH 到内网机器
- `warp` 模式：cloudflared 作为本地 DNS 代理，拦截并加速所有 `*.yourdomain.com` 流量
- `cloudflared tunnel info` 查看活跃连接和数据传输量
- 自带 Prometheus 指标端点（`--metrics 0.0.0.0:49312`）

---

## 99. websocat

**前世今生：** websocat 由俄罗斯开发者 Vitaly "_Vi" Shukela 于 2018 年创建。WebSocket 协议虽然被广泛使用，但在命令行调试时很不方便——curl 不支持 WebSocket，wscat 需要 Node.js 环境且功能有限。websocat 的定位是 "WebSocket 世界的 netcat"——`websocat ws://server` 像 `nc 1.2.3.4 80` 一样简单自然。它用 Rust 编写，单二进制文件，支持 WebSocket 客户端/服务器、SSL、管道转发、Unix Socket。websocat 已成为 WebSocket 调试的事实标准工具。

**使用方法与案例：**

安装：
```bash
cargo install websocat
# 或从 GitHub Releases 下载预编译二进制
```

**案例1：连接 WebSocket 服务并交互**
```bash
websocat ws://echo.websocket.org
# 输入任意文字，服务器回显
hello
> hello
```
比 `wscat -c ws://...` 更轻量，无需 npm。

**案例2：WebSocket ↔ 管道桥接**
```bash
# 把 WebSocket 消息写入文件
websocat ws://mes-server:8080/events > events.log

# 把文件内容通过 WebSocket 发送
tail -f /var/log/production.log | websocat ws://collector:8080/ingest

# JSON 消息收发
echo '{"cmd":"get_status"}' | websocat ws://device.local:8888
```

**案例3：启动 WebSocket 服务器**
```bash
# 启动一个简单的 echo 服务器
websocat -s 8080
# 或者把收到的消息转发给命令
websocat -s 8080 exec:tee -a /tmp/messages.log
```

**进阶技巧：**
- `--binary` 二进制模式（而非文本模式）
- `--socks5 127.0.0.1:1080` 通过代理连接
- `websocat --ws-c-uri=wss://... --unix-listen=/tmp/ws.sock` WebSocket ↔ Unix Socket 中转
- `--header "Authorization: Bearer xxx"` 自定义头

---

## 100. nmap

**前世今生：** nmap（Network Mapper）由 Gordon Lyon（代号 Fyodor）于 1997 年在 Phrack 杂志上首次发布。Lyon 当时 19 岁，需要一个比 `ping` 更聪明的工具来扫描网络。nmap 很快成为安全研究人员和系统管理员的标配。它的核心创新在于"TCP 栈指纹识别"——通过精心构造探测包并分析响应，即使不连接也能判断目标操作系统和运行的服务。20 多年间 nmap 被好莱坞电影多次出镜（《黑客帝国》、《谍影重重》），被美国政府列入出口管制（后来解禁）。nmap 拥有自己的脚本引擎（NSE），500+ 脚本可做漏洞检测、服务枚举、暴力破解等。它至今还是网络扫描领域无可争议的标准。

**使用方法与案例：**

安装：
```bash
apt install nmap      # Linux
brew install nmap     # macOS
# Windows: 官网下载安装包（带 GUI Zenmap）
```

**案例1：扫描局域网所有设备**
```bash
nmap -sn 192.168.1.0/24
# -sn: Ping scan（不扫端口），快速找到局域网里哪些 IP 是活的
```
输出：
```
Nmap scan report for 192.168.1.1 (router)
Nmap scan report for 192.168.1.10 (mes-server)
Nmap scan report for 192.168.1.50 (printer)
```

**案例2：扫描开放端口和服务版本**
```bash
nmap -sV -p 1-1000 192.168.1.10
# -sV: 探测服务版本（比如 "nginx 1.24" 而不是只有 "http"）
```
输出：
```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.9 (Ubuntu)
80/tcp  open  http     nginx 1.24.0
5432/tcp open  postgres PostgreSQL 16
```

**案例3：网络安全审计**
```bash
# 用 NSE 脚本扫描常见漏洞
nmap --script vuln 192.168.1.10

# 检测 SMB 共享（Windows 文件共享）
nmap --script smb-enum-shares 192.168.1.0/24

# SSL/TLS 配置检查
nmap --script ssl-enum-ciphers -p 443 example.com
```

**进阶技巧：**
- `-T4` 加速扫描（T0 最慢最隐蔽，T5 最快但可能丢包）
- `-oA scan_result` 同时输出三种格式（txt/xml/grepable）
- `nmap --script http-headers` 检查 HTTP 安全头（CSP、HSTS 等）
- `ndiff` 比较两次扫描结果，找变化（新开的端口、切换的服务）

---

*第10组完成 · 下一组: 安全与加密*
