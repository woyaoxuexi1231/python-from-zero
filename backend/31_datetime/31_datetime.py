# ============================================================
# 第 31 课（知识讲解）：datetime —— 和「时间」打交道
# 运行方式：python 31_datetime/31_datetime.py
# 配套练习：31_datetime_exercise.py（自检，全是新场景）
# ============================================================
from datetime import date, time, datetime, timedelta

# 痛点：日志要「几点几分」、成绩要记「哪天改的」、文件名要「YYYYMMDD」。
# 裸手拼字符串容易错；datetime 标准库把这些做对：解析、比较、加减、格式化。
# 三种口味：date(年月日) / time(时分秒) / datetime(两者都要)。
print("========== 第31课 datetime ==========\n")


# ---------- 1. 现在的时刻 ----------
print("【1】拿「现在」")
now = datetime.now()          # 完整：年月日时分秒+微秒
today = date.today()          # 只要年月日
print("  datetime.now():", now)
print("  date.today():", today)
print("  字段提:(year, month, day =", today.year, today.month, today.day, ")")
print("  hour/minute/second =", now.hour, now.minute, now.second)


# ---------- 2. 自己构造一个时刻 ----------
print("\n【2】按需构造")
d = date(2026, 8, 24)                     # 年、月、日（缺省在中间，别写错顺序）
t = time(9, 30, 15)                       # 时、分、秒
dt = datetime(2026, 8, 24, 9, 30, 15)     # 合体
print("  date:", d, "| time:", t, "| datetime:", dt)


# ---------- 3. 结构化与格式化：strftime（对象 → 字符串） ----------
print("\n【3】strftime：把时刻变成字符串")
dt = datetime(2026, 8, 24, 9, 30, 15)
print("  %Y 年:", dt.strftime("%Y"))                       # 2026
print("  %m %d:", dt.strftime("%Y-%m-%d"))                # 2026-08-24（常用）
print("  %H %M %S:", dt.strftime("%Y-%m-%d %H:%M:%S"))    # 2026-08-24 09:30:15
print("  文件名推荐:", dt.strftime("%Y%m%d_%H%M%S"))       # 20260824_093015
print("  星期几:", dt.strftime("%A"), "| %a:", dt.strftime("%a"))


# ---------- 4. 解析：strptime（字符串 → 时刻） ----------
print("\n【4】strptime：把字符串按格式读回来")
s = "2026-08-24 09:30:15"
parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print("  解析结果:", parsed, "| 类型:", type(parsed).__name__)
print("  只取日期:", parsed.date())
# 格式要对上：给错格式会 ValueError，通常 try/except 接住（第 8 课）。
try:
    datetime.strptime("24/08/2026", "%Y-%m-%d")
except ValueError as e:
    print("  格式不符:", e)


# ---------- 5. 加减：timedelta ----------
print("\n【5】timedelta：加几天、减几小时")
now = datetime(2026, 8, 24, 10, 0, 0)
tomorrow = now + timedelta(days=1)
ago3 = now - timedelta(days=3, hours=2)
print("  明天:", tomorrow)
print("  三天两小时前:", ago3)
print("  加 30 分钟:", now + timedelta(minutes=30))
print("  表示「时长」:", timedelta(days=1) + timedelta(hours=5))


# ---------- 6. 比较与差值 ----------
print("\n【6】日期比大小、算间隔")
start = datetime(2026, 8, 20, 8, 0, 0)
end = datetime(2026, 8, 24, 8, 0, 0)
print("  start < end:", start < end)
span = end - start
print("  相隔:", span, "| span.days =", span.days)         # timedelta 再取 .days
print("  多少秒:", span.total_seconds())


# ---------- 7. 一天内的 .replace 微调 ----------
print("\n【7】.replace：改某个字段，其余不动")
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
print("  当天零点:", midnight)
print("  不变式: replace 原对象仍")  # datetime 不可变，返回新对象


# ---------- 8. 易错点 ----------
print("\n【8】易错点速记")
print("  ① datetime 不可变：now.replace(...) 返回新值，要接住变量")
print("  ② 构造 date() 顺序是 年、月、日——写成(日,月,年)最常见错")
print("  ③ strptime 格式必须和你给的字符串完全对上，否则 ValueError")
print("  ④ 本地 naive vs 带时区 aware：跨时区/部署再讲，这里保持本地 naive")
print("  ⑤ 只用日期/只用时间，选 date / time；都要用 datetime")
print("  ⑥ 时间戳 to timestamp()，存库常用 now.timestamp()")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("datetime.now() / date.today()   —— 现在")
print("datetime(y, mo, d, h, mi, s)    —— 自己造")
print("dt.strftime('%Y-%m-%d %H:%M:%S')-> 时刻→字符串（格式化）")
print("datetime.strptime(s, fmt)       —— 字符串→时刻（要 try/except）")
print("+/- timedelta(days=…, hours=…)  —— 加减时间")
print("两时刻相减 → timedelta，取 .days / .total_seconds()")
print(">=< 直接比较两个 datetime")
print("格式码: %Y年 %m月 %d日 %H时 %M分 %S秒 %A星期全文")