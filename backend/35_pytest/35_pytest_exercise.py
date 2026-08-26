# ============================================================
# 第 35 课（练习）：pytest 思维 —— 可测函数（新场景）
# 运行方式：python 35_pytest/35_pytest_exercise.py
# 选做：自己写 test_*.py，用 pytest 再验
# ============================================================
# 先读 35_pytest.py，并跑通：python -m pytest 35_pytest/ -v
# 下面 6 题写「好测」的小函数。写完自检 ✅/❌。


# ---------- 题 1：减法 ----------
# 写 sub(a: int, b: int) -> int：返回 a - b。
def sub(a: int, b: int) -> int:
    pass


# ---------- 题 2：是否偶数 ----------
# 写 is_even(n: int) -> bool：偶数 True，奇数 False。
def is_even(n: int) -> bool:
    pass


# ---------- 题 3：限幅 ----------
# 写 clip(x: int, lo: int, hi: int) -> int：
#   若 lo > hi → raise ValueError("lo 不能大于 hi")
#   否则返回落在 [lo, hi] 内的 x（小于 lo 取 lo，大于 hi 取 hi）。
def clip(x: int, lo: int, hi: int) -> int:
    pass


# ---------- 题 4：首词 ----------
# 写 first_word(text: str) -> str：
#   按空格拆，返回第一个非空片段；若全空白 → ""。
#   例："  hello world" → "hello"；"   " → ""
def first_word(text: str) -> str:
    pass


# ---------- 题 5：安全除法 ----------
# 写 safe_div(a: float, b: float) -> float：
#   b == 0 → raise ZeroDivisionError("除数不能为 0")
#   否则返回 a / b。
def safe_div(a: float, b: float) -> float:
    pass


# ---------- 题 6：等级 ----------
# 写 letter_grade(score: int) -> str：
#   score 不在 0~100 → raise ValueError("分数越界")
#   >=90 → "A"；>=80 → "B"；>=70 → "C"；>=60 → "D"；否则 "F"
def letter_grade(score: int) -> str:
    pass


# ============ 测试框架（不用改）============
# 下面用「手写断言」模拟 pytest 思路；真正项目请用 pytest 文件。
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


def expect_raises(exc_type: type, fn, *args) -> bool:
    try:
        fn(*args)
    except exc_type:
        return True
    except Exception:
        return False
    return False


if __name__ == "__main__":
    all_pass = True

    all_pass &= run_tests("题1 sub", [
        (sub(5, 3), 2, "5-3"),
        (sub(0, 1), -1, "0-1"),
    ])

    all_pass &= run_tests("题2 is_even", [
        (is_even(2), True, "2"),
        (is_even(3), False, "3"),
        (is_even(0), True, "0"),
    ])

    all_pass &= run_tests("题3 clip", [
        (clip(5, 0, 10), 5, "中间"),
        (clip(-1, 0, 10), 0, "低于 lo"),
        (clip(99, 0, 10), 10, "高于 hi"),
        (expect_raises(ValueError, clip, 1, 10, 0), True, "lo>hi 抛错"),
    ])

    all_pass &= run_tests("题4 first_word", [
        (first_word("hello world"), "hello", "普通"),
        (first_word("  hi  there"), "hi", "前导空格"),
        (first_word("   "), "", "全空白"),
    ])

    all_pass &= run_tests("题5 safe_div", [
        (safe_div(10, 2), 5.0, "10/2"),
        (expect_raises(ZeroDivisionError, safe_div, 1, 0), True, "除零"),
    ])

    all_pass &= run_tests("题6 letter_grade", [
        (letter_grade(95), "A", "A"),
        (letter_grade(80), "B", "B"),
        (letter_grade(70), "C", "C"),
        (letter_grade(60), "D", "D"),
        (letter_grade(59), "F", "F"),
        (expect_raises(ValueError, letter_grade, -1), True, "越界低"),
        (expect_raises(ValueError, letter_grade, 101), True, "越界高"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！可以去写真正的 test_*.py 了！")
        print("   提示：python -m pytest 35_pytest/ -v")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")
