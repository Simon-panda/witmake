# 第13组：CI/CD 与部署

## 121. GitHub Actions

**前世今生：** GitHub Actions 由 GitHub 于 2018 年 10 月宣布，2019 年 11 月正式 GA。在 Actions 之前，GitHub 的 CI/CD 主要靠第三方集成（Travis CI、CircleCI）。Actions 的创新在于将 CI/CD 完全嵌入仓库——`.github/workflows/` 目录中的 YAML 文件自动触发。事件驱动模型非常灵活：push、PR、issue comment、schedule、webhook 都能触发。2020 年后 Actions 迅速吃掉 Travis CI 的市场份额，成为开源项目 CI/CD 的首选。Actions Marketplace 有 1.5 万+ 预制 Action，覆盖几乎所有语言和云平台。Actions 的免费额度对公开仓库无限，私有仓库每月 2000 分钟，极大降低了小团队 CI/CD 门槛。

**使用方法与案例：**

**案例1：Python 项目 CI（测试 + lint）**
```yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v3
        with:
          python-version: ${{ matrix.python-version }}
      - run: uv pip install -r requirements-dev.txt
      - run: pytest --cov=. --cov-report=xml
      - uses: codecov/codecov-action@v4
        if: success()
```

**案例2：自动构建 Docker 镜像并推送**
```yaml
name: Build and Push
on:
  push:
    tags: ["v*"]
jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      - uses: docker/metadata-action@v5
        id: meta
        with:
          images: ghcr.io/${{ github.repository }}
          tags: type=semver,pattern={{version}}
      - uses: docker/build-push-action@v5
        with:
          push: true
          tags: ${{ steps.meta.outputs.tags }}
```

**案例3：定时任务（替代 cron）**
```yaml
name: Daily OEE Report
on:
  schedule:
    - cron: "0 6 * * *"   # 每天 6:00 UTC
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - run: |
          python generate_report.py
          curl -X POST ${{ secrets.FEISHU_WEBHOOK }} \
            -H "Content-Type: application/json" \
            -d @report.json
```

**进阶技巧：**
- `needs` 定义 job 依赖；`if: failure()` 只在失败时运行（如发告警）
- `concurrency` 防止同一分支并发运行
- OIDC 连接云平台无需存密钥：`permissions: id-token: write`

---

## 122. GitLab CI

**前世今生：** GitLab CI 于 2012 年作为 GitLab 的内置功能推出，是第一个"仓库内置 CI"产品。GitLab CI 的核心理念是"一个 `.gitlab-ci.yml` 搞定一切"——构建、测试、部署、安全扫描、发布都在同一个配置文件中。GitLab 提供免费的自托管 Runner，也提供 SaaS Runner。GitLab 的 Auto DevOps 可以零配置为任何项目生成 CI/CD 管道。2018 年后 GitLab 收购 Gemnasium（安全扫描）并整合到 CI 中，使 GitLab 成为最全面的内置 DevOps 平台。

**使用方法与案例：**

**案例：完整的 MES API 管道**
```yaml
# .gitlab-ci.yml
stages:
  - build
  - test
  - security
  - deploy

variables:
  DOCKER_IMAGE: $CI_REGISTRY_IMAGE:$CI_COMMIT_SHORT_SHA

build:
  stage: build
  script:
    - docker build -t $DOCKER_IMAGE .
    - docker push $DOCKER_IMAGE

test:
  stage: test
  script:
    - docker run --rm $DOCKER_IMAGE pytest
  coverage: '/TOTAL.*\s+(\d+\.\d+)%/'

security:
  stage: security
  script:
    - docker run --rm aquasec/trivy image $DOCKER_IMAGE

deploy:
  stage: deploy
  only: [main]
  script:
    - kubectl set image deployment/mes-api mes-api=$DOCKER_IMAGE
```

**进阶技巧：**
- `needs: ["job-name"]` 让 job 不等整个 stage 完成就启动
- `rules:` 替代 `only/except`，支持 if 条件
- `extends:` 复用 job 模板，减少重复代码

---

## 123. Argo CD

**前世今生：** Argo CD 由 Intuit（TurboTax、Mint 母公司）于 2018 年创建并开源，2020 年捐献给 CNCF。Argo CD 是 GitOps 的事实标准实现——Git 仓库是唯一的真实来源，Argo CD 持续将 Git 中的 K8s 清单同步到集群，自动检测和修正漂移（drift）。与传统的 push 式 CD（Jenkins 执行 `kubectl apply`）不同，Argo CD 是 pull 式——它自己跑在 K8s 里，盯着你的 Git 仓库，发现变化自动同步。2024 年 Argo CD 从 CNCF 毕业，被 Adobe、NVIDIA、Tesla 等数千家公司使用。

**使用方法与案例：**

安装：
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

**案例1：部署 MES 应用到 K8s**
```yaml
# argocd/application.yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: mes-api
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/myorg/mes-k8s-manifests
    targetRevision: main
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: mes-prod
  syncPolicy:
    automated:
      prune: true          # 删除 Git 中已移除的资源
      selfHeal: true       # 自动修复手动修改（修正漂移）
    syncOptions:
      - CreateNamespace=true
```

**案例2：多环境管理（App of Apps 模式）**
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: apps
spec:
  source:
    path: apps/
    directory:
      recurse: true
```
一个根 Application 管理所有子 Application，pull 仓库的 `apps/` 目录自动发现所有环境。

**进阶技巧：**
- Argo CD Image Updater 自动更新镜像版本（无需改 Git）
- `argocd app diff mes-api` 预览差异
- RBAC 精细控制谁能 sync 哪个 App
- Notifications 集成飞书/Slack

---

## 124. Flux CD

**前世今生：** Flux 由 Weaveworks（Alexis Richardson，K8s 社区领袖）于 2016 年创建，是 GitOps 术语的"发明者"。Flux 与 Argo CD 理念相似但设计不同：Flux 用 K8s 原生控制器模型，每个组件都是一个 controller。Flux v2（2020 年）重构为模块化架构：source controller（拉取 Git/Helm）、kustomize controller（应用 K8s 清单）、helm controller（管理 Helm release）、notification controller（告警）。2024 年 Weaveworks 破产后，Flux 由 CNCF 继续维护。

**使用方法与案例：**

安装：
```bash
flux bootstrap github \
  --owner=myorg --repository=mes-flux \
  --path=clusters/production
```

**案例：Helm + Kustomize 混合部署**
```yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: mes-api
spec:
  interval: 5m
  sourceRef:
    kind: GitRepository
    name: mes-manifests
  path: ./apps/mes-api/overlays/production
```

**进阶技巧：**
- Image Automation Controller 自动更新镜像 tag
- `flux suspend/resume` 临时控制同步
- Webhook Receiver 支持 GitHub/GitLab 即时触发（不必等 interval）

---

## 125. Jenkins

**前世今生：** Jenkins 的前身是 Sun Microsystems 的 Kohsuke Kawaguchi 于 2004 年创建的 Hudson。Kawaguchi 在 Sun 时需要一个自动构建工具，他用 Java 写了 Hudson。2011 年 Oracle 收购 Sun 后与社区发生商标分歧，社区 fork 为 Jenkins。Jenkins 通过 1800+ 插件生态统治了 CI/CD 领域十年（2010-2020）。Jenkinsfile（Pipeline as Code）让管道逻辑从 UI 配置变为代码管理。虽然现在被 GitHub Actions 等云原生方案蚕食，但在企业私有部署场景，Jenkins 仍是最灵活的选择。

**使用方法与案例：**

```groovy
// Jenkinsfile
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t mes-api:${BUILD_NUMBER} .'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest --junitxml=results.xml'
            }
            post {
                always { junit 'results.xml' }
            }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps {
                input message: 'Deploy to production?', ok: 'Yes'
                sh 'kubectl set image deployment/mes-api mes-api=mes-api:${BUILD_NUMBER}'
            }
        }
    }
}
```

**进阶技巧：**
- Shared Library 复用 Pipeline 代码
- Blue Ocean 插件提供现代 UI
- `parallel` 并行执行独立 stage

---

## 126. Drone CI ### 127. Dagger

**前世今生：** Drone 由 Brad Rydzewski 于 2014 年创建，是最早的容器原生 CI 平台——每个 pipeline step 都跑在独立的 Docker 容器中。2019 年被 Harness 收购。Drone 的配置极简，`.drone.yml` 比 Jenkinsfile 简洁得多。但 Harness 收购后转向付费，社区分支 Woodpecker CI 继承了其理念。

Dagger 由 Solomon Hykes（Docker 联合创始人）于 2022 年创建。Hykes 认为目前的 CI/CD 过于依赖 YAML 和平台特有语法，Dagger 用通用编程语言（Go/Python/Node.js）定义管道，在任何 CI 上运行。

**案例：Dagger + Go 定义 CI**
```go
func (m *Mes) Test(ctx context.Context) error {
    return dag.Container().From("python:3.11").
        WithDirectory("/app", m.Source).
        WithWorkdir("/app").
        WithExec([]string{"pytest", "--cov"}).
        Sync(ctx)
}
```
```bash
dagger call test
# 在本地 Docker 中运行，与线上 CI 完全一致
```

---

## 128. Woodpecker CI ### 129. Renovate ### 130. Kaniko

**Woodpecker CI** 是 Drone CI 的开源分支，继承了其简洁性和容器原生设计。适合自托管且不满 Drone 许可证变更的团队。

**Renovate** 由 WhiteSource（现 Mend）于 2017 年创建，是自动依赖更新机器人。它比你手动检查依赖升级更智能——自动创建 PR 更新 `package.json`、`requirements.txt`、Dockerfile FROM 等，支持分组、自动合并、定时调度。

```json
// renovate.json
{
  "extends": ["config:recommended"],
  "schedule": ["before 6am on Monday"],
  "automerge": true,
  "automergeType": "pr"
}
```

**Kaniko** 由 Google 于 2018 年创建。Docker 构建需要 root 权限和 Docker daemon，在 K8s 中不安全。Kaniko 在用户空间（userspace）构建容器镜像，无需 Docker daemon、无需特权模式。它是 GitLab CI 和 Tekton 中容器构建的默认工具。

```yaml
# 在 K8s 中构建镜像
apiVersion: v1
kind: Pod
spec:
  containers:
    - name: kaniko
      image: gcr.io/kaniko-project/executor:latest
      args:
        - "--context=git://github.com/myorg/mes-api"
        - "--destination=ghcr.io/myorg/mes-api:v1.0"
```

---

*第13组完成*
