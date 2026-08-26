# ============================================================
# 第 31 课（练习）：datetime —— 全部是新场景
# 运行方式：python 31_datetime/31_datetime_exercise.py
# ============================================================
from datetime import date, time, datetime, timedelta

# 先读 31_datetime.py。下面 6 题全是新场景。写完自检 ✅/❌。

# ---------- 题 1：文件名时间戳 ----------
# 写 file_stamp(dt: datetime) -> str：
#   返回形如 "20260824_093015"（年月日时分秒，10 位时间戳回流不冲突也不重复）。
def file_stamp(dt: datetime) -> str:
    pass


# ---------- 题 2：解析不确定格式的日期 ----------
# 写 parse_dt(raw: str) -> datetime | None：
#   依次尝试 ["%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y/%m/%d"]，
#   成功返回解析结果，全失败返回 None（别让程序崩）。
def parse_dt(raw: str) -> datetime | None:
    pass


# ---------- 题 3：距离某天还有几天 ----------
# 写 days_until(target: datetime, now: datetime) -> int：
#   返回从 now 到 target 还有多少整天（用 t.days；不足一天算 0；已过去算负数）。
def days_until(target: datetime, now: datetime) -> int:
    pass


# ---------- 题 4：按当前时间返回问候 ----------
# 写 greeting(now: datetime) -> str：
#   5-12 点 "早上好"，12-18 "下午好"，其他 "晚上好"。
def greeting(now: datetime) -> str:
    pass


# ---------- 题 5：到期日 = 签发日 + N 天 ----------
# 写 expire_at(issued: date, valid_days: int) -> date：
#   返回签发日期加 valid_days 天。
def expire_at(issued: date, valid_days: int) -> date:
    pass


# ---------- 题 6：综合 —— 时长格式化 ----------
# 写 human_delta(seconds: int) -> str：
#   把秒数格式成 "X天X小时"（天为整数部分 /86400，小时为余数 /3600）；
#   不足 1 天只显示 "X小时"，测试只看整段，先按正确公式算。
def human_delta(seconds: int) -> str:
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

    all_pass &= run_tests("题1 file_stamp", [
        (file_stamp(datetime(2026, 8, 24, 9, 30, 15)),
         "20260824_093015", "精确到秒"),
        (file_stamp(datetime(2026, 1, 2, 3, 4, 5)),
         "20260102_030405", "补零"),
    ])

    all_pass &= run_tests("题2 parse_dt", [
        (parse_dt("2026-08-24 09:30:15"),
         datetime(2026, 8, 24, 9, 30, 15), "完整格式"),
        (parse_dt("2026-08-24"),
         datetime(2026, 8, 24, 0, 0, 0), "纯日期"),
        (parse_dt("2026/08/24"),
         datetime(2026, 8, 24, 0, 0, 0), "斜杠格式"),
        (parse_dt("乱写的"), None, "解析失败回 None"),
    ])

    all_pass &= run_tests("题3 days_until", [
        (days_until(datetime(2026, 8, 28), datetime(2026, 8, 24)), 4, "未来 4 天"),
        (days_until(datetime(2026, 8, 24), datetime(2026, 8, 24)), 0, "同一天"),
        (days_until(datetime(2026, 8, 24, 9), datetime(2026, 8, 24, 18)),
         -1, "过去一天"),
    ])

    all_pass &= run_tests("题4 greeting", [
        (greeting(datetime(2026, 8, 24, 7)), "早上好", "7 点"),
        (greeting(datetime(2026, 8, 24, 12)), "下午好", "12 点整"),
        (greeting(datetime(2026, 8, 24, 20)), "晚上好", "20 点"),
    ])

    all_pass &= run_tests("题5 expire_at", [
        (expire_at(date(2026, 8, 24), 7), date(2026, 8, 31), "签发+7 天"),
        (expire_at(date(2026, 8, 24), 0), date(2026, 8, 24), "当天到期"),
    ])

    all_pass &= run_tests("题6 human_delta", [
        (human_delta(86400 * 2 + 3600), "2天1小时", "两天整加一小时"),
        (human_delta(3600 * 3), "3小时", "不足一天只要小时"),
        (human_delta(0), "0小时", "零秒"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部通过！datetime 可以上手用了！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")