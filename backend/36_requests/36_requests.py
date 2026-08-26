# ============================================================
# 第 36 课 · 阶段 2（客户端）：三方 requests 调 HTTP
# 运行：先起 36_flask_server.py → 再 python 36_requests/36_requests.py
# 配套练习：36_requests_exercise.py（离线自检）
# ============================================================
# 与 36_stdlib_client.py 做同一组动作——对照「三方省了哪些样板」。
import os

try:
    import requests
except ImportError:
    print("【安装】先执行 pip install requests")
    raise SystemExit(1)

BASE = "http://127.0.0.1:8899"
DL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "demo.requests.tmp.bin")

try:
    requests.get(f"{BASE}/hello", timeout=2)
except requests.RequestException:
    print("本地服务没跑：另开终端执行 python 36_requests/36_flask_server.py")
    raise SystemExit(0)

# 1) GET JSON —— 一行拿 status + .json()
r = requests.get(f"{BASE}/get", timeout=5)
print("[GET] /get           ->", r.status_code, "url =", r.json()["url"])

# 2) params= 自动拼查询串（不用手写 urlencode）
r = requests.get(f"{BASE}/get", params={"q": "python", "page": 1}, timeout=5)
print("[GET] /get           ->", r.url, "args =", r.json()["args"])

# 3) headers=
r = requests.get(f"{BASE}/headers",
                 headers={"X-Study-Hub": "from-zero-36-requests"}, timeout=5)
print("[GET] /headers       -> X-Study-Hub =",
      r.json()["headers"].get("X-Study-Hub"))

# 4) json= 自动序列化 + 设 Content-Type
r = requests.post(f"{BASE}/post",
                  json={"name": "小明", "score": 95}, timeout=5)
print("[POST] /post         ->", r.status_code, "回显 =", r.json()["received"])

# 5) raise_for_status：非 2xx 统一抛 HTTPError
bad = requests.get(f"{BASE}/status/404", timeout=5)
print("[GET] /status/404    -> code =", bad.status_code, end="; ")
try:
    bad.raise_for_status()
except requests.HTTPError as e:
    print("raise_for_status 抛", type(e).__name__)

# 6) 流式下载：stream + iter_content（大文件不一次塞进内存）
with requests.get(f"{BASE}/download", stream=True, timeout=5) as r:
    r.raise_for_status()
    with open(DL_PATH, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)
print(f"[GET] /download      -> 已写盘 {os.path.basename(DL_PATH)}"
      f"（{os.path.getsize(DL_PATH)} 字节），首行：")
with open(DL_PATH, "r", encoding="utf-8") as f:
    print("       ", f.readline().strip())

print("\n→ 阶段 2 结束。对照阶段 1：同一动作，标准库要写更多样板。")
