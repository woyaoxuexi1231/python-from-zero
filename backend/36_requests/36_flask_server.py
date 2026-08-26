# ============================================================
# 第 36 课 · 阶段 2（服务端）：三方 Flask 暴露同一套接口
# 运行：pip install flask → python 36_requests/36_flask_server.py
#   启动后保持运行，Ctrl+C 停。配套客户端：36_requests.py
# ============================================================
# 路由与阶段 1 的 http.server 相同——对比代码量与可读性。
import os

try:
    from flask import Flask, jsonify, request, send_file
except ImportError:
    print("【安装】先执行 pip install flask")
    raise SystemExit(1)

HOST, PORT = "127.0.0.1", 8899
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "demo.txt")

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write("第 36 课 Flask 演示：这是被下载的文件。\n第二行：third-party stage。\n")

app = Flask(__name__)


@app.get("/hello")
def hello():
    return jsonify(greet="from-zero-36", kind="flask")


@app.get("/get")
def echo_get():
    # request.args 已是解析好的查询参数；url 用完整 path+query
    return jsonify(url=request.full_path.rstrip("?"), args=request.args.to_dict())


@app.get("/headers")
def echo_headers():
    return jsonify(headers=dict(request.headers))


@app.post("/post")
def echo_post():
    # get_json(silent=True)：正文不是 JSON 时返回 None，不抛错
    payload = request.get_json(silent=True)
    if payload is None:
        payload = request.get_data(as_text=True)
    return jsonify(received=payload)


@app.get("/status/<int:code>")
def status(code: int):
    return jsonify(status=code), code


@app.get("/download")
def download():
    return send_file(FILE_PATH, as_attachment=True, download_name="demo.txt")


def main():
    print(f"[阶段2·三方] Flask → http://{HOST}:{PORT}/", flush=True)
    print("保持运行……另开终端跑 36_requests.py。Ctrl+C 停止。", flush=True)
    # 教学演示：单进程即可；生产会用 gunicorn / waitress 等
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)


if __name__ == "__main__":
    main()
