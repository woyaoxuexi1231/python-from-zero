# ============================================================
# 第 15 课：lambda 与 map / filter / sorted
# 运行方式：python 15_lambda_map_filter.py
# ============================================================

# 第 13 课学了 def 写函数，第 14 课学了推导式。
# 这一课学两件事：
#   1. lambda：临时用的小函数，不用 def 起名。
#   2. 把函数当参数传给 map / filter / sorted。
#
# 你上节课说推导式像 Java 的 stream。下面的对照会反复出现：
#   Java: xs.stream().map(f).filter(p).toList()
#   Py  : [f(x) for x in xs if p(x)]          # 推导式（最常用）
#   Py  : list(map(f, xs))  /  list(filter(p, xs))   # 函数式写法
#
# 结论先放这：Python 里优先写推导式，map/filter 知道就行。
# 但 lambda + sorted(key=) 是日常真常用的组合，必须会。


# ---------- 1. lambda 是什么 ----------
# lambda 参数: 表达式
# 没有函数名、没有 return（表达式的值就是返回值）、只能写一行。

add = lambda a, b: a + b
print(add(2, 3))  # 5

# 等价于：
# def add(a, b):
#     return a + b
# lambda 就是「当场写、不取名」的简版。

double = lambda x: x * 2
print(double(10))  # 20
print("-----")

# ---------- 2. 把函数当参数传：sorted(key=) ----------
# sorted(可迭代, key=函数) 会用 key 算出来的「排序依据」来排，不改原数据。

scores: dict[str, int] = {
    "小明": 90,
    "hulei": 75,
    "小红": 40,
    "阿": 100,
}

# 按分数从高到低排名字
by_score = sorted(scores.items(), key=lambda item: item[1], reverse=True)
print(by_score)  # [('阿', 100), ('小明', 90), ('hulei', 75), ('小红', 40)]

# 按名字长度排（短的在前）
by_len = sorted(scores.keys(), key=lambda name: len(name))
print(by_len)  # ['阿', '小明', '小红', 'hulei']
print("-----")

# 对照 Java 思路：key=lambda 就像 Comparator 里 compareTo 算的那一个数。


# ---------- 3. map：对每个元素套一个函数 ----------
# map(函数, 可迭代) 返回一个「还没算完」的迭代器，用 list() 收成列表。

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
print(squared)  # [1, 4, 9, 16]

# 等价推导式（更 Pythonic，推荐）：
squared2 = [x * x for x in nums]
print(squared2)
print("-----")

# ---------- 4. filter：只留符合条件的 ----------
# filter(判断函数, 可迭代) 留「返回真」的元素。

ages = [15, 18, 20, 12, 33]
adults = list(filter(lambda a: a >= 18, ages))
print(adults)  # [18, 20, 33]

# 等价推导式（更推荐）：
adults2 = [a for a in ages if a >= 18]
print(adults2)
print("-----")


# ---------- 5. 什么时候用哪个 ----------
# 简单映射 / 过滤          → 推导式 [f(x) for x in xs] / [x for x in xs if p(x)]
# 需要按某个规则排序        → sorted(xs, key=lambda ...)
# map / filter 适合：已经有一个现成函数名要传进去时用，临时小逻辑还是推导式清楚。
#
# 一句话：lambda 是工具，sorted(key=) 是主场，map/filter 是备胎。


# ---------- 练习 ----------
# 1. 写函数 top_students(scores: dict[str, int], n: int) -> list[str]
#    返回分数最高的前 n 个名字（从高到低）。用 sorted(key=...) + slice。
#    top_students({"A": 90, "B": 60, "C": 80}, 2) 应得到 ["A", "C"]
#
# 2. 写函数 names_start_with(items: list[str], letter: str) -> list[str]
#    返回所有以 letter 开头的名字（忽略大小写）。用推导式。
#    names_start_with(["Bob", "alice", "Ben"], "b") 应得到 ["Bob", "Ben"]
#
# 写在下面，保存后再运行。

def top_students(scores: dict[str, int], n: int) -> list[str]:
    ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
    return [name for name, _ in ranked[:n]]


def names_start_with(items: list[str], letter: str) -> list[str]:
    return [name for name in items if name.lower().startswith(letter.lower())]


print(top_students({"A": 90, "B": 60, "C": 80}, 2))
print(names_start_with(["Bob", "alice", "Ben"], "b"))


# ---------- 练习 ----------
# 1. 写函数 top_students(scores: dict[str, int], n: int) -> list[str]
#    返回分数最高的前 n 个名字（从高到低）。用 sorted(key=...) + slice。
#    top_students({"A": 90, "B": 60, "C": 80}, 2) 应得到 ["A", "C"]
#
# 2. 写函数 names_start_with(items: list[str], letter: str) -> list[str]
#    返回所有以 letter 开头的名字（忽略大小写）。用推导式。
#    names_start_with(["Bob", "alice", "Ben"], "b") 应得到 ["Bob", "Ben"]
#
# 写在下面，保存后再运行。


# 返回分数最高的前 n 个名字（从高到低）
def top_students2(scores_def: dict[str, int], n_def: int) -> list[str]:
    # 首先第一件事情就是排序
    scores_sorted = sorted(scores_def.items(), key=lambda item: item[1], reverse=True)
    # 现在得到了排好序的列表了，只需要按规则返回前n个就行了，这就用到之前的
    names = list(map(lambda k: k[0], scores_sorted))
    return names[0:n_def]


print(top_students2({"A": 90, "B": 60, "C": 80}, 2))


# 2. 写函数 names_start_with(items: list[str], letter: str) -> list[str]
#    返回所有以 letter 开头的名字（忽略大小写）。用推导式。
#    names_start_with(["Bob", "alice", "Ben"], "b") 应得到 ["Bob", "Ben"]

def names_start_with2(items: list[str], letter: str) -> list[str]:
    return [name for name in items if name.startswith(letter.lower())]


print(names_start_with(["Bob", "alice", "Ben"], "b"))


# 题 1（sorted + key 基础） 写 sort_by_length(words: list[str]) -> list[str]，按单词长度从短到长排序，长度一样保持原顺序。
#
# sort_by_length(["pear", "a", "banana", "fig"]) → ["a", "fig", "pear", "banana"]


def sort_by_length(words: list[str]) -> list[str]:
    # def sorted(
    #     iterable: Iterable[SupportsRichComparisonT], /, *, key: None = None, reverse: bool = False
    # ) -> list[SupportsRichComparisonT]: ...
    # sorted(1.数组 2.排序规则 3.是否反转)
    # 我写道这里真的感觉python和java的差别还是挺大的，感觉真的python就是为了数据处理而来的，目前写的东西大部分都是在数据处理中。，而且语法也偏向如何更易于处理数据的方向进行
    return sorted(words, key=lambda word: len(word))


# 题 2（sorted 多条件） 写 sort_students(students: list[tuple[str, int]]) -> list[tuple[str, int]]，先按分数从高到低，分数相同的按名字字母升序。
#
# sort_students([("B",80),("A",90),("C",90)]) → [("A",90),("C",90),("B",80)]
# 提示：key=lambda s: (-s[1], s[0])
def sort_students(students: list[tuple[str, int]]) -> list[tuple[str, int]]:
    # 先按照分数排序, 直接使用两个排序不行，第二个排序又会把第一个排序打乱。所以要融合成一个才行
    # students_sorted = sorted(students, key=lambda item: item[1], reverse=True)
    # students_sorted2 = sorted(students_sorted, key=lambda item: item[0], reverse=False)
    # return students_sorted2

    # 我这里偷看了提示，我自己没想出来，我还在想 key 是不是可以写成 java 的 lambda 表达式那样，我写个 if elseif表达式来弄
    return sorted(students, key=lambda item: (-item[1], item[0]), reverse=False)


print(sort_students([("B", 80), ("A", 90), ("C", 90)]))


# 题 3（map 顺序，专治你刚才的坑） 写 to_upper(words: list[str]) -> list[str]，把每个单词变成大写。用 map 写（故意练一遍正确顺序）。
#
# to_upper(["hi","ok"]) → ["HI","OK"]

def to_upper(words_def: list[str]) -> list[str]:
    return list(map(lambda word_def: word_def.upper(), words_def))


print(to_upper(["hi", "ok"]))


# 题 4（filter + 推导式对照） 写 evens(nums: list[int]) -> list[int]，返回所有偶数。分别用推导式和 filter 写两个版本，体会哪个更顺。
#
# evens([1,2,3,4,5,6]) → [2,4,6]

def evens(nums_def: list[int]) -> list[int]:
    # [f(x) for x in xs p(x)]
    return [num for num in nums_def if num % 2 == 0]
    # return list(filter(lambda x: x % 2 == 0, nums_def))


print(evens([1, 2, 3, 4, 5, 6]))

# 题 5（综合，忽略大小写，你第二题的升级） 写 group_by_first_letter(names: list[str]) -> dict[str, list[str]]，把名字按**首字母（忽略大小写）**分组。
#
# group_by_first_letter(["Bob","alice","Ben","amy"]) → {"b":["Bob","Ben"], "a":["alice","amy"]}
# 提示：用 defaultdict(list) 或先建空字典再 setdefault
def group_by_first_letter(names: list[str]) -> dict[str, list[str]]:
    result: dict[str, list[str]] ={}

    # ① 原始
    # for name in names:
    #     key = name[:1].lower()
    #     if key not in result:
    #         result[key] = []
    #     result[key].append(name)

    # ② 使用 setdefault
    for name in names:
        key = name[:1].lower()
        result.setdefault(key, []).append(name)


    # result = defaultdict(list)          # 访问不存在的 key 时自动给个空 list
    # for name in names:
    #     key = name[0:1].lower()
    #     result[key].append(name)        # 不用先判断,直接 append

    return result


print(group_by_first_letter(["Bob", "alice", "Ben", "amy"]))


