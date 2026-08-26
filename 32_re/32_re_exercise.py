# ============================================================
# 第 32 课（练习）：re 正则 —— 全部是新场景
# 运行方式：python 32_re/32_re_exercise.py
# ============================================================
import re

# 先读 32_re.py。下面 6 题全是新场景。写完自检 ✅/❌。
# 提示：校验类优先 fullmatch；列表类优先 findall。

# ---------- 题 1：从日志里抠数字 ----------
# 写 extract_numbers(text: str) -> list[int]：
#   返回文本中所有连续数字段转成的 int 列表（按出现顺序）。
def extract_numbers(text: str) -> list[int]:
    pass


# ---------- 题 2：提取邮箱 ----------
# 写 extract_emails(text: str) -> list[str]：
#   返回文本中所有形如 xxx@yyy.zzz（字母/数字/点/下划线@字母.字母）的邮箱。
def extract_emails(text: str) -> list[str]:
    pass


# ---------- 题 3：校验手机号 ----------
# 写 is_valid_phone(raw: str) -> bool：
#   校验是否为 1 开头、共 11 位纯数字（用 fullmatch）。
def is_valid_phone(raw: str) -> bool:
    pass


# ---------- 题 4：取出年月日 ----------
# 写 extract_ymd(text: str) -> tuple[str, str, str] | None：
#   在文本中找第一处 YYYY-MM-DD，返回 (年, 月, 日)；找不到回 None。
def extract_ymd(text: str) -> tuple[str, str, str] | None:
    pass


# ---------- 题 5：压缩多余空白 ----------
# 写 clean_ws(text: str) -> str：
#   把连续的空白（空格/制表/换行）缩成一个空格，首尾去掉空白。
def clean_ws(text: str) -> str:
    pass


# ---------- 题 6：综合 —— 校验 IPv4 ----------
# 写 is_valid_ipv4(raw: str) -> bool：
#   校验是否为 由 1~3 位数字组成、以点分隔的 4 段（每段 0~255，
#   这里只需用字符合法性：4 段、每段 1~3 位数字、用 fullmatch；不用算数值）。
def is_valid_ipv4(raw: str) -> bool:
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

    all_pass &= run_tests("题1 extract_numbers", [
        (extract_numbers("id=7 合计 2026，余 15 件"), [7, 2026, 15], "多段数字"),
        (extract_numbers("没有数字"), [], "空列表"),
        (extract_numbers("v99_1"), [99, 1], "下划线分开也算两段"),
    ])

    all_pass &= run_tests("题2 extract_emails", [
        (extract_emails("联系 a.b_c@home.com 或 x@y.io"),
         ["a.b_c@home.com", "x@y.io"], "两个邮箱"),
        (extract_emails("无邮箱"), [], "没有"),
    ])

    all_pass &= run_tests("题3 is_valid_phone", [
        (is_valid_phone("13812345678"), True, "11 位 1 开头"),
        (is_valid_phone("2381234567"), False, "不是 1 开头"),
        (is_valid_phone("1381234567"), False, "只有 10 位"),
        (is_valid_phone("138a2345678"), False, "含字母"),
    ])

    all_pass &= run_tests("题4 extract_ymd", [
        (extract_ymd("出生 1999-12-31 登记"),
         ("1999", "12", "31"), "第一处日期"),
        (extract_ymd("没有日期"), None, "找不到"),
    ])

    all_pass &= run_tests("题5 clean_ws", [
        (clean_ws("  a   b\t\tc\n d  "), "a b c d", "多数空白压缩"),
        (clean_ws("ok"), "ok", "本来干净"),
    ])

    all_pass &= run_tests("题6 is_valid_ipv4", [
        (is_valid_ipv4("192.168.1.1"), True, "标准四个数字"),
        (is_valid_ipv4("1.2.3"), False, "只有三段"),
        (is_valid_ipv4("999.888.777.666"), True, "纯字符合法(数值校验另说)"),
        (is_valid_ipv4("1.2.3.4.5"), False, "五段"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！re 可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")