# ============================================================
# 第 22 课（练习）：OOP 进阶 —— 继承、多态
# 运行方式：python 22_oop_inheritance/22_oop_inheritance_exercise.py
# ============================================================

# 先读 22_oop_inheritance.py 讲概念，再来做这 5 题。
# 规则：函数/类都留了 pass 或空体，等你填。注释只有要求，没有答案。
# 写完保存后运行本文件，底部自检测试（✅/❌）告诉每题过了没。
# 期望输出都在每条用例的注释里，对不上就看 ❌ 改。

from typing import Any


# ---------- 题 1：基础继承 + 方法重写 ----------
# 已有父类 Animal（属性 name，方法 sound() 返回通用声音 "..."）。
# 写子类 Dog 重写 sound() -> "汪汪！"
# 写子类 Cat 重写 sound() -> "喵～"
class Animal:
    def __init__(self, name: str):
        self.name = name

    def sound(self) -> str:
        return "..."

class Dog(Animal):
    def sound(self) -> str:
        return "汪汪！"
        pass   # 填：return "汪汪！"

class Cat(Animal):
    def sound(self) -> str:
        return "喵～"
        pass   # 填：return "喵～"


# ---------- 题 2：super() 构造链 + 新增属性 ----------
# 已有 class Animal2(name, age)。写子类 Cat2(name, age, color)，
# 构造里用 super().__init__(name, age) 把 name/age 交给父类，
# 再给 self.color 存 color（子类新属性）。
class Animal2:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

class Cat2(Animal2):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color
        pass   # 填：super().__init__(name, age)  +  self.color = color


# ---------- 题 3：多态 + 鸭子类型 ----------
# 写函数 speak_all(animals) -> str
# 遍历列表里的每个对象，调它的 sound()，用 "、" 把各声音拼成一个字符串返回。
# 【重点】你不需要判断对象类型，只要它有 sound() 就行（鸭子类型）。
# 注意：列表里会混入一个和 Animal 无关、但自带 sound() 的 Robot。
def speak_all(animals: list[Any]) -> str:
    result = ""
    for animal in animals:
        result += animal.sound() + "、"
    return result[:-1]
    pass


# ---------- 题 4：继承 + 多态算面积 ----------
# 已有 class Shape（area() 返回 0.0）。
# 写子类 Rectangle(w, h)：构造存 self.w/self.h，重写 area() -> w*h。
# 写子类 Square(side)：构造存 self.side，重写 area() -> side*side。
class Shape:
    def area(self) -> float:
        return 0.0

class Rectangle(Shape):
    def __init__(self, w: float, h: float):
        self.w = w
        self.h = h

    def area(self) -> float:
        return self.w * self.h
        pass   # 填：return self.w * self.h

class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side
        pass   # 填：return self.side * self.side


# ---------- 题 5：继承链判定（isinstance 顺序） ----------
# 有三级继承：AnimalL3 -> DogL3 -> PuppyL3（Puppy 是 Dog 的子类）。
# 写函数 whoami(obj) -> str：
#   是 PuppyL3 的实例 → "puppy"
#   是 DogL3 的实例   → "dog"
#   是 AnimalL3 的实例 → "animal"
#   都不是           → "unknown"
# 提示：isinstance 会连父类一起算，所以判断顺序要先"子"后"父"。
class AnimalL3:
    def __init__(self, name: str):
        self.name = name

class DogL3(AnimalL3):
    pass

class PuppyL3(DogL3):
    pass

def whoami(obj: Any) -> str:
    if isinstance(obj, PuppyL3):
        return "puppy"
    if isinstance(obj, DogL3):
        return "dog"
    if isinstance(obj, AnimalL3):
        return "animal"
    return "unknown"
    pass


# ============ 测试框架（照搬第 17/21 课，不用改）============
def run_tests(title: str, cases: list[tuple]) -> bool:
    print(f"\n===== {title} =====")
    ok = 0
    for i, (expected, actual, desc) in enumerate(cases, 1):
        passed = expected == actual
        ok += passed
        mark = "✅" if passed else "❌"
        print(f"  {mark} 用例{i:02d} {desc}")
        if not passed:
            print(f"        期望: {expected!r}")
            print(f"        实际: {actual!r}")
    total = len(cases)
    print(f"  ---> {title}: {ok}/{total} 通过")
    return ok == total


if __name__ == "__main__":
    all_pass = True

    all_pass &= run_tests("题1 继承 + 重写（Dog/Cat 覆盖 sound）", [
        (Dog("旺财").name, "旺财", "继承到父类属性 name"),
        (Dog("旺财").sound(), "汪汪！", "Dog 重写的叫声"),
        (Cat("咪咪").sound(), "喵～", "Cat 重写的叫声"),
        (isinstance(Dog("a"), Animal), True, "Dog 是 Animal 的子类实例"),
        (issubclass(Cat, Animal), True, "Cat 是 Animal 的子类"),
        (issubclass(Dog, object), True, "一切类都是 object 的子类"),
    ])

    all_pass &= run_tests("题2 super 构造链 + 新属性", [
        (Cat2("咪咪", 2, "橘").name, "咪咪", "name 来自父类构造"),
        (Cat2("咪咪", 2, "橘").age, 2, "age 来自父类构造"),
        (Cat2("咪咪", 2, "橘").color, "橘", "color 是子类新属性"),
        (isinstance(Cat2("a", 1, "黑"), Animal2), True, "Cat2 是 Animal2 子类"),
        (isinstance(Animal2("a", 1), Cat2), False, "父类实例不是子类实例"),
    ])

    # 题3：混入无关的 Robot，验证鸭子类型
    class Robot:
        def sound(self) -> str:
            return "哔哔"

    mixed = [Dog("旺财"), Cat("咪咪"), Robot()]
    all_pass &= run_tests("题3 多态 + 鸭子类型（speak_all 不认类型）", [
        (speak_all([Dog("a"), Cat("b")]), "汪汪！、喵～", "按顺序拼接两种音"),
        (speak_all(mixed), "汪汪！、喵～、哔哔", "Robot 无关也算，顺序一致"),
        (speak_all([Robot()]) == "哔哔", True, "只有 Robot 也能发声"),
        (speak_all([]), "", "空列表返回空串"),
    ])

    all_pass &= run_tests("题4 继承 + 多态算面积", [
        (Rectangle(3, 4).area(), 12.0, "矩形 3x4 面积"),
        (Square(5).area(), 25.0, "方形 5x5 面积"),
        (Rectangle(1.5, 2).area(), 3.0, "浮点边长"),
        (isinstance(Rectangle(1, 2), Shape), True, "Rectangle 是 Shape 子类"),
        (issubclass(Square, Shape), True, "Square 是 Shape 子类"),
        (sum(s.area() for s in [Rectangle(2, 3), Square(4)]), 22.0, "混放多态求和"),
    ])

    p = PuppyL3("皮")
    all_pass &= run_tests("题5 继承链判定（isinstance 先后顺序）", [
        (whoami(p), "puppy", "Puppy 本体判成 puppy"),
        (whoami(DogL3("d")), "dog", "Dog 判成 dog"),
        (whoami(AnimalL3("a")), "animal", "Animal 判成 animal"),
        (whoami(123), "unknown", "无关对象 unknown"),
        (isinstance(p, DogL3), True, "Puppy 也是 Dog 的实例"),
        (issubclass(PuppyL3, AnimalL3), True, "间接继承也算"),
    ])

    print("\n" + "=" * 40)
    if all_pass:
        print("🎉 全部 5 题通过！继承/多态练习过关！")
    else:
        print("⚠️  有题目未全过，看上面的 ❌ 改对应实现，再跑一次。")