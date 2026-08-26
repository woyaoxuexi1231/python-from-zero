# ============================================================
# 第 33 课（练习）：argparse —— 全部是新场景
# 运行方式：python 33_argparse/33_argparse_exercise.py
# ============================================================
import argparse

# 先读 33_argparse.py。下面 6 题全是新场景。写完自检 ✅/❌。
# 提示：每道题都要在函数里创建自己的 ArgumentParser；用 parse_args(argv) 传列表。

# ---------- 题 1：双数相加 ----------
# 写 add_from_argv(argv: list[str]) -> int：
#   声明两个位置参数 a、b（都 type=int），返回 a + b。
#   例：["3", "5"] → 8
def add_from_argv(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("a", type=int)
    p.add_argument("b", type=int)
    args = p.parse_args(argv)
    return args.a + args.b


# ---------- 题 2：重复问候 ----------
# 写 greet_from_argv(argv: list[str]) -> str：
#   位置参数 name；可选 --times（int，默认 1）。
#   返回把 f"你好，{name}" 用换行拼 times 次（末尾无多余换行）。
#   例：["小明", "--times", "2"] → "你好，小明\n你好，小明"
def greet_from_argv(argv: list[str]) -> str:
    p = argparse.ArgumentParser()
    p.add_argument("name")
    p.add_argument("--times", type=int, default=1)
    args = p.parse_args(argv)
    return "\n".join([f"你好，{args.name}"] * args.times)


# ---------- 题 3：大小写开关 ----------
# 写 echo_from_argv(argv: list[str]) -> str：
#   位置参数 text；可选 --upper（store_true）。
#   有 --upper 则返回 text.upper()，否则原样返回 text。
def echo_from_argv(argv: list[str]) -> str:
    p = argparse.ArgumentParser()
    p.add_argument("text")
    p.add_argument("--upper", action="store_true")
    args = p.parse_args(argv)
    return args.text.upper() if args.upper else args.text


# ---------- 题 4：choices 选模式 ----------
# 写 mode_from_argv(argv: list[str]) -> str：
#   可选 --mode，choices=["fast","safe"]，默认 "safe"。
#   返回解析到的 mode 字符串。
def mode_from_argv(argv: list[str]) -> str:
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["fast", "safe"], default="safe")
    args = p.parse_args(argv)
    return args.mode


# ---------- 题 5：复制描述 ----------
# 写 copy_desc(argv: list[str]) -> str：
#   位置参数 src、dst；可选 --force（store_true）。
#   无 --force → f"copy {src} -> {dst}"
#   有 --force → f"FORCE copy {src} -> {dst}"
def copy_desc(argv: list[str]) -> str:
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("--force", action="store_true")
    args = p.parse_args(argv)
    prefix = "FORCE " if args.force else ""
    return f"{prefix}copy {args.src} -> {args.dst}"


# ---------- 题 6：综合 —— 报告行 ----------
# 写 report_line(argv: list[str]) -> str：
#   位置参数 title；
#   可选 --date（str，默认 "today"）；
#   可选 -v/--verbose（store_true）。
#   非 verbose：f"[{date}] {title}"
#   verbose：f"[{date}] {title} (verbose)"
def report_line(argv: list[str]) -> str:
    p = argparse.ArgumentParser()
    p.add_argument("title")
    p.add_argument("--date", default="today")
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args(argv)
    suffix = " (verbose)" if args.verbose else ""
    return f"[{args.date}] {args.title}{suffix}"


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

    all_pass &= run_tests("题1 add_from_argv", [
        (add_from_argv(["3", "5"]), 8, "3+5"),
        (add_from_argv(["-1", "10"]), 9, "负数"),
    ])

    all_pass &= run_tests("题2 greet_from_argv", [
        (greet_from_argv(["小明"]), "你好，小明", "默认 1 次"),
        (greet_from_argv(["小明", "--times", "2"]),
         "你好，小明\n你好，小明", "两次"),
    ])

    all_pass &= run_tests("题3 echo_from_argv", [
        (echo_from_argv(["hello"]), "hello", "原样"),
        (echo_from_argv(["hello", "--upper"]), "HELLO", "转大写"),
    ])

    all_pass &= run_tests("题4 mode_from_argv", [
        (mode_from_argv([]), "safe", "默认"),
        (mode_from_argv(["--mode", "fast"]), "fast", "指定 fast"),
    ])

    all_pass &= run_tests("题5 copy_desc", [
        (copy_desc(["a.txt", "b.txt"]), "copy a.txt -> b.txt", "普通"),
        (copy_desc(["a.txt", "b.txt", "--force"]),
         "FORCE copy a.txt -> b.txt", "强制"),
    ])

    all_pass &= run_tests("题6 report_line", [
        (report_line(["周报"]), "[today] 周报", "默认 date"),
        (report_line(["周报", "--date", "2026-08-25"]),
         "[2026-08-25] 周报", "指定 date"),
        (report_line(["周报", "-v", "--date", "2026-08-25"]),
         "[2026-08-25] 周报 (verbose)", "verbose"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！argparse 可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
