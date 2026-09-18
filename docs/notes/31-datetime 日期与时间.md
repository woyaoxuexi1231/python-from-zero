# 第 31 课：datetime 日期与时间

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：datetime/date/time、strftime 格式化、strptime 解析、timedelta 加减、比较与 .replace；配文件名时间戳与到期日练习。

---

日志要「几点几分」、成绩要记「哪天改的」、导出文件要「YYYYMMDD」的时间戳。 裸手拼字符串容易错、对不齐。这一课用标准库 `datetime` 把这几件事做对：构造、格式化、解析、加减、比较。

## 这一课解决什么问题

- 拿现在 → `datetime.now()` / `date.today()`
- 时刻变字符串 → `strftime`（文件名时间戳）
- 字符串变时刻 → `strptime`（解析输入）
- 加几天几小时 → `timedelta`
- 日期比大小、算间隔 → 直接 `<`/`-`，差值取 `.days`

## 三种口味

```python
from datetime import date, time, datetime, timedelta

now = datetime.now()   # 年月日 + 时分秒 + 微秒
today = date.today()   # 只要年月日

d  = date(2026, 8, 24)        # 年、月、日
t  = time(9, 30, 15)          # 时、分、秒
dt = datetime(2026, 8, 24, 9, 30, 15)
```

> **踩坑**
>
> `date()`/`datetime()` 参数顺序是 **年、月、日**。 最容易写反成（日,月,年），结果静默变成另一天。

## 格式化：strftime（时刻 → 字符串）

```python
dt = datetime(2026, 8, 24, 9, 30, 15)
dt.strftime("%Y-%m-%d %H:%M:%S")   # "2026-08-24 09:30:15"
dt.strftime("%Y%m%d_%H%M%S")       # "20260824_093015"  ← 文件名时间戳
dt.strftime("%A")                  # "Monday"（星期全文）
```

常用格式码：`%Y`年、`%m`月、`%d`日、`%H`时、`%M`分、`%S`秒、`%A`星期。

## 解析：strptime（字符串 → 时刻）

```python
parsed = datetime.strptime("2026-08-24 09:30:15", "%Y-%m-%d %H:%M:%S")
# parsed == datetime(2026, 8, 24, 9, 30, 15)
```

> **踩坑**
>
> 用于解析的**格式必须和字符串完全对齐**，对不齐抛 `ValueError`。 解析用户输入时通常 `try/except` 包住（第 8 课），匹配 SLO 失败回退默认值。

## 加减：timedelta

```python
tomorrow = now + timedelta(days=1)
early    = now - timedelta(days=3, hours=2)
earlier  = now + timedelta(minutes=30)

span = end - start          # 得到 timedelta
span.days                   # 整天天数
span.total_seconds()        # 总秒数
```

## 比较与微调

```python
now < later          # True，datetime 直接比大小
now.replace(hour=0, minute=0, second=0)   # 改某字段，其余不变 → 当天零点
```

> **不可变**
>
> `datetime`/`date` 都是不可变的。`.replace(...)`、`+ timedelta` 返回**新对象**,要重新接住变量,原对象不变。

## 配课怎么练

2. 先跑 `31_datetime.py`，对照输出。
4. 再打开 `31_datetime_exercise.py`，6 题：文件名时间戳、解析、算间隔、问候、到期日、时长格式化。
6. 题 2 要给多个格式 `for fmt in [...]` 循环试，题 3/题 6 注意算整天和除数要整除。

## 收束

datetime 是「时间」的操作集：构造、格式化、解析、加减、比较,配 `timedelta` 就够日常脚本。 下一课按标准库地图.next 是 `re`(从文本里抠字段),或先做个 26~31 的小复习。

---

上一课：[第 30 课：enum 枚举](30-enum 枚举.md)　|　下一课：[第 32 课：re 正则表达式](32-re 正则表达式.md)
