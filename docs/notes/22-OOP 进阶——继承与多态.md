# 第 22 课：OOP 进阶——继承与多态

`Python 从零` · 更新于 2026-08-24 · 标签：Python、入门

**摘要**：继承、super()、方法重写、鸭子类型、isinstance/issubclass。

---

第 16 课会写基础类。这一课往上走：继承复用、super 构造链、方法重写、 多态与鸭子类型，以及 `isinstance` / 常用魔术方法。

## 为什么继承

- 复用：子类自动拥有父类属性和方法
- 分层：共有逻辑放父类，差异放子类

```python
class Animal:
    def __init__(self, name: str):
        self.name = name
    def intro(self) -> str:
        return f"我是 {self.name}"

class Dog(Animal):
    pass

print(Dog("旺财").intro())
```

## super().__init__

```python
class Cat(Animal):
    def __init__(self, name: str, color: str):
        super().__init__(name)
        self.color = color
```

子类有自己的 __init__ 时，通常先把父类需要的数据交给 `super()`。

## 方法重写

```python
class Dog(Animal):
    def sound(self) -> str:
        return "汪汪！"

class Cat(Animal):
    def sound(self) -> str:
        return "喵～"
```

同名方法，调到子类版本。Python 里方法天生可重写。

## 多态 + 鸭子类型

```python
def play_with(pet):
    return pet.sound()   # 不看声明类型，看有没有 sound()

class Robot:
    def sound(self) -> str:
        return "哔哔"

print(play_with(Dog()), play_with(Robot()))
```

> **原理**
>
> 「走起来像鸭子、叫起来像鸭子，就当它是鸭子。」 不要求必须继承同一父类——这和许多静态类型语言的习惯不同。

## isinstance / issubclass

```python
print(isinstance(Dog(), Animal))
print(issubclass(Dog, Animal))
```

> **踩坑**
>
> 子类写了 __init__ 却忘了 super，父类属性可能根本没初始化。 配课有知识文件 + 练习文件，先跑通讲解再做自检。

## 建议你自己练的几件事

2. Animal / Dog / Cat：继承、重写 sound、play_with 多态。
4. 给子类加独有属性，构造里正确 super。
6. 做一个无继承的「有 sound」的类，验证鸭子类型。

## 收束

继承分层，重写定差异，鸭子类型看行为不看血统。 下一课装饰器：不改函数体，给函数「加料」。

---

上一课：[第 21 课：复习通关（18～20）](21-复习通关（18～20）.md)　|　下一课：[第 23 课：装饰器](23-装饰器.md)
