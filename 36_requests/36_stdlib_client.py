# ============================================================
# 第 36 课 · 阶段 1（客户端）：标准库 urllib 调 HTTP
# 运行：先起 36_stdlib_server.py → 再 python 36_stdlib_client.py
# 全程不依赖外网、不装三方包。对比阶段 2 的 requests 写法。
# ============================================================
import json
import os
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE = "http://127.0.0.1:8899"
DL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "demo.stdlib.tmp.bin")


def get_json(url: str, headers: dict | None = None) -> tuple[int, dict]:
    """标准库：自己开 Request、读 bytes、decode、json.loads。"""
    req = Request(url, headers=headers or {}, method="GET")
    with urlopen(req, timeout=5) as resp:
        raw = resp.read().decode("utf-8")
        return resp.status, json.loads(raw)


def post_json(url: str, payload: dict) -> tuple[int, dict]:
    """标准库：自己 dumps、设 Content-Type、再读响应。"""
    body = json.dumps(payload).encode("utf-8")
    req = Request(
        url, data=body, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    with urlopen(req, timeout=5) as resp:
        raw = resp.read().decode("utf-8")
        return resp.status, json.loads(raw)


# 预检
try:
    get_json(f"{BASE}/hello")
except (URLError, TimeoutError):
    print("本地服务没跑：另开终端执行 python 36_requests/36_stdlib_server.py")
    raise SystemExit(0)

# 1) GET JSON
status, data = get_json(f"{BASE}/get")
print("[GET] /get           ->", status, "url =", data["url"])

# 2) 查询参数：标准库要自己 urlencode 拼到 URL
qs = urlencode({"q": "python", "page": 1})
status, data = get_json(f"{BASE}/get?{qs}")
print("[GET] /get?…        ->", f"{BASE}/get?{qs}", "args =", data["args"])

# 3) 自定义头
status, data = get_json(f"{BASE}/headers",
                        headers={"X-Study-Hub": "from-zero-36-stdlib"})
print("[GET] /headers       -> X-Study-Hub =",
      data["headers"].get("X-Study-Hub"))

# 4) POST JSON
status, data = post_json(f"{BASE}/post", {"name": "小明", "score": 95})
print("[POST] /post         ->", status, "回显 =", data["received"])

# 5) 非 2xx：标准库用 HTTPError，状态码在异常上
try:
    get_json(f"{BASE}/status/404")
except HTTPError as e:
    print("[GET] /status/404    -> code =", e.code, "; HTTPError 抛",
          type(e).__name__)

# 6) 下载：标准库读完再写盘（小文件够用；大文件要自己分块）
req = Request(f"{BASE}/download", method="GET")
with urlopen(req, timeout=5) as resp:
    with open(DL_PATH, "wb") as f:
        f.write(resp.read())
print(f"[GET] /download      -> 已写盘 {os.path.basename(DL_PATH)}"
      f"（{os.path.getsize(DL_PATH)} 字节），首行：")
with open(DL_PATH, "r", encoding="utf-8") as f:
    print("       ", f.readline().strip())

print("\n→ 阶段 1 结束。对照阶段 2：36_flask_server.py + 36_requests.py")
