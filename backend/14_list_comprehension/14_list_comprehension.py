# ============================================================
# 第 14 课：列表推导式
# 运行方式：python 14_list_comprehension.py
# ============================================================

# 第 4 课会用 for 往空列表里 append。
# 推导式把「建空列表 → 循环 → append」压成一行。
# 先会 for，再压缩。看不懂就拆回 for。


# ---------- 1. 先写你会的 for ----------

nums: list[int] = [1, 2, 3, 4]

doubled: list[int] = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6, 8]
print("-----")

# ---------- 2. 同一件事，写成推导式 ----------
# 读法从右往左：for 每一项，算出左边的表达式，放进新列表。
# [ 表达式 for 变量 in 可迭代对象 ]

doubled2 = [n * 2 for n in nums]
print(doubled2)
print("-----")

# ---------- 3. 加 if：只要符合条件的 ----------
# [ 表达式 for 变量 in ... if 条件 ]
# 条件写在最后。不符合的直接跳过，不会进新列表。

positives = [n for n in [-2, 0, 3, 5] if n > 0]
print(positives)  # [3, 5]
print("-----")

# 等价的 for：
positives2: list[int] = []
for n in [-2, 0, 3, 5]:
    if n > 0:
        positives2.append(n)
print(positives2)
print("-----")

# ---------- 4. 转换 + 过滤可以一起 ----------

scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
}

# 只要及格的人的名字
passed = [name for name, score in scores.items() if score >= 60]
print(passed)
print("-----")

# 把所有分数变成「XX 分」这种字符串
labels = [f"{score} 分" for score in scores.values()]
print(labels)
print("-----")

# ---------- 5. 什么时候别用 ----------
# 推导式适合：短、一眼能看懂的「映射 / 过滤」。
# 循环体里有很多步、要打印、要改外部变量 → 老老实实写 for。
# 嵌套两层以上的推导式，新手先别写，可读性很差。


# ---------- 6. 顺便知道：集合、字典也有 ----------
# 花括号 + 推导 → 集合；键: 值 + 推导 → 字典。
# 这一课练习只用列表 []。

unique_lens = {len(name) for name in scores}
print(unique_lens)

score_map = {name: score for name, score in scores.items() if score >= 60}
print(score_map)
print("-----")


# ---------- 练习 ----------
# 1. 写函数 squares(nums: list[int]) -> list[int]
#    返回每个数的平方。用推导式，不要手写 for + append。
#    squares([1, 2, 3, 4]) 应得到 [1, 4, 9, 16]
#
# 2. 写函数 adults(ages: list[int]) -> list[int]
#    返回所有 >= 18 的年龄。用带 if 的推导式。
#    adults([15, 18, 20, 12]) 应得到 [18, 20]
#
# 写在下面，保存后再运行。

def squares(nums_def: list[int]) -> list[int]:
    return [n_def * n_def for n_def in nums_def]


def adults(nums_def: list[int]) -> list[int]:
    return [n_def for n_def in nums_def if n_def >= 18]


print(squares([1, 2, 3, 4]))
print(adults([15, 18, 20, 12]))