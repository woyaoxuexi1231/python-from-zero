# ============================================================
# 第 12 课：None、真假值、and / or
# 运行方式：python 12_none_and_or.py
# ============================================================

# get_score 找不到人时返回 None。None 表示「没有值」，接近 Java 的 null。
# 这一课把「怎么判断没有」和「if 到底把什么当成真」说清楚。


# ---------- 1. None：专门表示没有 ----------
# 它是一个值，类型是 NoneType。不是 0，也不是 ""。

missing = None
print(missing)
print(type(missing))
print("-----")


def get_score(book: dict[str, int], name: str) -> int | None:
    if name in book:
        return book[name]
    else:
        return None


scores: dict[str, int] = {"小明": 90, "hulei": 0, "小红": 40}

print(get_score(scores, "小明"))  # 90
print(get_score(scores, "不存在"))  # None
print("-----")

# ---------- 2. 判断没有：用 is None，不要用 == ----------
# is 问的是「是不是同一个东西」。None 全世界只有一份，所以用 is。
# == 问的是「值相不相等」。对 None 碰巧也能用，但习惯上写 is None。

score = get_score(scores, "不存在")
if score is None:
    print("没有这个人")
else:
    print(f"{score} 分")
print("-----")

score = get_score(scores, "小明")
if score is not None:
    print(f"找到了：{score}")
print("-----")

# ---------- 3. if 会把很多东西当成假 ----------
# 下面这些在 if 里都相当于 False：
#   None   False   0   0.0   ""   []   {}   set()
# 其他大多数都相当于 True，包括非空字符串、非空列表、非 0 数字。

print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool("hulei"))
print(bool(90))
print("-----")

# 所以可以写：
name = ""
if not name:
    print("名字是空的")
print("-----")

# ---------- 4. 0 分是有效分数，不能用 if score 判断「有没有」----------
# hulei 是 0 分。0 在 if 里是假的，但人是存在的。

score = get_score(scores, "hulei")
if score:
    print("用 if score：会认为没有")  # 不会打印，因为 0 是假
if score is not None:
    print(f"用 is not None：hulei 是 {score} 分")  # 会打印
print("-----")

# 规则：
#   判断「有没有这个值」→ is None / is not None
#   判断「字符串/列表空不空」→ if name: / if not name:
#   判断分数高低     → score >= 60，不要靠真假值


# ---------- 5. and / or ----------
# and：两边都真，整个才真。左边假就不再算右边（短路）。
# or ：有一边真，整个就真。左边真就不再算右边。

age = 20
name = "hulei"
if age >= 18 and name != "":
    print("成年且有名字")
print("-----")

choice = "q"
if choice == "0" or choice == "q":
    print("要退出")
print("-----")

# ---------- 6. and / or 的结果不一定是 True / False ----------
# 它们返回「最后被算到的那个值」。
# 常见写法：空字符串时用一个默认值。

print("" or "匿名")  # 匿名   左边假，取右边
print("hulei" or "匿名")  # hulei  左边真，不再看右边
print("-----")


# ---------- 练习 ----------
# 1. 写函数 format_score(score: int | None) -> str
#    score 是 None 时返回 "缺考"；否则返回 f"{score} 分"。
#    必须用 is None 判断。
#    print(format_score(90))      应得到 90 分
#    print(format_score(0))       应得到 0 分     ← 0 不能当成缺考
#    print(format_score(None))    应得到 缺考
#
# 2. 写函数 can_save(name: str, score: int | None) -> bool
#    名字非空、而且分数不是 None，才返回 True。
#    用 and 连接两个条件。
#    print(can_save("小刚", 60))   True
#    print(can_save("", 60))       False
#    print(can_save("小刚", None)) False
#
# 写在下面，保存后再运行。

def format_score(def_score: int | None) -> str:
    if def_score is None:
        return "缺考"
    else:
        return f"{def_score}分"


print(format_score(90))
print(format_score(0))
print(format_score(None))


def can_save(def_name: str | None, def_score: int | None) -> bool:
    if def_name and def_score is not None:
        return True
    else:
        return False


print(can_save("小刚", 60))
print(can_save("", 60))
print(can_save("小刚", None))
