# ============================================================
# 第 36 课 · 阶段 1（服务端）：标准库 http.server 暴露接口
# 运行：python 36_requests/36_stdlib_server.py
#   启动后保持运行，Ctrl+C 停。配套客户端：36_stdlib_client.py
# ============================================================
# 同一套路由后面 Flask 也会再写一遍——对比「啰嗦 vs 人话」。
#   GET  /hello /get /headers /download /status/<码>
#   POST /post
import json
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

HOST, PORT = "127.0.0.1", 8899
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "demo.txt")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write("第 36 课 标准库演示：这是被下载的文件。\n第二行：stdlib stage。\n")


class Handler(BaseHTTPRequestHandler):
    """标准库写法：每个方法里自己解析路径、读 body、拼响应头。"""
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass  # 静默访问日志

    def _send(self, code, obj=None, body=None,
              ctype="application/json; charset=utf-8", headers=None):
        if obj is not None:
            body = json.dumps(obj, ensure_ascii=False)
        data = body.encode("utf-8") if isinstance(body, str) else body or b""
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        for k, v in (headers or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        args = {k: v[0] for k, v in parse_qs(parsed.query).items()}

        if path == "/get":
            self._send(200, {"url": self.path, "args": args})
        elif path == "/headers":
            self._send(200, {"headers": dict(self.headers.items())})
        elif path == "/hello":
            self._send(200, {"greet": "from-zero-36", "kind": "stdlib"})
        elif path == "/download":
            with open(FILE_PATH, "rb") as f:
                raw = f.read()
            self._send(
                200, body=raw, ctype="application/octet-stream",
                headers={"Content-Disposition": 'attachment; filename="demo.txt"'})
        elif path.startswith("/status/"):
            code = int(path.rsplit("/", 1)[1])
            self._send(code, {"status": code})
        else:
            self._send(404, {"error": "not found"})

    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        if urlparse(self.path).path == "/post":
            try:
                obj = json.loads(raw.decode("utf-8"))
            except Exception:
                obj = raw.decode("utf-8", errors="replace")
            self._send(200, {"received": obj})
        else:
            self._send(200, body=raw.decode("utf-8", errors="replace"),
                       ctype="application/octet-stream")


def main():
    print(f"[阶段1·标准库] http.server → http://{HOST}:{PORT}/", flush=True)
    print("保持运行……另开终端跑 36_stdlib_client.py。Ctrl+C 停止。", flush=True)
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n服务已停止。")


if __name__ == "__main__":
    main()
