

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
