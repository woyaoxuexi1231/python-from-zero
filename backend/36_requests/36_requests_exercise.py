# ============================================================
# 第 36 课（练习）：HTTP 思维 —— 围绕状态码 / URL / 字段的纯函数
# 运行：python 36_requests/36_requests_exercise.py
# 全部离线。先跑通阶段 1（stdlib）再阶段 2（requests/Flask）。
# ============================================================


# ---------- 题 1：2xx 算成功 ----------
# 写 is_success(status_code: int) -> bool：
#   200 <= status_code <= 299 → True，否则 False。
def is_success(status_code: int) -> bool:
    pass


# ---------- 题 2：拼查询 URL ----------
# 写 build_url(base: str, params: dict[str, str | int]) -> str：
#   无 params → 原样返回 base
#   有 params → base + "?" + "k=v&k=v..."（按 dict 插入顺序；值转 str）
#   例：build_url("https://api.example/items", {"q": "py", "page": 2})
#       → "https://api.example/items?q=py&page=2"
#   简化：不必做 URL 编码（练习不测中文/空格）。
#   （标准库 urllib.parse.urlencode / requests 的 params= 就是在干这事）
def build_url(base: str, params: dict[str, str | int]) -> str:
    pass


# ---------- 题 3：Bearer 头 ----------
# 写 auth_headers(token: str) -> dict[str, str]：
#   返回 {"Authorization": f"Bearer {token}"}
def auth_headers(token: str) -> dict[str, str]:
    pass


# ---------- 题 4：从 JSON 抽字段 ----------
# 写 get_message(payload: dict) -> str：
#   若 "message" 在 payload 且值为 str → 返回该字符串
#   否则 → ""
def get_message(payload: dict) -> str:
    pass


# ---------- 题 5：客户端 / 服务端错误 ----------
# 写 error_kind(status_code: int) -> str：
#   400~499 → "client"
#   500~599 → "server"
#   其它 → "other"
def error_kind(status_code: int) -> str:
    pass


# ---------- 题 6：综合 —— 规范化结果 ----------
# 写 normalize(status_code: int, payload: dict) -> dict：
#   返回 {
#     "ok": is_success(status_code),
#     "kind": "ok" if ok else error_kind(status_code),
#     "message": get_message(payload),
#   }
#   注意：成功时 kind 固定为 "ok"（即使 status 是 201 也一样）。
def normalize(status_code: int, payload: dict) -> dict:
    pass


# ============ 测试框架（不用改）============
def run_tests(title: str, cases: list[tuple]) -> bool:
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        passed = expected == actual
        ok += passed
        mark = "✅" if passed else "❌"
        print(f"  {mark} 用例{i:02d} {desc}")
        if not passed:
            print(f"        期望: {expected!r}")
            print(f"        实际: {actual!r}")
    total = len(cases)
    print(f"  ---> {title}: {ok}/{total} 通过")
    return ok == total


if __name__ == "__main__":
    all_pass = True

    all_pass &= run_tests("题1 is_success", [
        (is_success(200), True, "200"),
        (is_success(201), True, "201"),
        (is_success(299), True, "299"),
        (is_success(199), False, "199"),
        (is_success(404), False, "404"),
    ])

    all_pass &= run_tests("题2 build_url", [
        (build_url("https://api.example/x", {}), "https://api.example/x", "无参数"),
        (build_url("https://api.example/items", {"q": "py", "page": 2}),
         "https://api.example/items?q=py&page=2", "两个参数"),
    ])

    all_pass &= run_tests("题3 auth_headers", [
        (auth_headers("abc"), {"Authorization": "Bearer abc"}, "token"),
    ])

    all_pass &= run_tests("题4 get_message", [
        (get_message({"message": "ok"}), "ok", "有 message"),
        (get_message({"msg": "x"}), "", "无 message"),
        (get_message({"message": 1}), "", "非 str"),
    ])

    all_pass &= run_tests("题5 error_kind", [
        (error_kind(404), "client", "404"),
        (error_kind(500), "server", "500"),
        (error_kind(200), "other", "200"),
    ])

    all_pass &= run_tests("题6 normalize", [
        (normalize(200, {"message": "done"}),
         {"ok": True, "kind": "ok", "message": "done"}, "成功"),
        (normalize(404, {"message": "missing"}),
         {"ok": False, "kind": "client", "message": "missing"}, "客户端错"),
        (normalize(503, {}),
         {"ok": False, "kind": "server", "message": ""}, "服务端错无消息"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！from-zero 基础课收官！")
        print("   下一步：大复习 → 自己开一个小项目（CLI + logging + requests + pytest）。")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
