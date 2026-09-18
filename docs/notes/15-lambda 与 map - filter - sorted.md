# 第 15 课：lambda 与 map / filter / sorted

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：lambda 小函数、sorted(key=) 必会组合、map/filter 与推导式怎么选。

---

两件事：**lambda**（临时小函数）和**把函数当参数传** （尤其 `sorted(key=)`）。map/filter 知道即可，日常更常写推导式。

## lambda：当场写、不取名

```python
add = lambda a, b: a + b
print(add(2, 3))  # 5

double = lambda x: x * 2
```

没有名字、没有 return 关键字，只能写一个表达式。复杂逻辑请用 `def`。

## sorted(key=)：按「算出来的依据」排

```python
scores = {"小明": 90, "hulei": 75, "小红": 40, "阿": 100}

by_score = sorted(scores.items(), key=lambda item: item[1], reverse=True)
by_len = sorted(scores.keys(), key=lambda name: len(name))
```

> **原理**
>
> `key` 接收一个函数：对每个元素算出「排序用的值」。 不改原数据；`reverse=True` 从大到小。 这是 lambda 最值得学的日常组合。

## map / filter：函数式写法

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x * x, nums))
# 更推荐： [x * x for x in nums]

ages = [15, 18, 20, 12]
adults = list(filter(lambda a: a >= 18, ages))
# 更推荐： [a for a in ages if a >= 18]
```

> **踩坑**
>
> `map`/`filter` 返回的是惰性迭代器，要看见列表需 `list(...)`。 Python 里优先推导式；读别人代码时能认 map/filter 即可。

## 函数是一等公民

能传进 `sorted`、`map`，也能自己写「接收函数」的高阶函数。 第 23 课装饰器会把这件事推到极致。

## 建议你自己练的几件事

2. 按分数、按名字长度各排一次成绩 dict。
4. 同一映射分别用 map 和推导式写，确认结果相同。
6. 对对象列表（下一课）用 `key=lambda s: s.score` 排序。

## 收束

lambda 适合短 key；sorted(key=) 必会；map/filter 认得出、推导式写得出。 下一课 class：把数据和行为绑在一起。

---

上一课：[第 14 课：列表推导式](14-列表推导式.md)　|　下一课：[第 16 课：类与对象](16-类与对象.md)
