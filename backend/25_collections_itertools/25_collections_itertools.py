# ============================================================
# 第 25 课（知识讲解）：常用数据结构 + itertools
# 运行方式：python 25_collections_itertools/25_collections_itertools.py
# 配套练习：25_collections_itertools_exercise.py（自检，全是新场景）
# ============================================================
from collections import defaultdict, Counter, namedtuple
import itertools

# 这些是"标准库写好了的高频算法"，不用自己造轮子。
# 【Java 对照】
#   defaultdict    ≈ map.computeIfAbsent / getOrDefault
#   Counter        ≈ 流式 groupingBy+counting
#   namedtuple     ≈ 更轻的只读 record/POJO
#   itertools      ≈ 多数靠 Guava 或自己写
print("========== 第25课 collections + itertools ==========\n")


# ---------- 1. 三种推导式 ----------
print("【1】list / dict / set 推导式")
lst = [i * 2 for i in range(5)]                     # 列表：新列表
dct = {c: i for i, c in enumerate("abc")}           # 字典：键→值
st  = {x % 3 for x in range(10)}                    # 集合：去重
print("  列表", lst)          # [0, 2, 4, 6, 8]
print("  字典", dct)          # {'a': 0, 'b': 1, 'c': 2}
print("  集合", st)           # {0, 1, 2}


# ---------- 2. defaultdict：给不存在的键一个默认值 ----------
print("\n【2】defaultdict：分组神器")
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
bucket = defaultdict(list)                    # 默认值 = 一个空 list
for w in words:
    bucket[w].append(w)                       # 键不存在时自动建空 list
print("  bucket[apple] =", bucket["apple"])   # ['apple', 'apple', 'apple']
# 用法核心：不存在的键不再 KeyError，而是"按默认工厂现造一个"。
# 常用工厂：list / set / int(→0) / lambda:默认值


# ---------- 3. Counter：一键计数 ----------
print("\n【3】Counter：给可迭代对象数个数")
cnt = Counter("abracadabra")
print(cnt)
print("  ", dict(cnt))                        # {'a':5,'b':2,'r':2,'c':1,'d':1}
print("  出现最多的 2 个:", cnt.most_common(2))  # [('a',5),('b',2)]


# ---------- 4. namedtuple：给元组里的位置"起名字" ----------
print("\n【4】namedtuple：带字段名的轻量元组")
Point = namedtuple("Point", ["x", "y"])
p = Point(x=3, y=4)
print("  p =", p)                              # Point(x=3, y=4)
print("  p.x 和 p[0] 都能拿到:", p.x, p[0])      # 3 3
x, y = p                                       # 还能像元组一样解包
print("  解包:", x, y)


# ---------- 5. itertools 基础：chain / islice / count / cycle ----------
print("\n【5】itertools 迭代器工具")
# chain：把多个可迭代对象首尾相连
print("  chain:", list(itertools.chain([1, 2], [3], [4, 5])))     # [1,2,3,4,5]
# count：无限递增；islice：只取前面几个（不把整个无限序列存出来）
print("  count取前5:", list(itertools.islice(itertools.count(10), 5)))  # [10,11,12,13,14]
# cycle：无限循环
print("  cycle取前6:", list(itertools.islice(itertools.cycle("AB"), 6)))  # ['A','B','A','B','A','B']


# ---------- 6. groupby：连续分组（注意：只认连续相邻的） ----------
print("\n【6】itertools.groupby：把相邻相同元素归一组")
data = ["a", "a", "b", "b", "b", "a"]          # 注意有两个 'a'，不连在一起
for key, group in itertools.groupby(data):
    print(f"    键 {key!r} → {list(group)}")    # 两个 'a' 分成了两批
# 想按某字段分组，先按该字段 sort 再 groupby(data, key=...) 即可


# ---------- 7. 组合枚举：product / permutations / combinations ----------
print("\n【7】排列组合枚举")
# product：笛卡尔积（允许重复）
print("  product AB×2:", ["".join(t) for t in itertools.product("AB", repeat=2)])
# permutations：排列（有序、不重复）
print("  permutations ABC取2:", list(itertools.permutations("ABC", 2)))
# combinations：组合（无序）
print("  combinations ABC取2:", list(itertools.combinations("ABC", 2)))


# ---------- 8. accumulate：前缀累积 ----------
print("\n【8】itertools.accumulate：前缀和")
print("  ", list(itertools.accumulate([1, 2, 3, 4])))     # [1, 3, 6, 10]
print("  前缀乘积:", list(itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b)))


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("defaultdict(f)：缺键自动造默认值 分组神器")
print("Counter(可迭代)：计数 + most_common(n)")
print("namedtuple('名',字段)：带名字的元组，能解包")
print("chain/count/cycle/islice：迭代器串/无限/截取")
print("groupby(已按key排好序)：连续分组")
print("product/permutations/combinations：排列组合")
print("accumulate：前缀和/累积")