# ============================================================
# 第 34 课（练习）：logging —— 全部是新场景
# 运行方式：python 34_logging/34_logging_exercise.py
# ============================================================
import io
import logging

# 先读 34_logging.py。下面 6 题全是新场景。写完自检 ✅/❌。
# 提示：捕获日志可用 StringIO + StreamHandler；别依赖真实控制台。


# ---------- 题 1：模块 logger ----------
# 写 get_worker_logger() -> logging.Logger：
#   返回 logging.getLogger("worker")。
def get_worker_logger() -> logging.Logger:
    pass


# ---------- 题 2：verbose → 级别（承接 argparse） ----------
# 写 level_for_verbose(verbose: bool) -> int：
#   verbose 为 True → logging.DEBUG；否则 logging.INFO。
def level_for_verbose(verbose: bool) -> int:
    pass


# ---------- 题 3：字符串 → 级别常量 ----------
# 写 level_from_name(name: str) -> int：
#   "debug"→DEBUG, "info"→INFO, "warning"→WARNING, "error"→ERROR（大小写不敏感）
#   未知字符串 → logging.INFO
def level_from_name(name: str) -> int:
    pass


# ---------- 题 4：捕获一条 INFO ----------
# 写 capture_info(message: str) -> str：
#   新建 logger 名 "capture"（handlers 清空、propagate=False、level=INFO），
#   挂 StreamHandler(io.StringIO())，只打一条 logger.info(message)，
#   返回捕获到的字符串（去掉首尾空白）。不要 basicConfig。
def capture_info(message: str) -> str:
    pass


# ---------- 题 5：按级别过滤消息 ----------
# 写 filter_messages(level: int, records: list[tuple[int, str]]) -> list[str]：
#   records 里每项是 (级别常量, 消息文本)。
#   返回「级别 >= level」的消息列表（保持原顺序）。
#   例：level=INFO 时 DEBUG 丢掉，INFO/WARNING/ERROR 保留。
def filter_messages(level: int, records: list[tuple[int, str]]) -> list[str]:
    pass


# ---------- 题 6：综合 —— 问候日志行 ----------
# 写 greet_log_line(name: str, verbose: bool) -> str：
#   level = level_for_verbose(verbose)
#   用 logger 名 "greet"，同样 StringIO 捕获；
#   verbose 时先 logger.debug(f"准备问候 {name}")（可不捕获 debug，只关心 INFO）；
#   再 logger.info(f"你好，{name}")；
#   返回捕获到的**最后一行** INFO 正文（即 "你好，{name}"）。
def greet_log_line(name: str, verbose: bool) -> str:
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

    w = get_worker_logger()
    all_pass &= run_tests("题1 get_worker_logger", [
        (w.name, "worker", "logger 名"),
        (type(w), logging.Logger, "类型"),
    ])

    all_pass &= run_tests("题2 level_for_verbose", [
        (level_for_verbose(False), logging.INFO, "默认 INFO"),
        (level_for_verbose(True), logging.DEBUG, "verbose DEBUG"),
    ])

    all_pass &= run_tests("题3 level_from_name", [
        (level_from_name("debug"), logging.DEBUG, "debug"),
        (level_from_name("INFO"), logging.INFO, "大写 info"),
        (level_from_name("Warning"), logging.WARNING, "混合 warning"),
        (level_from_name("error"), logging.ERROR, "error"),
        (level_from_name("unknown"), logging.INFO, "未知默认 INFO"),
    ])

    all_pass &= run_tests("题4 capture_info", [
        (capture_info("启动完成"), "启动完成", "普通消息"),
        (capture_info(""), "", "空串"),
    ])

    sample = [
        (logging.DEBUG, "d"),
        (logging.INFO, "i"),
        (logging.WARNING, "w"),
        (logging.ERROR, "e"),
    ]
    all_pass &= run_tests("题5 filter_messages", [
        (filter_messages(logging.DEBUG, sample), ["d", "i", "w", "e"], "全保留"),
        (filter_messages(logging.INFO, sample), ["i", "w", "e"], "去掉 DEBUG"),
        (filter_messages(logging.WARNING, sample), ["w", "e"], "只要 WARNING+"),
        (filter_messages(logging.ERROR, sample), ["e"], "只要 ERROR"),
    ])

    all_pass &= run_tests("题6 greet_log_line", [
        (greet_log_line("小明", False), "你好，小明", "普通"),
        (greet_log_line("Bob", True), "你好，Bob", "verbose 仍返回 INFO 行"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！logging 可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
