# ============================================================
# 第 22 课（知识讲解）：OOP 进阶 —— 继承、多态
# 运行方式：python 22_oop_inheritance/22_oop_inheritance.py
# 配套练习：22_oop_inheritance_exercise.py（自检）
# ============================================================

# 第 16 课讲了最基础的类。这一课往上走一层：继承、重写、多态。
# 你是 Java 开发者，很多词的既视感会很强（extends / @Override / 父类引用），
# 但 Python 有几个和你习惯不一样的地方，我会在每处标【Java 对照】。
print("========== 第22课 OOP进阶：继承 / 多态 ==========\n")


# ---------- 1. 为什么继承 ----------
# 继承解决两件事：
#   1) 复用：子类自动拥有父类的属性和方法，不用重写。
#   2) 分层：把共有逻辑放父类，把不同之处放子类。
# 【Java 对照】class Dog extends Animal —— Python 用 class Dog(Animal):。
print("【1】继承：子类自动继承父类的方法")
class Animal:
    def __init__(self, name: str):
        self.name = name

    def intro(self) -> str:
        return f"我是 {self.name}"

class Dog(Animal):
    pass   # 什么都不写：Doge 直接继承 Animal 的一切

dog = Dog("旺财")
print(dog.intro())          # "我是 旺财" —— intro 来自父类
print(Animal is Dog.__mro__[1])   # True：Dog 的父类是 Animal，先放着后面看


# ---------- 2. super().__init__：子类构造里调用父类构造 ----------
# 子类有自己的 __init__，但往往也要把父类要的初始数据传上去。
# super() 就是从"子类"跳到"父类"要方法。
# 【Java 对照】Java 的 super(...) 必须是构造第一行；Python 也推荐放前面。
print("\n【2】super().__init__()：子类构造把参数交给父类构造")
class Animal2:                      # 和上面同名会覆盖，所以用新类名演示
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Cat(Animal2):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)   # 把 name、age 交给父类构造
        self.color = color            # 子类自己的新属性

c = Cat("咪咪", 2, "橘")
print(f"{c.name} {c.age}岁 {c.color}色")   # 咪咪 2岁 橘色


# ---------- 3. 方法重写 override ----------
# 子类跟父类写一样的方法名，就是重写。调的时候用子类版本。
# 【Java 对照】Java 里方法默认是"虚"的才可被重写；Python 里所有方法天生可重写，
# 也没有 final 禁继承/禁重写的关键字。
print("\n【3】方法重写：同名的子类方法盖过父类")
class Animal3:
    def sound(self) -> str:
        return "...（父类的通用声音）"

class Dog3(Animal3):
    def sound(self) -> str:
        return "汪汪！"     # 同名重写，盖掉父类的

class Cat3(Animal3):
    def sound(self) -> str:
        return "喵～"

print(Dog3().sound(), "|", Cat3().sound())   # 汪汪！ | 喵～


# ---------- 4. 多态 + 鸭子类型（重点，和你 Java 习惯差最多） ----------
# 多态=同一个方法名，对不同的对象给出不同的行为。
# 【Java 对照】Java：Animal a = new Dog();  a.sound();  —— 先有"父类类型"才能装子类。
# Python：不看声明类型，看对象"有没有这个方法"。这叫鸭子类型：
#   "走起来像鸭子、叫起来像鸭子，就当它是鸭子。"
print("\n【4】多态 + 鸭子类型")
def play_with(pet):            # 参数不写类型注解也没关系
    return pet.sound()          # 只要东西有 sound() 就行

print(play_with(Dog3()), "|", play_with(Cat3()))   # 汪汪！ | 喵～

# 更强的证明：一个跟 Animal 毫无关系的类，只要有 sound() 就能被 play_with 用。
class Robot:
    def sound(self) -> str:
        return "哔哔"

print("连 Robot 也能进来玩：", play_with(Robot()))   # 哔哔
print("是不是 Animal 的子类？", issubclass(Robot, Animal3))   # False —— 但照样能多态


# ---------- 5. isinstance / issubclass：判断"是谁" ----------
# isinstance(对象, 类)    对象是不是这个类（或其子类）的实例
# issubclass(子类, 父类)  子类是不是父类的后代
# 【Java 对照】instanceof / 继承判定。
print("\n【5】isinstance / issubclass")
print(isinstance(Dog3(), Animal3), isinstance(Dog3(), Dog3))      # True True
print(isinstance(Animal3(), Dog3))                                # False（父不是子）
print(issubclass(Dog3, Animal3), issubclass(Cat3, Animal3))       # True True
print(issubclass(Dog3, object))                                   # True（一切皆 object）


# ---------- 6. 魔术方法推进：对象能打印、能比大小、能排序 ----------
# __str__ / __repr__：打印对象显示成什么。
# 【Java 对照】toString()。返回值应该是"对人可读"的字符串。
# __lt__：定义"小于"，有了它对象就能放进 sorted() 排序，类似 Java 的 Comparable。
print("\n【6】魔术方法：__str__ / __lt__ 让对象可打印、可排序")
class Student:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):                    # print(obj) 和列表里显示对象时用
        return f"{self.name}:{self.score}"

    def __lt__(self, other) -> bool:       # "比大小"的规则
        return self.score < other.score    # 小于=分数更低（这样能按分数升序排）

students = [Student("小明", 90), Student("小红", 40), Student("hulei", 75)]
print("原始：", students)
print("按分数升序：", sorted(students))    # sorted 内部就靠 __lt__
print("按分数降序：", sorted(students, reverse=True))


# ---------- 7. property：属性背后的 getter/setter ----------
# @property 把"方法"伪装成"属性"来读写，能加校验。
# 【Java 对照】Java 的 getXxx()/setXxx()。Python 用 @property 更优雅。
print("\n【7】@property + setter：像字段一样读写，但能校验")
class Bank:
    def __init__(self, balance: int = 0):
        self._balance = balance            # 真数据存 _balance

    @property
    def balance(self) -> int:              # 读：bank.balance
        return self._balance

    @balance.setter
    def balance(self, amount: int):        # 写：bank.balance = xxx，带校验
        if amount < 0:
            raise ValueError("余额不能为负")
        self._balance = amount

acc = Bank(100)
print("读：", acc.balance)                 # 100，读起来像字段
acc.balance = 200                          # 写起来也像字段
print("改后：", acc.balance)
try:
    acc.balance = -5                       # 触发 setter 校验
except ValueError as e:
    print("触发校验：", e)


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("子类能拿父类的：  class Dog(Animal):")
print("子类构造交接：    super().__init__(父类要的参数)")
print("同名即重写：      方法名一样，子类版本生效")
print("多态=鸭子类型：   有方法就行，不看类型声明")
print("判断是谁：        isinstance(对象,类)  issubclass(子,父)")
print("对象排序：        实现 __lt__ 就能 sorted()")
print("属性带校验：      @property / @balance.setter")