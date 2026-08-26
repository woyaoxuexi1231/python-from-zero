# ============================================================
# 第 4 课：列表、循环
# 运行方式：python 04_lists_and_loops.py
# ============================================================

# ---------- 1. 列表：一排有顺序的东西 ----------
# 用方括号 []，中间用逗号分开。
# 类型标注 list[int] 表示「这是一个装满整数的列表」。

ages: list[int] = [15, 18, 20, 12]
names: list[str] = ["小明", "hulei", "小红"]

print(ages)
print(names)
print("-----")

# ---------- 2. 编号从 0 开始 ----------
# 第一个是 [0]，第二个是 [1]，依此类推。
# 这叫索引。几乎所有编程语言都从 0 起算。

print(names[0])  # 小明
print(names[1])  # hulei
print(len(names))  # 3   len() 是列表里有几个元素
print("-----")

# ---------- 3. for：把列表里每一项拿出来做一次 ----------
# for 后面的 name 是你起的临时名字，每一轮会变成下一项。
# 下面这段会打印 3 行。

for name in names:
    print(f"你好，{name}")
print("-----")

# ---------- 4. 循环里可以做判断 ----------

for age in ages:
    if age >= 18:
        print(f"{age} 岁，成年")
    else:
        print(f"{age} 岁，未成年")
print("-----")


# ---------- 5. 循环里累计：先准备一个盒子，再往里加 ----------
# 这是非常常见的写法。先把 result 设成 0，每看到一个数字就加上去。

def sum_demo(numbers: list[int]) -> int:
    result = 0
    for n in numbers:
        result = result + n
    return result


print(sum_demo([1, 2, 3, 4]))  # 10
print("-----")

# ---------- 6. append：往列表末尾加一项 ----------

nums: list[int] = [1, 2]
nums.append(3)
print(nums)  # [1, 2, 3]
print("-----")


# ---------- 练习 ----------
# 1. 写函数 sum_numbers(numbers: list[int]) -> int
#    返回列表里所有数字的和。
#    sum_numbers([1, 2, 3, 4]) 应该是 10。
#
# 2. 写函数 count_positive(numbers: list[int]) -> int
#    统计列表里有几个大于 0 的数字。
#    count_positive([-2, 0, 3, 5]) 应该是 2。
#
# 两个函数都写好后，用 print 把上面两个例子的结果打出来。
# 写在下面，保存后再运行。
def sum_number(ns: list[int]) -> int:
    result = 0
    for n in ns:
        result = result + n
    return result


myints: list[int] = [1, 2, 3, 4]
myints2 = [1, 2, 3, 4, 5]

print(sum_number(myints))
print(sum_number(myints2))


def count_positive(ns: list[int]) -> int:
    result = 0
    for n in ns:
        if n > 0:
            result = result + 1
    return result

print(count_positive(myints))
