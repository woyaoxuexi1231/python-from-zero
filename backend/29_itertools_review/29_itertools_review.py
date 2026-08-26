# ============================================================
# 第 29 课（复习强化）：itertools 模块 —— 迭代、分组、组合、累积
# 运行方式：python 29_itertools_review/29_itertools_review.py
# 配套练习：29_itertools_review_exercise.py（自检，全是新场景）
# ============================================================
import itertools

# 第 25 课 collections 和 itertools 挤在一课，itertools 容易「看过命名、写题卡壳」。
# 这一课只复习 itertools 八个最常用的：chain / islice / count / cycle /
# groupby / product / permutations / combinations / accumulate。
# 目标：看见「串起来、取前 N、分组、排列组合、前缀和」时，手能伸过去。
print("========== 第29课 itertools 复习强化 ==========\n")


# ---------- 1. chain：把多个可迭代对象首尾相接 ----------
print("【1】chain：串起来，不先合并成一个大 list")
rows_a = [1, 2]
rows_b = [3]
rows_c = [4, 5]
print("  chain:", list(itertools.chain(rows_a, rows_b, rows_c)))

# 嵌套 list 展平：chain.from_iterable（比手写双层循环短）
nested = [[1, 2], [3], [4, 5]]
print("  from_iterable:", list(itertools.chain.from_iterable(nested)))
print("  小抄：chain(a,b,c) 平铺；chain.from_iterable(二维) 展平")


# ---------- 2. islice + count / cycle：无限序列里只取一段 ----------
print("\n【2】islice：惰性截取，别把无限序列 list 出来")
# count(start)：0,1,2,… 无限；islice 只拿前 n 个
print("  count 前5:", list(itertools.islice(itertools.count(10), 5)))

# cycle：A,B,A,B,… 无限循环；配合 islice 取前几个
print("  cycle 前6:", list(itertools.islice(itertools.cycle("AB"), 6)))

# 大文件/生成器常用：只 peek 前 N 条
def read_lines(path):
    """假装逐行读文件（惰性）"""
    for i, line in enumerate([f"L{i}" for i in range(100)]):
        yield line

print("  大文件 peek3:", list(itertools.islice(read_lines("x"), 3)))
print("  小抄：无限或很大 → islice(it, n)；别 list(无限)")


# ---------- 3. groupby：只认「相邻相同」—— 先排序！ ----------
print("\n【3】groupby：连续相同 key 归一组（不是 SQL 的 GROUP BY）")
messy = ["u1", "u2", "u1", "u1", "u2"]   # 相同 user 不挨着 → 会拆成多段
for key, group in itertools.groupby(messy):
    print(f"    未排序 {key!r} → {list(group)}")

# 正确：先按分组键 sort，再 groupby
records = [("Bob", "A"), ("Amy", "B"), ("Anna", "A"), ("Cara", "B")]
records.sort(key=lambda r: r[1])          # 按班级排在一起
print("  按班分组:")
for cls, group in itertools.groupby(records, key=lambda r: r[1]):
    names = [name for name, _ in group]
    print(f"    班 {cls}: {names}")
print("  小抄：groupby 前必须 sort(key=…)；只合并相邻相等")


# ---------- 4. product / permutations / combinations ----------
print("\n【4】排列组合：三个词别混")
# product：笛卡尔积，可 repeat；有序、可重复
print("  product AB×2:", ["".join(t) for t in itertools.product("AB", repeat=2)])

# permutations：排列，顺序算不同，不重复选
print("  permutations ABC取2:", list(itertools.permutations("ABC", 2)))

# combinations：组合，顺序不算，不重复选
print("  combinations ABC取2:", list(itertools.combinations("ABC", 2)))
print("  小抄：product 笛卡尔；permutations 排列；combinations 组合")


# ---------- 5. accumulate：前缀累积 ----------
print("\n【5】accumulate：前缀和 / 前缀积 / 自定义累积")
print("  前缀和:", list(itertools.accumulate([1, 2, 3, 4])))
print("  前缀积:", list(itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b)))

scores = [70, 85, 90, 60]
print("  截至每场的最高分:", list(itertools.accumulate(scores, max)))
print("  小抄：accumulate(seq) 默认求和；第二参数可换 max/乘积等")


# ---------- 6. 易错点 ----------
print("\n【6】易错点速记")
print("  ① groupby 不排序 → 同名 key 被拆成多段（和 SQL GROUP BY 不一样）")
print("  ② list(itertools.count()) 会卡死 —— 无限序列必须 islice")
print("  ③ groupby 的 group 迭代器只能扫一次，list(group) 后就被消费了")
print("  ④ combinations/permutations 的 r 省略时等于 len(seq)")
print("  ⑤ product(*iterables) 与 product(iterable, repeat=k) 两种写法别混")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("chain / from_iterable：串起来 / 展平二维")
print("islice + count/cycle：无限序列取前 N")
print("sort + groupby(key)：按字段分组（相邻）")
print("product / permutations / combinations：笛卡尔 / 排列 / 组合")
print("accumulate：前缀和、前缀 max、自定义累积")
