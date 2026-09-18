# 第 30 课：enum 枚举

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：Enum/IntEnum/StrEnum、name/value、反查与 auto()；用枚举替代魔法字符串，接近 Java enum。

---

状态、等级、颜色常写成 `"pending"`、`"done"` 字符串——拼错要运行时才炸，IDE 也不补全。 第 27 课 `Literal` 能在类型上约束「只能是几个值」；这一课用 **enum** 在运行时建真正的枚举类，接近 Java 的 `enum`。

## 这一课解决什么问题

- 有限固定取值 → 用 `class X(Enum)`，别散落魔法字符串
- 要成员名 / 绑定值 → `.name` / `.value`
- 字符串来反查 → `Status("pending")`；按名 → `Status["PENDING"]`
- 要当 int / str 用 → `IntEnum` / `StrEnum`

## 基本 Enum

```python
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"

Status.PENDING.name    # "PENDING"
Status.PENDING.value   # "pending"
Status.PENDING is Status.PENDING   # True（单例）
```

> **踩坑**
>
> `Status.PENDING == "pending"` 是 **False**——成员不是 str。 要比字符串用 `.value`；成员之间用 `==` 或 `is`。

## 反查与遍历

```python
Status["PENDING"]      # 按成员名
Status("pending")      # 按 value（非法会 ValueError）

[m.name for m in Status]    # 所有成员名
```

## auto / IntEnum / StrEnum

```python
from enum import auto, IntEnum, StrEnum

class Priority(Enum):
    LOW = auto()      # 1, 2, 3 … 自动递增

class HttpCode(IntEnum):
    OK = 200
HttpCode.OK == 200    # True，可当 int

class Color(StrEnum):
    RED = "red"
Color.RED == "red"    # True，可当 str 拼接
```

> **和 Literal 的区别**
>
> `Literal["a","b"]`：类型检查器用，运行时仍是普通 str。 `Enum`：运行时真类，能迭代、反查、挂方法。API 边界常 enum 定义值，参数标注 `Status` 或 `Literal` 视团队习惯。

## 配课怎么练

2. 先跑 `30_enum.py`，对照输出。
4. 再打开 `30_enum_exercise.py`，6 题：订单状态、反查、IntEnum、StrEnum、auto。
6. 题 1 先定义 `OrderStatus` 成员，后面几题复用。

## 收束

enum 的核心：把「就这几个取值」收成类，补全、防拼错、可读性都比裸字符串强。 下一课可以继续 functools 进阶、logging，或做一个 18~30 的小复习——你哪块虚就补哪块。

---

上一课：[第 29 课：itertools 复习强化](29-itertools 复习强化.md)　|　下一课：[第 31 课：datetime 日期与时间](31-datetime 日期与时间.md)
