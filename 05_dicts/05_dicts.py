# ============================================================
# 第 5 课：字典
# 运行方式：python 05_dicts.py
# ============================================================

# ---------- 1. 字典：用名字找东西 ----------
# 列表靠编号：ages[0]
# 字典靠键（key）：scores["hulei"]
# 每一个键对应一个值（value）。
# 用花括号 {}，写成 键: 值。

scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}

print(scores)
print(scores["hulei"])  # 75
print("-----")

# ---------- 2. 读取、修改、添加 ----------
# 读：   scores["小明"]
# 改：   scores["小明"] = 95
# 加：   写一个原来没有的键，就是新增

print(scores["小明"])
scores["小明"] = 95
scores["小刚"] = 60
print(scores)
print("-----")

# ---------- 3. 键不存在会报错 ----------
# 下面这行如果取消注释会报 KeyError：
# print(scores["不存在的人"])
#
# 先用 in 问问，再去取。

if "hulei" in scores:
    print("找到了 hulei")
else:
    print("没有这个人")
print("-----")

# ---------- 4. 循环字典 ----------
# for name in scores:           拿到的是键
# scores[name]                  再用键去取值
# for name, score in scores.items():  键和值一起拿

for name in scores:
    print(f"{name} 的分数是 {scores[name]}")
print("-----")

for name, score in scores.items():
    if score >= 60:
        print(f"{name} 及格了，{score} 分")
    else:
        print(f"{name} 不及格，{score} 分")
print("-----")


# ---------- 5. 字典可以当函数的参数和返回值 ----------

def get_score(scores: dict[str, int], name: str) -> int:
    return scores[name]


print(get_score(scores, "小红"))  # 40
print("-----")


# ---------- 练习 ----------
# 1. 写函数 total_score(scores: dict[str, int]) -> int
#    把字典里所有分数加起来返回。
#    用上面的 scores 调用，print 结果。
#
# 2. 写函数 passed_count(scores: dict[str, int]) -> int
#    统计有几个人分数 >= 60。
#    用上面的 scores 调用，print 结果。
#
# 写在下面，保存后再运行。


def total_score(scores2: dict[str, int]) -> int:
    return sum(scores2.values())


total_score_num = total_score(scores)
print(f"总分是：{total_score_num}")


def passed_count(scores2: dict[str, int]) -> int:
    result = 0
    for k, v in scores2.items():
        if v > 60:
            result += 1

    return result

passed_count = passed_count(scores)
print(f"总分大于60的人一共有 {passed_count} 人")
