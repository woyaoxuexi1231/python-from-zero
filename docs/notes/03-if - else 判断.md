# 第 3 课：if / else 判断

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：比较运算符、缩进分支、elif 命中即停、在函数里 return 判断结果、与 input 联用。

---

程序不能永远走直线。真实场景里，要根据条件走不同分支： 成年还是未成年、分数够不够及格、输入合不合法。 这一课的核心就是 `if / elif / else`，以及比较运算符产出的 `True` / `False`。

## 比较：问一个「是或否」的问题

一个等号 `=` 是赋值；两个等号 `==` 是比较。 比较的结果永远是布尔值。

```python
print(3 > 1)      # True
print(18 >= 18)   # True
print(3 == 5)     # False
print(3 != 5)     # True（不等于）
```

> **踩坑**
>
> 写条件时把 `==` 写成 `=`，在 Python 里通常直接 `SyntaxError`（if 后面不能赋值）。养成「条件里用双等号」的肌肉记忆。

## if / else：二选一

`if` 后面跟条件；为 `True` 时执行缩进块，否则走 `else`。 Python 用缩进表示归属——少空、多空都会报错，这是语法的一部分，不是风格偏好。

```python
age = 20
if age >= 18:
    print("成年")
else:
    print("未成年")
```

> **原理**
>
> 缩进块是「只在这个条件下执行」的一组语句。 块外的代码无论条件真假都会继续跑——判断只影响分支，不截断整个程序。

## elif：多个分支，命中即停

`elif` 是 else if 的缩写：上面都不对，再试这个。 从上往下检查，第一个为真的分支执行后，后面全部跳过。

```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```

顺序很重要：若先写 `>= 60` 再写 `>= 90`， 95 分会先被「及格」截住，永远到不了「优秀」。

## 在函数里判断并 return

把判断封进函数，调用方只关心结果。返回布尔或字符串都常见。

```python
def is_adult(age: int) -> bool:
    return age >= 18

def grade(score: int) -> str:
    if score >= 90:
        return "优秀"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
```

> **原理**
>
> `return age >= 18` 比写完整 if/else 返回 True/False 更短，语义相同。 条件表达式本身就是布尔值，可以直接交回去。

## 和 input 接起来

```python
user_age = int(input("请输入年龄："))
if is_adult(user_age):
    print(f"{user_age} 岁，已经成年")
else:
    print(f"{user_age} 岁，还未成年")
```

记住第 2 课：先 `input`，再 `int`，再判断。 转换失败会崩——第 8 课再用 `try/except` 接住。

## 建议你自己练的几件事

2. 写 `abs_value(n)`：非负返回 n，否则返回 `-n`。
4. 用 input 读一个整数，调用上面的函数，f-string 打印绝对值。
6. 故意把 elif 的分数阈值顺序写反，观察 95 分会落在哪一档。

## 收束

带走三件事：比较产出真假；缩进划定分支；elif 从上到下命中即停。 下一课进入列表与 `for`——一次处理「一排东西」。

---

上一课：[第 2 课：字符串、输入与类型转换](02-字符串、输入与类型转换.md)　|　下一课：[第 4 课：列表与循环](04-列表与循环.md)
