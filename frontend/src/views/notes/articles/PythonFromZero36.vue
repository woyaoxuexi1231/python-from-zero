<template>
  <div class="article">
    <p>
      脚本要拉远程数据，或把自己的能力暴露成 HTTP 接口时，
      标准库（<code>urllib</code> / <code>http.server</code>）能做，但日常几乎都用三方。
      本课先用标准库看清原理，再<strong>按生态把主流三方列全</strong>：
      优势 / 劣势、相对使用率、生产是否推荐，并各给一份最小教程。
      这是 from-zero<strong>基础最后一课</strong>。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>客人 / 主人：谁发请求、谁暴露接口</li>
      <li>标准库最小写法 + <code>ThreadingHTTPServer</code> 原理（为何无线程池）</li>
      <li>客户端三方：<code>requests</code> / <code>httpx</code> / <code>aiohttp</code> / <code>urllib3</code></li>
      <li>服务端三方：<code>Flask</code> / <code>FastAPI</code> / <code>Django</code> / <code>Starlette</code> / <code>aiohttp</code> 等</li>
      <li>各库优劣、热度、生产建议；教程按<strong>客户端 / 服务端</strong>分开</li>
      <li>Flask 与 FastAPI：为何 Hello World 极像、真正差在哪</li>
    </ul>

    <h2>先分清：客人 vs 主人</h2>
<pre><code>客户端（客人）：我的脚本  ===HTTP 请求==▶  别人的服务
服务端（主人）：我的服务  ◀===HTTP 请求===  浏览器 / 别的脚本</code></pre>
    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        一次请求 ≈ 方法 + URL +（可选）查询参数 / 头 / 正文；
        一次响应 ≈ 状态码 + 头 + 正文。
        标准库和所有三方走的是<strong>同一条 HTTP</strong>；差别只在 API 好不好写、异步支不支持、适不适合上线。
      </p>
    </div>

    <!-- ========== 标准库 ========== -->
    <h2>阶段 1：标准库（对照基线）</h2>
    <h3>客户端 <code>urllib</code></h3>
<pre><code>import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

qs = urlencode({"q": "py", "page": 1})
with urlopen(f"{url}?{qs}", timeout=5) as resp:
    data = json.loads(resp.read().decode("utf-8"))

body = json.dumps({"name": "小明"}).encode("utf-8")
req = Request(url, data=body, method="POST",
              headers={"Content-Type": "application/json"})
with urlopen(req, timeout=5) as resp:
    print(json.loads(resp.read().decode("utf-8")))</code></pre>

    <h3>服务端 <code>http.server</code></h3>
<pre><code>from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"greet": "hi"}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

ThreadingHTTPServer(("127.0.0.1", 8899), Handler).serve_forever()</code></pre>
    <p>能跑，但路由 / 读 body / 拼响应头全是样板——下面三方就是来收这些样板的。</p>

    <h2><code>ThreadingHTTPServer</code>：原理与无线程池</h2>
    <p>
      = <code>HTTPServer</code>（听端口、解析 HTTP、调 Handler）
      + <code>ThreadingMixIn</code>（<strong>每个连接新建一条线程</strong>）。
      单线程版 <code>HTTPServer</code> 会让请求互相堵；线程版让主线程继续 <code>accept</code>。
    </p>
<pre><code>主线程：accept → 开 Thread(跑 Handler) → 立刻再 accept
工作线程：读请求 → do_GET/do_POST → 写响应 → 线程结束</code></pre>
    <p>
      <strong>为什么没有线程池？</strong>标准库定位是演示：来一个请求就 <code>Thread().start()</code>，干完丢掉；
      没有固定工人数、没有队列上限——突发流量可能开爆线程。
      「无线程池」≠「池不好」，只是这套不负责生产级并发。
    </p>
    <p>
      生产常见：Waitress（线程池）、Gunicorn sync（进程池）、
      uvicorn / Gunicorn+gevent（协程）。业务框架（Flask/FastAPI）管路由；
      专业 server 管并发。客户端 <code>requests</code> 里的是<strong>连接池</strong>（复用 TCP），别和服务端线程池混谈。
    </p>

    <!-- ========== 三方全景 ========== -->
    <h2>阶段 2：三方生态全景</h2>
    <p>
      下面「使用率」来自 PyPI 近月下载量的<strong>相对档位</strong>（约 2026-08，含 CI / 传递依赖，只比热度，不是精确用户数）。
      「生产推荐」指：新项目 / 线上服务是否优先选它。
    </p>

    <h3>客户端（发请求）</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>库</th>
          <th>使用率</th>
          <th>优势</th>
          <th>劣势</th>
          <th>生产推荐</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>requests</code></td>
          <td>极高（同步客户端事实标准）</td>
          <td>API 最熟、文档多、同步脚本一把梭</td>
          <td>无原生 async；维护偏保守</td>
          <td><strong>推荐</strong>（同步场景首选）</td>
        </tr>
        <tr>
          <td><code>httpx</code></td>
          <td>很高（新项目增速快）</td>
          <td>API 像 requests；同步+异步一套；HTTP/2</td>
          <td>生态比 requests 略新，老教程少</td>
          <td><strong>推荐</strong>（要 async / 现代栈首选）</td>
        </tr>
        <tr>
          <td><code>aiohttp</code>（ClientSession）</td>
          <td>高</td>
          <td>asyncio 生态成熟；客户端+服务端一体</td>
          <td>只走 async；API 与 requests 不像</td>
          <td><strong>推荐</strong>（已在 aiohttp/asyncio 栈里时）</td>
        </tr>
        <tr>
          <td><code>urllib3</code></td>
          <td>极高（多为传递依赖）</td>
          <td>连接池、重试等底层能力强；requests 就建在它上面</td>
          <td>偏底层，业务代码直接写少</td>
          <td>一般<strong>不直接写</strong>；特殊定制再碰</td>
        </tr>
      </tbody>
    </table>

    <h3>服务端（暴露接口）</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>库</th>
          <th>使用率</th>
          <th>优势</th>
          <th>劣势</th>
          <th>生产推荐</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>FastAPI</code></td>
          <td>极高（近年新 API 项目常第一）</td>
          <td>类型注解、自动 OpenAPI、异步友好、性能好</td>
          <td>要懂一点 typing / pydantic；全站页面不如 Django</td>
          <td><strong>强烈推荐</strong>（新 HTTP API）</td>
        </tr>
        <tr>
          <td><code>Flask</code></td>
          <td>很高（存量与教程海量）</td>
          <td>极简、好上手、扩展多</td>
          <td>默认同步；大型项目结构要自己定规矩</td>
          <td><strong>推荐</strong>（小服务 / 遗留 / 教学对照）</td>
        </tr>
        <tr>
          <td><code>Django</code></td>
          <td>高（完整 Web 应用）</td>
          <td>ORM、Admin、鉴权、电池齐全</td>
          <td>偏重；纯 JSON API 常显臃肿</td>
          <td><strong>推荐</strong>（要整站 / 后台 / 传统 Web）</td>
        </tr>
        <tr>
          <td><code>Starlette</code></td>
          <td>很高（常作 FastAPI 底座）</td>
          <td>轻量 ASGI、性能好</td>
          <td>比 FastAPI 少「开箱」功能</td>
          <td>要极简 ASGI 时用；一般直接 FastAPI</td>
        </tr>
        <tr>
          <td><code>aiohttp</code>（web）</td>
          <td>中高</td>
          <td>与异步客户端同库；控制细</td>
          <td>生态与「现代 API 脚手架」不如 FastAPI</td>
          <td>已在 aiohttp 栈可继续；新项目更常 FastAPI</td>
        </tr>
        <tr>
          <td><code>Tornado</code></td>
          <td>中（老牌异步）</td>
          <td>长连接 / WebSocket 历史积累</td>
          <td>新项目份额被 FastAPI 等分流</td>
          <td>维护旧系统可以；新项目慎选</td>
        </tr>
        <tr>
          <td><code>Sanic</code> / <code>Quart</code> 等</td>
          <td>相对小众</td>
          <td>各有异步 / Flask-兼容卖点</td>
          <td>招聘与资料少于四大主流</td>
          <td>一般<strong>不优先</strong>；团队已定栈除外</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout--principle">
      <span class="callout__label">入门怎么选</span>
      <p>
        客户端：同步 → <code>requests</code>；要异步 / 和 FastAPI 配套 → <code>httpx</code>。<br>
        服务端：新 API → <code>FastAPI</code>；对照标准库 / 超小服务 → <code>Flask</code>；整站后台 → <code>Django</code>。<br>
        本课配课练习用 <code>requests</code> + <code>Flask</code>（最好上手对照）；生产新 API 更常 FastAPI。
      </p>
    </div>

    <h2>Flask 和 FastAPI 为什么长得像？</h2>
    <p>
      你好眼：两者都是「造一个 <code>app</code> → <code>@app.get/post</code> 挂路由 → 函数里返回数据」。
      这是现代 Python Web 框架的<strong>共同套路</strong>，不是抄袭错觉——Hello World 本来就会像。
    </p>
    <table class="article-table">
      <thead>
        <tr>
          <th></th>
          <th>Flask</th>
          <th>FastAPI</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>表面写法</td>
          <td colspan="2">装饰器路由、函数返回 JSON——几乎同一套心智模型</td>
        </tr>
        <tr>
          <td>协议栈</td>
          <td>WSGI（偏同步）</td>
          <td>ASGI（原生异步友好）</td>
        </tr>
        <tr>
          <td>请求体校验</td>
          <td>自己 <code>get_json()</code>，对不对靠你</td>
          <td>用类型 / <code>BaseModel</code>，非法直接 422</td>
        </tr>
        <tr>
          <td>接口文档</td>
          <td>要自己接 Swagger 等</td>
          <td>自带 <code>/docs</code>（OpenAPI）</td>
        </tr>
        <tr>
          <td>返回值</td>
          <td>常显式 <code>jsonify(...)</code></td>
          <td>直接 <code>return dict</code> / Pydantic 模型</td>
        </tr>
        <tr>
          <td>生产挂载</td>
          <td>gunicorn / waitress 等</td>
          <td>uvicorn（或 gunicorn+uvicorn worker）</td>
        </tr>
        <tr>
          <td>更适合</td>
          <td>小服务、存量项目、教学对照</td>
          <td>新 HTTP API、要文档与校验开箱即用</td>
        </tr>
      </tbody>
    </table>
    <p>
      一句话：<strong>入门长得像；长大后差在异步模型、数据校验、自动文档、性能与生态方向。</strong>
      学会其中一个，另一个迁移成本很低——所以本课两个都给最小例子。
    </p>

    <!-- ========== 教程：客户端 / 服务端分开 ========== -->
    <h2>三方教程 · 客户端（发请求）</h2>

    <h3><code>requests</code>（同步 · 最常用）</h3>
<pre><code>pip install requests</code></pre>
<pre><code>import requests

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
s.get("https://httpbin.org/headers", timeout=8)</code></pre>

    <h3><code>httpx</code>（同步 + 异步）</h3>
<pre><code>pip install httpx</code></pre>
<pre><code>import httpx

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

asyncio.run(main())</code></pre>

    <h3><code>aiohttp</code> 客户端</h3>
<pre><code>pip install aiohttp</code></pre>
<pre><code>import aiohttp
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

asyncio.run(main())</code></pre>

    <h3><code>urllib3</code>（底层 · 了解即可）</h3>
<pre><code>pip install urllib3</code></pre>
<pre><code>import json
import urllib3

http = urllib3.PoolManager()
r = http.request(
    "POST",
    "https://httpbin.org/post",
    body=json.dumps({"name": "小明"}).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    timeout=urllib3.Timeout(total=8.0),
)
print(r.status, json.loads(r.data.decode("utf-8")))</code></pre>
    <p>业务优先 <code>requests</code> / <code>httpx</code>；要精细拧连接池、重试时再直接用 <code>urllib3</code>。</p>

    <h2>三方教程 · 服务端（暴露接口）</h2>

    <h3><code>Flask</code></h3>
<pre><code>pip install flask</code></pre>
<pre><code>from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/hello")
def hello():
    return jsonify(greet="hi")

@app.post("/echo")
def echo():
    return jsonify(received=request.get_json(silent=True))

# 仅本地演示；生产用 waitress / gunicorn 挂载 app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8899)</code></pre>
<pre><code># 生产示意：
# pip install waitress
# waitress-serve --host=0.0.0.0 --port=8000 app:app</code></pre>

    <h3><code>FastAPI</code></h3>
<pre><code>pip install "fastapi[standard]"</code></pre>
<pre><code>from fastapi import FastAPI
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
# 文档：http://127.0.0.1:8899/docs</code></pre>

    <h3><code>Django</code>（完整 Web；API 最小形态）</h3>
<pre><code>pip install django
django-admin startproject mysite
# 在 urls.py / views.py 里挂路由</code></pre>
<pre><code># views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def echo(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=405)
    data = json.loads(request.body.decode("utf-8") or "{}")
    return JsonResponse({"received": data})</code></pre>
    <p>正经 Django API 更常配 Django REST framework；上表「整站 / 后台」才是主场。</p>

    <h3><code>Starlette</code>（轻量 ASGI · FastAPI 底座）</h3>
<pre><code>pip install starlette uvicorn</code></pre>
<pre><code>from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

async def hello(request):
    return JSONResponse({"greet": "hi"})

app = Starlette(routes=[Route("/hello", hello)])
# uvicorn 模块名:app --port 8899</code></pre>

    <h3><code>aiohttp</code> 服务端</h3>
<pre><code>from aiohttp import web

async def hello(request):
    return web.json_response({"greet": "hi"})

app = web.Application()
app.router.add_get("/hello", hello)
web.run_app(app, host="127.0.0.1", port=8899)</code></pre>

    <h2>推荐骨架（日常同步客户端）</h2>
<pre><code>def fetch_json(url: str, **kwargs) -> dict:
    r = requests.get(url, timeout=8, **kwargs)
    r.raise_for_status()
    return r.json()</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        永远写 <code>timeout=</code>。JSON 用 <code>json=dict</code>（requests/httpx），别手拼 <code>data=</code> 字符串。
        Flask/FastAPI 的 <code>app.run</code> / 热重载开发服 ≠ 生产服。
        <code>200</code> 只表示 HTTP 成功；业务成功还看 body。token 别进仓库。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>阶段 1：起 <code>36_stdlib_server.py</code> → 跑 <code>36_stdlib_client.py</code>。</li>
      <li><code>pip install requests flask</code>。</li>
      <li>阶段 2：起 <code>36_flask_server.py</code> → 跑 <code>36_requests.py</code>。</li>
      <li>练习：<code>36_requests_exercise.py</code>（6 题离线）。</li>
      <li>选做：把上面 <code>httpx</code> / <code>FastAPI</code> 最小示例自己跑通一遍。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走：标准库看懂协议 → 客户端日常 <code>requests</code>/<code>httpx</code> →
      服务端新 API 优先 <code>FastAPI</code>，小服务可用 <code>Flask</code>，整站看 <code>Django</code>；
      <code>ThreadingHTTPServer</code> 懂原理即可，上线换专业 server。
      <strong>from-zero 基础课到此收官。</strong>
    </p>
  </div>
</template>
