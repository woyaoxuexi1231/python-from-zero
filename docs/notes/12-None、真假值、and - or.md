# 第 12 课：None、真假值、and / or

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：is None 判断缺席、if 的假值列表、0 分不是没有、and/or 短路与默认值。

---

`get_score` 找不到人时返回 `None`。 这一课把「怎么判断没有」和「if 到底把什么当成真」说清楚—— 否则 0 分会被误判成「没这个人」。

## None：专门表示没有

```python
missing = None
print(type(missing))  # NoneType

def get_score(book: dict[str, int], name: str) -> int | None:
    if name in book:
        return book[name]
    return None
```

`None` 不是 0，也不是空字符串。接近其他语言里的 null。

## 判断没有：用 is None

```python
score = get_score(scores, "不存在")
if score is None:
    print("没有这个人")
elif score is not None:
    print(f"{score} 分")
```

> **原理**
>
> `is` 问「是不是同一个对象」；None 全局唯一，所以用 `is None`。 `==` 问值相等，对 None 碰巧也能用，但习惯写 `is`。

## if 会把很多东西当成假

在 if 里相当于 False 的常见值：

- `None`、`False`
- `0`、`0.0`
- `""`、`[]`、`{}`、`set()`

其他大多数为真：非空字符串、非空列表、非零数字……

```python
name = ""
if not name:
    print("名字是空的")
```

> **踩坑**
>
> hulei 若是 0 分：`if score:` 会当成假，误判「没有」。 **判断有没有值 → `is None`；判断空不空 → `if not name`； 判断分数高低 → 写 `>= 60`，别靠真假值。**

## and / or：短路

```python
# and：左边假就不再算右边
# or ：左边真就不再算右边
name = input("名字：").strip() or "匿名"
print(name)
```

`or` 常用来给默认值：左边有内容就用左边，否则用右边。 `and` 常用来「前置条件满足才做后面」。

> **原理**
>
> Python 的 and/or 不一定返回 True/False，而是返回**决定结果的那个操作数**。 所以 `"" or "匿名"` 得到 `"匿名"`，不是 `True`。

## 建议你自己练的几件事

2. 给成绩本某人设 0 分，分别用 `if score` 和 `is not None` 对比。
4. 用 `bool()` 打印 None、0、""、[]、"hi" 的真假。
6. 用 `x or default` 给空输入填默认名。

## 收束

None 表示缺席；真假值是 if 的隐式规则；and/or 会短路且返回操作数。 下一课函数进阶：默认参数、*args、以及「默认值不要用空列表」。

---

上一课：[第 11 课：切片、range、enumerate](11-切片、range、enumerate.md)　|　下一课：[第 13 课：函数进阶](13-函数进阶.md)
