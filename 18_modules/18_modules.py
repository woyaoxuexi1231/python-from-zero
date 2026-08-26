# ============================================================
# 第 18 课：模块与包（import / 自己写模块 / __name__）
# 运行方式：python 18_modules/18_modules.py
# ============================================================


# 前面 1~17 课，所有代码都写在一个 .py 文件里。现实中代码要分文件、
# 分目录，才好复用和维护。这一课学怎么"把代码拆开、再拼回来"。
#
# 本课配套文件（同目录，都是自己写的模块）：
#   - tools.py   一个模块，里面装了变量(PI)和函数(greet/square/add)
#   - calc.py    另一个模块，它自己又 import 了 tools
#
# 你写 Java，对"包/导入"不陌生：Java 用 import com.x.Y；
# Python 用 import 模块名。差异：Python 一个 .py 文件就是一个模块，
# 不需要 package 关键字，文件夹 + __init__.py 才算"包"（本课先用单文件模块）。


# ---------- 1. import 整个模块，用 模块名.东西 调用 ----------
# 方式A：import 整个模块。之后凡是这个模块里的东西，都加前缀 tools.
import tools

print(tools.greet("小明"))   # 你好，小明！（来自 tools 模块）
print(tools.square(5))       # 25
print(tools.PI)              # 3.14159
print("-----")


# ---------- 2. from 模块 import 具体的东西，直接拿来用 ----------
# 方式B：只引入想要的名字。之后不用加前缀，直接写名字。
# 好处是短；坏处是同名容易撞，且看不出这东西来自哪个模块。
from tools import square, greet, PI

print(square(7))             # 49  （直接写，不用 tools.）
print(greet("小红"))          # 你好，小红！（来自 tools 模块）
print(PI)                    # 3.14159
print("-----")


# ---------- 3. 给 import 起别名 as ----------
# 方式C：名字太长、或想避免重名时用 as 改名。
import calc as c

print(c.sum_list([1, 2, 3, 4]))   # 10.0
print(c.mean([10, 20, 30]))       # 20.0
print("-----")


# ---------- 4. 模块之间也能互相 import ----------
# 注意 calc.py 里写了 `from tools import add`，
# 也就是说 calc.sum_list 内部复用了 tools 的 add。
# 模块不是孤岛，可以像搭积木一样互相调用。打开 calc.py 看一眼就懂。
# 这里直接验证：用 calc 算总和，底层其实走了 tools.add
print(c.sum_list([1, 2, 3]))   # 6.0  （calc 内部调用了 tools.add）
print("-----")


# ---------- 5. __name__ == "__main__" 是干嘛的 ----------
# 当一个 .py 被「直接运行」(python xxx.py) 时，它内部的 __name__ 是 "__main__"；
# 当它被别的文件 import 时，__name__ 是模块名（tools 文件里就是 "tools"）。
#
# 所以 tools.py 末尾写了：
#   if __name__ == "__main__":
#       print("tools.py 被直接运行了")
# 这段代码：你 `python tools.py` 时会跑；但被我们 import 时不会跑。
# 用途：模块既能当"零件"被别人引入（不触发演示代码），
#       又能自己单独运行做测试/演示。
#
# 验证一下：本文件是直接运行的，所以 __name__ 是 "__main__"
print("本文件 __name__ =", __name__)   # __main__
print("tools 模块 __name__ =", tools.__name__)  # tools
print("-----")


# ---------- 6. 包（package）一句话 ----------
# 包 = 带 __init__.py 的文件夹，里面放多个模块。
# 引入方式变成：from 包名 import 模块，或 from 包名.模块 import 函数。
# 本课先用单文件模块就够了，等你做更大项目（比如把成绩系统拆一堆文件）
# 再上包。知道"文件夹 + __init__.py = 包"即可。


# ---------- 练习 ----------
# 1. 在 tools.py 里再加一个函数 double(n) -> n*2，
#    然后回到本文件顶部加一行 `from tools import double`，
#    下面打印 double(21)。保存后再运行，看输出 42。
#

# 2. 新建一个模块 logger.py（同目录），里面写一个函数 log(msg)，
#    往屏幕打印 "[LOG] msg"。再在本文件里 import 它并打印一句话。
#    （这一步练的是"自己从零建一个模块并被引入"。）
#

# 3. 把第 16 课的 Student 类复制到本目录的 models.py，
#    然后 `from models import Student`，创建两个学生打印一下。
#    （体会：类也能放进模块，被别的文件 import —— 和 Java 的包思想一致。）
#

print("===== 练习区（把上面 3 题写在这里，保存后运行）=====")

# 题1 示范（取消注释并先按练习说明改 tools.py）：
from tools import double
print(double(21))   # 42

# 题2 示范（先建 logger.py）：
import logger
logger.log("模块系统跑通了")

# 题3 示范（先建 models.py）：
from models import Student
a = Student("小明", 90)
b = Student("小红", 40)
print(a, b, a.is_pass(), b.is_pass())
