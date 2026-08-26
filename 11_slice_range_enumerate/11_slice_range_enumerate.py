# ============================================================
# 第 11 课：切片、range、enumerate
# 运行方式：python 11_slice_range_enumerate.py
# ============================================================

# 第 4 课会取单个：names[0]
# 这一课取一段、按次数循环、循环时同时拿到编号。
#
# Java 没有切片。range 接近 for (int i = 0; i < n; i++)。
# enumerate 接近「既要下标又要元素」时的写法。


# ---------- 1. 切片：取一段，不含结尾 ----------
# names[start:end]  从 start 取到 end 之前。
# end 那个位置本身不包含。这和 range、和 Java 的 substring 一样。

names: list[str] = ["小明", "hulei", "小红", "小刚"]

print(names[0:2])  # ['小明', 'hulei']   第 0、1 个，没有第 2 个
print(names[1:3])  # ['hulei', '小红']
print("-----")

# 省略一边：从头取、取到尾。
print(names[:2])  # 前两个
print(names[2:])  # 从下标 2 一直到结束
print(names[:])  # 整份拷贝，原列表不受影响
print("-----")

# 切片得到的是新列表。改拷贝不会改原来的。
copy = names[:]
copy[0] = "改了"
print(copy)
print(names)
print("-----")

# ---------- 2. 负数下标：从尾巴数 ----------
# -1 是最后一个，-2 是倒数第二个。

print(names[-1])  # 小刚
print(names[-2:])  # 最后两个
print(names[:-1])  # 去掉最后一个
print("-----")

# ---------- 3. 步长：每隔几个取一个 ----------
# [start:end:step]

nums: list[int] = [0, 1, 2, 3, 4, 5, 6]
print(nums[::2])  # [0, 2, 4, 6]  每隔一个
print(nums[1:5:2])  # [1, 3]
print("-----")

# 字符串也能切片，规则完全一样。
word = "Python"
print(word[:3])  # Pyt
print(word[-2:])  # on
print("-----")

# ---------- 4. range：需要转几圈、或需要连续整数时用 ----------
# range(3)          → 0, 1, 2        到 3 之前
# range(1, 4)       → 1, 2, 3
# range(0, 6, 2)    → 0, 2, 4
# 它不是列表。print(range(3)) 看到的是 range(0, 3)，要用 list() 才能看清。

print(list(range(3)))
print(list(range(1, 4)))
print(list(range(0, 6, 2)))
print("-----")

for i in range(3):
    print(f"第 {i} 圈")
print("-----")

# 已经有列表时，直接 for name in names，不要先 range(len(names))。
# range 适合：没有现成列表、只想重复 n 次、或只要数字本身。


# ---------- 5. enumerate：循环时同时要编号和值 ----------
# 每一轮得到一个元组 (下标, 值)，用第 10 课的拆包接住。
# 默认从 0 起。start=1 就从 1 起，做排名时常用。

for i, name in enumerate(names):
    print(f"{i}: {name}")
print("-----")

for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")
print("-----")


# ---------- 练习 ----------
# 1. 写函数 first_n(items: list[str], n: int) -> list[str]
#    返回列表的前 n 项。用切片，不要自己 for。
#    first_n(["a", "b", "c", "d"], 2) 应该是 ["a", "b"]。
#
# 2. 写函数 print_ranked(items: list[str]) -> None
#    用 enumerate(..., start=1) 打印成：
#        1. 小明
#        2. hulei
#        ...
#    用下面的 names 调用一次。
#
# 两个函数都写好后，用 print / 调用把结果打出来。
# 写在下面，保存后再运行。


def first_n(items: list[str], n: int) -> list[str]:
    return items[:n]
    # return items[0:n]


def print_ranked(items: list[str]) -> None:
    for index, e in enumerate(items, start=1):
        print(f"{index}. {e}")


print(f"{first_n(names, 2)}")
print_ranked(names)
