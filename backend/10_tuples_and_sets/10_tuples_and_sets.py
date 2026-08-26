# ============================================================
# 第 10 课：元组、集合
# 运行方式：python 10_tuples_and_sets.py
# ============================================================

# 第 1 阶段结束：成绩本已经能转圈、能接住错误、能存盘。
# 这一课换两种新容器，后面几乎每天都会碰到。
#
# 列表 list  ：一排有顺序的东西，可以改。方括号 []
# 元组 tuple ：也是一排有顺序的东西，但不能改。圆括号 ()
# 集合 set   ：一堆不重复的东西，没有顺序。set() 或 {1, 2, 3}
#
# 字典的 {} 是 键: 值。集合的 {} 里没有冒号。空集合必须写 set()，
# 写成 {} 得到的是空字典。


# ---------- 1. 元组：和列表很像，但不能改 ----------

point: tuple[int, int] = (3, 5)
print(point)
print(point[0])  # 3   索引和列表一样，从 0 开始
print(len(point))  # 2
print("-----")

# 下面这行如果取消注释会报 TypeError：元组不支持赋值
# point[0] = 10

# 列表可以改，对比一下：
nums: list[int] = [3, 5]
nums[0] = 10
print(nums)  # [10, 5]
print("-----")

# ---------- 2. 拆包：一次解开多个值 ----------
# 左边写几个名字，右边元组有几项，就会一一对应赋进去。
# 这是元组最常见的用法，比 point[0]、point[1] 更清楚。

x, y = point
print(x)  # 3
print(y)  # 5
print("-----")


# 第 5 课其实已经用过拆包：
#   for name, score in scores.items():
# items() 每一轮给出的就是 (键, 值) 这个元组。


# ---------- 3. 函数返回多个值：其实是返回一个元组 ----------
# return a, b  等价于  return (a, b)
# 调用的一边用两个变量接住，就是拆包。

def min_and_max(numbers: list[int]) -> tuple[int, int]:
    smallest = numbers[0]
    largest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest


low, high = min_and_max([8, 3, 15, 1])
print(low)  # 1
print(high)  # 15
print("-----")

# 也可以先整包接住，再自己拆：
pair = min_and_max([8, 3, 15, 1])
print(pair)  # (1, 15)
print(type(pair))  # <class 'tuple'>
print("-----")

# ---------- 4. 集合：自动去重，用 in 问「有没有」很快 ----------

tags: set[str] = {"python", "java", "python"}
print(tags)  # 只有两个，重复的 python 被丢掉。打印顺序不一定
print("-----")

# in：问这个值在不在集合里
print("python" in tags)  # True
print("go" in tags)  # False
print("-----")

# add / remove
tags.add("go")
print(tags)
tags.remove("java")
print(tags)
print("-----")

# 空集合：
empty: set[str] = set()
print(empty)
print(type({}))  # <class 'dict'>   空花括号是字典
print(type(set()))  # <class 'set'>
print("-----")

# ---------- 5. 两个集合可以求交集、并集 ----------
# & 两个都有
# | 至少有一个有

class_a: set[str] = {"小明", "hulei", "小红"}
class_b: set[str] = {"hulei", "小刚", "小红"}
print(class_a & class_b)  # 两班都有的人
print(class_a | class_b)  # 两班合在一起（去重）
print("-----")

# ---------- 6. 列表 → 集合：最快的去重办法 ----------

raw: list[str] = ["小明", "hulei", "小明", "小红"]
unique: set[str] = set(raw)
print(unique)
print("-----")

# ---------- 练习 ----------
# 1. 写函数 swap(a: int, b: int) -> tuple[int, int]
#    返回 (b, a)，也就是把两个数对调。
#    调用：x, y = swap(1, 2)
#    print 出来应该是 2 和 1。
#
# 2. 写函数 both_passed(a: set[str], b: set[str]) -> set[str]
#    返回两份名单里都出现的名字（交集）。
#    用下面这两个集合调用，print 结果。
#
# 写在下面，保存后再运行。

math_passed: set[str] = {"小明", "hulei", "小刚"}
english_passed: set[str] = {"hulei", "小红", "小刚"}


def swap(a: int, b: int) -> tuple[int, int]:
    return b, a

x, y = swap(1, 2)

print(f"交换 1,2 结果为: {x}, {y}")


def both_passed(a: set[str], b: set[str]) -> set[str]:
    return a & b

print(both_passed(math_passed, english_passed))