# ============================================================
# 第 16 课：类与对象（class）
# 运行方式：python 16_class_basics.py
# ============================================================


# 前面 13~15 课，你一直用 dict 装数据：
#   scores = {"小明": 90, "hulei": 75}
# 数据(名字+分数)和「操作数据的函数」(求平均、判断是否及格)是分开的。
#
# 类(class) 就是把「数据」和「操作数据的函数」绑在一起：
#   数据 → 属性(attribute)
#   函数 → 方法(method)
#
# 你写 Java，对 class 不陌生。重点看 Python 和 Java 的差异：
#   - 没有 public/private 强制（靠命名约定）
#   - __init__ 是构造器，self 是「这个对象自己」（类似 Java 的 this）
#   - 不用声明属性类型就能用（但我们可以标类型提示）


# ---------- 1. 第一个类：Student ----------
# class 类名:
#     def __init__(self, 参数...):   # 构造器，创建对象时自动调用
#         self.属性 = 参数             # self.xxx 才是「这个对象自己的数据」

class Student:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    # 方法：第一个参数必须是 self（代表对象自己）
    def is_pass(self) -> bool:
        return self.score >= 60

    def __str__(self) -> str:
        # print(对象) 时怎么显示；不写就只打印内存地址
        return f"{self.name}: {self.score} 分"

    def __repr__(self) -> str:
        # 列表/容器里打印元素时用 repr；没有它就退化成内存地址。
        # 直接复用 __str__ 即可，让 [s1, s2] 也显示得好看。
        return self.__str__()


# 创建对象（不用 new 关键字！）
s1 = Student("小明", 90)
s2 = Student("小红", 40)

print(s1.name, s1.score)  # 小明 90
print(s1.is_pass())  # True
print(s2.is_pass())  # False
print(s1)  # 小明: 90 分
print("-----")


# ---------- 2. 和 dict 对比 ----------
# dict 版：scores = {"name": "小明", "score": 90}
#   想判断是否及格，得另外写函数 is_pass(d)
# class 版：数据和方法在一起，s.is_pass() 顺着对象就能调
# 这就是 class 的价值：行为跟着数据走。


# ---------- 3. 类方法 / 属性也能算（property） ----------
# 有些「值」是算出来的，不是存着的。用 @property 可以当属性用。

class StudentV2:
    def __init__(self, name: str, score: int) -> None:
        self.name = name
        self.score = score

    @property
    def level(self) -> str:
        # 像属性一样访问：s.level，不用 s.level()
        if self.score >= 90:
            return "优秀"
        if self.score >= 60:
            return "及格"
        return "不及格"


s3 = StudentV2("阿", 95)
print(s3.level)  # 优秀（注意：没加括号，像属性不是方法）
print("-----")

# ---------- 4. 接上第 15 课：对象也能排序 ----------
# sorted(key=...) 对对象一样用，key 里取对象的属性。

students = [
    Student("小明", 90),
    Student("hulei", 75),
    Student("小红", 40),
]

by_score = sorted(students, key=lambda s: s.score, reverse=True)
for s in by_score:
    print(s)
# 小明: 90 分 / hulei: 75 分 / 小红: 40 分
print("-----")


# ---------- 5. 和 Java 的差异速记 ----------
# Java:  public class Student { private int score; public Student(...) }
# Py  :  class Student:        def __init__(self, score): self.score = score
#   - 没有 new：s = Student(...) 直接调类
#   - 没有 private 强制：想「私有」就命名前面加 _（约定，不是真封锁）
#   - self 必须显式写，且永远是方法第一个参数


# ---------- 练习 ----------
# 1. 写类 Book，属性 title(str)、price(int)，方法 is_expensive() -> bool
#    价格 >= 100 算贵。创建两本书打印一下。
#


class Book:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    @property
    def level(self) -> str:
        if self.price >= 90:
            return "贵的一批"
        else:
            return "不要钱"

    # 题目要求的方法：价格 >= 100 算贵，返回 bool
    def is_expensive(self) -> bool:
        return self.price >= 100


book1 = Book("活着", 20)
book2 = Book("钢铁是怎样炼成的吗", 1000)
print(book1.level)
print(book2.level)


# 2. 写 class 版本的成绩本：class GradeBook，__init__ 接收 list[Student]，
#    方法 average() -> float 返回平均分；passed() -> list[Student] 返回及格的。
#    把上面 students 传进去试一下。
#
# 写在下面，保存后再运行。
class GradeBook:

    def __init__(self, students_class: list[Student]) -> None:
        self.students = students_class

    def average(self) -> float:
        return sum([student.score for student in self.students]) / len(self.students)

    def passed(self) -> list[Student]:
        return [student for student in self.students if student.is_pass()]


students: list[Student] = [s1, s2]
gradebook = GradeBook(students)
print(gradebook.average())
print(gradebook.passed())
