# 第 29 课：itertools 复习强化

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门、复习

**摘要**：chain/islice/groupby 先排序、product/permutations/combinations、accumulate 前缀累积；6 道新题。

---

第 25 课 `collections` 和 `itertools` 挤在一起， 第 28 课已经单独复习了 collections。第 29 课**只复习 itertools**， 把 `chain`、`islice`、`groupby`、排列组合、 `accumulate` 练到能随手用——不教新语法，专门补熟练度。

## 这一课解决什么问题

- 看见「多个 list 拼一起 / 二维展平」→ 想到 `chain` / `chain.from_iterable`
- 看见「无限或很大，只取前 N 个」→ 想到 `islice`
- 看见「按某字段分组」→ 想到 **先 sort** 再 `groupby`
- 看见「笛卡尔积 / 排列 / 组合」→ 想到 `product` / `permutations` / `combinations`
- 看见「前缀和、滚动最高」→ 想到 `accumulate`

## chain：串起来、展平

```python
import itertools

list(itertools.chain([1, 2], [3], [4, 5]))           # [1, 2, 3, 4, 5]
list(itertools.chain.from_iterable([[1, 2], [3]]))    # [1, 2, 3]
```

不必先 `a + b + c` 造大 list；`from_iterable` 专门压二维。

## islice + count / cycle：无限序列只取一段

```python
list(itertools.islice(itertools.count(10), 5))       # [10, 11, 12, 13, 14]
list(itertools.islice(itertools.cycle("AB"), 6))     # A,B,A,B,A,B
```

> **踩坑**
>
> 别 `list(itertools.count())`——会卡死。 无限或很大的迭代器，用 `islice(it, n)` 截取。

## groupby：先排序，再分组

```python
records = [("Bob", "A"), ("Amy", "B"), ("Anna", "A")]
records.sort(key=lambda r: r[1])   # 必须！按班排在一起

for cls, group in itertools.groupby(records, key=lambda r: r[1]):
    names = [name for name, _ in group]
    ...
```

> **原理**
>
> `groupby` 只合并**相邻**且 key 相同的元素——不是 SQL 的 GROUP BY。 相同 key 不挨着会被拆成多段；要先 `sort(key=…)`。

> **踩坑**
>
> `group` 是一次性迭代器，`list(group)` 之后就被消费了，不能反复用。

## product / permutations / combinations

| 工具 | 含义 | 例 ABC 取 2 |
| --- | --- | --- |
| `product` | 笛卡尔积，可 repeat，有序可重复 | `product("AB", repeat=2)` → AA,AB,BA,BB |
| `permutations` | 排列，顺序不同算不同 | (A,B),(A,C),(B,A)… |
| `combinations` | 组合，顺序不算 | (A,B),(A,C),(B,C) |

## accumulate：前缀累积

```python
list(itertools.accumulate([1, 2, 3, 4]))              # [1, 3, 6, 10] 前缀和
list(itertools.accumulate(scores, max))                 # 截至每场最高分
```

## 配课怎么练

2. 先跑 `29_itertools_review.py`，对照输出理解各工具。
4. 再打开 `29_itertools_review_exercise.py`，6 题全是新场景。
6. 题 3 卡壳：回来看 groupby「先 sort」；别抄第 25 课答案。
8. 全绿后，自己用 `product` 枚举两个列表的配对，用 `accumulate` 算累计销售额。

## 建议你自己练的几件事

2. 用 `chain.from_iterable` 展平 `[[1,2],[3]]`。
4. 用 `islice(count(100), 3)` 取 100,101,102。
6. 把学生列表按班 `sort + groupby`，对照 exercise 题 3。
8. 用 `combinations` 从 4 人里选 2 人组队。

## 收束

itertools 的核心是**惰性迭代**：不先把所有组合算进内存，按需一个个拿。 熟练的标志是读题选对工具，写题记得 groupby 前 sort、无限序列用 islice。 下一课可以继续 enum、 functools，或 pathlib 进阶——你哪块虚就补哪块。

---

上一课：[第 28 课：collections 复习强化](28-collections 复习强化.md)　|　下一课：[第 30 课：enum 枚举](30-enum 枚举.md)
