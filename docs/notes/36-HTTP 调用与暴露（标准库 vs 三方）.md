# 第 36 课：HTTP 调用与暴露（标准库 vs 三方）

`Python 从零` · 更新于 2026-08-26 · 标签：Python、入门、网络

**摘要**：标准库对照 + 主流 HTTP 三方全景（优劣/热度/生产建议）与各库最小教程；ThreadingHTTPServer 原理；基础课收官。

---

脚本要拉远程数据，或把自己的能力暴露成 HTTP 接口时， 标准库（`urllib` / `http.server`）能做，但日常几乎都用三方。 本课先用标准库看清原理，再**按生态把主流三方列全**： 优势 / 劣势、相对使用率、生产是否推荐，并各给一份最小教程。 这是 from-zero**基础最后一课**。

## 这一课解决什么问题

- 客人 / 主人：谁发请求、谁暴露接口
- 标准库最小写法 + `ThreadingHTTPServer` 原理（为何无线程池）
- 客户端三方：`requests` / `httpx` / `aiohttp` / `urllib3`
- 服务端三方：`Flask` / `FastAPI` / `Django` / `Starlette` / `aiohttp` 等
- 各库优劣、热度、生产建议；教程按**客户端 / 服务端**分开
- Flask 与 FastAPI：为何 Hello World 极像、真正差在哪

## 先分清：客人 vs 主人

```text
客户端（客人）：我的脚本  ===HTTP 请求==▶  别人的服务
服务端（主人）：我的服务  ◀===HTTP 请求===  浏览器 / 别的脚本
```

> **原理**
>
> 一次请求 ≈ 方法 + URL +（可选）查询参数 / 头 / 正文； 一次响应 ≈ 状态码 + 头 + 正文。 标准库和所有三方走的是**同一条 HTTP**；差别只在 API 好不好写、异步支不支持、适不适合上线。

## 阶段 1：标准库（对照基线）

### 客户端 `urllib`

```python
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

qs = urlencode({"q": "py", "page": 1})
with urlopen(f"{url}?{qs}", timeout=5) as resp:
    data = json.loads(resp.read().decode("utf-8"))

body = json.dumps({"name": "小明"}).encode("utf-8")
req = Request(url, data=body, method="POST",
              headers={"Content-Type": "application/json"})
with urlopen(req, timeout=5) as resp:
    print(json.loads(resp.read().decode("utf-8")))
```

### 服务端 `http.server`

```python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"greet": "hi"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

ThreadingHTTPServer(("127.0.0.1", 8899), Handler).serve_forever()
```

能跑，但路由 / 读 body / 拼响应头全是样板——下面三方就是来收这些样板的。

## `ThreadingHTTPServer`：原理与无线程池

= `HTTPServer`（听端口、解析 HTTP、调 Handler） + `ThreadingMixIn`（**每个连接新建一条线程**）。 单线程版 `HTTPServer` 会让请求互相堵；线程版让主线程继续 `accept`。

```text
主线程：accept → 开 Thread(跑 Handler) → 立刻再 accept
工作线程：读请求 → do_GET/do_POST → 写响应 → 线程结束
```

**为什么没有线程池？**标准库定位是演示：来一个请求就 `Thread().start()`，干完丢掉； 没有固定工人数、没有队列上限——突发流量可能开爆线程。 「无线程池」≠「池不好」，只是这套不负责生产级并发。

生产常见：Waitress（线程池）、Gunicorn sync（进程池）、 uvicorn / Gunicorn+gevent（协程）。业务框架（Flask/FastAPI）管路由； 专业 server 管并发。客户端 `requests` 里的是**连接池**（复用 TCP），别和服务端线程池混谈。

## 阶段 2：三方生态全景

下面「使用率」来自 PyPI 近月下载量的**相对档位**（约 2026-08，含 CI / 传递依赖，只比热度，不是精确用户数）。 「生产推荐」指：新项目 / 线上服务是否优先选它。

### 客户端（发请求）

| 库 | 使用率 | 优势 | 劣势 | 生产推荐 |
| --- | --- | --- | --- | --- |
| `requests` | 极高（同步客户端事实标准） | API 最熟、文档多、同步脚本一把梭 | 无原生 async；维护偏保守 | **推荐**（同步场景首选） |
| `httpx` | 很高（新项目增速快） | API 像 requests；同步+异步一套；HTTP/2 | 生态比 requests 略新，老教程少 | **推荐**（要 async / 现代栈首选） |
| `aiohttp`（ClientSession） | 高 | asyncio 生态成熟；客户端+服务端一体 | 只走 async；API 与 requests 不像 | **推荐**（已在 aiohttp/asyncio 栈里时） |
| `urllib3` | 极高（多为传递依赖） | 连接池、重试等底层能力强；requests 就建在它上面 | 偏底层，业务代码直接写少 | 一般**不直接写**；特殊定制再碰 |

### 服务端（暴露接口）

| 库 | 使用率 | 优势 | 劣势 | 生产推荐 |
| --- | --- | --- | --- | --- |
| `FastAPI` | 极高（近年新 API 项目常第一） | 类型注解、自动 OpenAPI、异步友好、性能好 | 要懂一点 typing / pydantic；全站页面不如 Django | **强烈推荐**（新 HTTP API） |
| `Flask` | 很高（存量与教程海量） | 极简、好上手、扩展多 | 默认同步；大型项目结构要自己定规矩 | **推荐**（小服务 / 遗留 / 教学对照） |
| `Django` | 高（完整 Web 应用） | ORM、Admin、鉴权、电池齐全 | 偏重；纯 JSON API 常显臃肿 | **推荐**（要整站 / 后台 / 传统 Web） |
| `Starlette` | 很高（常作 FastAPI 底座） | 轻量 ASGI、性能好 | 比 FastAPI 少「开箱」功能 | 要极简 ASGI 时用；一般直接 FastAPI |
| `aiohttp`（web） | 中高 | 与异步客户端同库；控制细 | 生态与「现代 API 脚手架」不如 FastAPI | 已在 aiohttp 栈可继续；新项目更常 FastAPI |
| `Tornado` | 中（老牌异步） | 长连接 / WebSocket 历史积累 | 新项目份额被 FastAPI 等分流 | 维护旧系统可以；新项目慎选 |
| `Sanic` / `Quart` 等 | 相对小众 | 各有异步 / Flask-兼容卖点 | 招聘与资料少于四大主流 | 一般**不优先**；团队已定栈除外 |

> **入门怎么选**
>
> 客户端：同步 → `requests`；要异步 / 和 FastAPI 配套 → `httpx`。 服务端：新 API → `FastAPI`；对照标准库 / 超小服务 → `Flask`；整站后台 → `Django`。 本课配课练习用 `requests` + `Flask`（最好上手对照）；生产新 API 更常 FastAPI。

## Flask 和 FastAPI 为什么长得像？

你好眼：两者都是「造一个 `app` → `@app.get/post` 挂路由 → 函数里返回数据」。 这是现代 Python Web 框架的**共同套路**，不是抄袭错觉——Hello World 本来就会像。

|   | Flask | FastAPI |
| --- | --- | --- |
| 表面写法 | 装饰器路由、函数返回 JSON——几乎同一套心智模型 |   |
| 协议栈 | WSGI（偏同步） | ASGI（原生异步友好） |
| 请求体校验 | 自己 `get_json()`，对不对靠你 | 用类型 / `BaseModel`，非法直接 422 |
| 接口文档 | 要自己接 Swagger 等 | 自带 `/docs`（OpenAPI） |
| 返回值 | 常显式 `jsonify(...)` | 直接 `return dict` / Pydantic 模型 |
| 生产挂载 | gunicorn / waitress 等 | uvicorn（或 gunicorn+uvicorn worker） |
| 更适合 | 小服务、存量项目、教学对照 | 新 HTTP API、要文档与校验开箱即用 |

一句话：**入门长得像；长大后差在异步模型、数据校验、自动文档、性能与生态方向。** 学会其中一个，另一个迁移成本很低——所以本课两个都给最小例子。

## 三方教程 · 客户端（发请求）

### `requests`（同步 · 最常用）

```bash
pip install requests
```

```python
import requests

r = requests.get(
    "https://httpbin.org/get",
    params={"q": "py"},
    headers={"X-Demo": "1"},
    timeout=8,
)
r.raise_for_status()
print(r.status_code, r.json())

r = requests.post(
    "https://httpbin.org/post",
    json={"name": "小明"},
    timeout=8,
)
print(r.json()["json"])

# 会话：复用连接 + 默认头
s = requests.Session()
s.headers["Authorization"] = "Bearer xxx"
s.get("https://httpbin.org/headers", timeout=8)
```

### `httpx`（同步 + 异步）

```bash
pip install httpx
```

```python
import httpx

# 同步：几乎是 requests 手感
r = httpx.get("https://httpbin.org/get", params={"q": "py"}, timeout=8.0)
r.raise_for_status()
print(r.json())

# 异步
import asyncio

async def main():
    async with httpx.AsyncClient(timeout=8.0) as client:
        r = await client.get("https://httpbin.org/get")
        print(r.status_code, r.json())

asyncio.run(main())
```

### `aiohttp` 客户端

```bash
pip install aiohttp
```

```python
import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://httpbin.org/get",
            params={"q": "py"},
            timeout=aiohttp.ClientTimeout(total=8),
        ) as resp:
            resp.raise_for_status()
            print(await resp.json())

asyncio.run(main())
```

### `urllib3`（底层 · 了解即可）

```bash
pip install urllib3
```

```python
import json
import urllib3

http = urllib3.PoolManager()
r = http.request(
    "POST",
    "https://httpbin.org/post",
    body=json.dumps({"name": "小明"}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    timeout=urllib3.Timeout(total=8.0),
)
print(r.status, json.loads(r.data.decode("utf-8")))
```

业务优先 `requests` / `httpx`；要精细拧连接池、重试时再直接用 `urllib3`。

## 三方教程 · 服务端（暴露接口）

### `Flask`

```bash
pip install flask
```

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/hello")
def hello():
    return jsonify(greet="hi")

@app.post("/echo")
def echo():
    return jsonify(received=request.get_json(silent=True))

# 仅本地演示；生产用 waitress / gunicorn 挂载 app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8899)
```

```text
# 生产示意：
# pip install waitress
# waitress-serve --host=0.0.0.0 --port=8000 app:app
```

### `FastAPI`

```bash
pip install "fastapi[standard]"
```

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    score: int = 0

@app.get("/hello")
def hello():
    return {"greet": "hi"}   # 不用 jsonify

@app.post("/echo")
def echo(item: Item):        # 自动校验；不合法 → 422
    return {"received": item}

# 启动：uvicorn 模块名:app --reload --port 8899
# 文档：http://127.0.0.1:8899/docs
```

### `Django`（完整 Web；API 最小形态）

```bash
pip install django
django-admin startproject mysite
# 在 urls.py / views.py 里挂路由
```

```python
# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def echo(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    data = json.loads(request.body.decode("utf-8") or "{}")
    return JsonResponse({"received": data})
```

正经 Django API 更常配 Django REST framework；上表「整站 / 后台」才是主场。

### `Starlette`（轻量 ASGI · FastAPI 底座）

```bash
pip install starlette uvicorn
```

```python
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def hello(request):
    return JSONResponse({"greet": "hi"})

app = Starlette(routes=[Route("/hello", hello)])
# uvicorn 模块名:app --port 8899
```

### `aiohttp` 服务端

```python
from aiohttp import web

async def hello(request):
    return web.json_response({"greet": "hi"})

app = web.Application()
app.router.add_get("/hello", hello)
web.run_app(app, host="127.0.0.1", port=8899)
```

## 推荐骨架（日常同步客户端）

```python
def fetch_json(url: str, **kwargs) -> dict:
    r = requests.get(url, timeout=8, **kwargs)
    r.raise_for_status()
    return r.json()
```

> **踩坑**
>
> 永远写 `timeout=`。JSON 用 `json=dict`（requests/httpx），别手拼 `data=` 字符串。 Flask/FastAPI 的 `app.run` / 热重载开发服 ≠ 生产服。 `200` 只表示 HTTP 成功；业务成功还看 body。token 别进仓库。

## 配课怎么练

2. 阶段 1：起 `36_stdlib_server.py` → 跑 `36_stdlib_client.py`。
4. `pip install requests flask`。
6. 阶段 2：起 `36_flask_server.py` → 跑 `36_requests.py`。
8. 练习：`36_requests_exercise.py`（6 题离线）。
10. 选做：把上面 `httpx` / `FastAPI` 最小示例自己跑通一遍。

## 收束

带走：标准库看懂协议 → 客户端日常 `requests`/`httpx` → 服务端新 API 优先 `FastAPI`，小服务可用 `Flask`，整站看 `Django`； `ThreadingHTTPServer` 懂原理即可，上线换专业 server。 **from-zero 基础课到此收官。**

---

上一课：[第 35 课：pytest 写断言](35-pytest 写断言.md)　|　下一课：[第 37 课：os 与配置读取（os.getenv / BaseSettings）](37-os 与配置读取（os.getenv - BaseSettings）.md)
