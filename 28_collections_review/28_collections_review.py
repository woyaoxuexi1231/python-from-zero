# ============================================================
# 第 28 课（复习强化）：collections 模块 —— 分组、计数、轻量记录
# 运行方式：python 28_collections_review/28_collections_review.py
# 配套练习：28_collections_review_exercise.py（自检，全是新场景）
# ============================================================
from collections import defaultdict, Counter, namedtuple, deque

# 第 25 课第一次见 collections，和 itertools 挤在一课里，容易「看过但不会用」。
# 这一课只复习 collections 四个最常用的：defaultdict / Counter / namedtuple / deque。
# 目标：看见「分组、计数、只读小对象、队列」时，手能自动伸过去。
print("========== 第28课 collections 复习强化 ==========\n")


# ---------- 1. defaultdict：复习 + 三种常用工厂 ----------
print("【1】defaultdict：缺键自动造默认值")
# 核心：bucket[key] 时 key 不存在 → 先调用工厂，再返回新造的空容器。
# 和 bucket = {} 的区别：普通 dict 缺键 KeyError；defaultdict 缺键「现造一个」。

# 工厂 list → 分组收集
by_word: defaultdict[str, list] = defaultdict(list)
for w in ["go", "py", "go", "go"]:
    by_word[w].append(w)
print("  list 工厂分组:", dict(by_word))

# 工厂 set → 分组且去重（如：每个用户去过哪些页面）
pages: defaultdict[str, set] = defaultdict(set)
visits = [("u1", "/home"), ("u2", "/home"), ("u1", "/about")]
for user, path in visits:
    pages[user].add(path)
print("  set 工厂去重:", {k: sorted(v) for k, v in pages.items()})

# 工厂 int → 缺键当作 0，适合计数（Counter 的内部思路类似）
hits: defaultdict[str, int] = defaultdict(int)
for ch in "banana":
    hits[ch] += 1          # 第一次 hits['b'] 不存在 → 先 int() 得 0，再 +=1
print("  int 工厂计数:", dict(hits))

print("  小抄：分组 list/set，计数 int；最后 dict(dd) 可转普通 dict")


# ---------- 2. Counter：比 defaultdict(int) 更方便的计数 ----------
print("\n【2】Counter：专用计数器")
cnt = Counter("abracadabra")
print("  基本:", dict(cnt))
print("  最多 2 个:", cnt.most_common(2))

# 合并计数：两个 Counter 可以直接相加
a = Counter("aab")
b = Counter("abb")
print("  相加:", dict(a + b))       # a:2 b:3

# elements()：按个数重复展开（了解即可）
print("  elements 前6:", list(Counter(a=2, b=1).elements())[:6])

print("  小抄：Counter(可迭代) 计数；most_common(n)；c1+c2 合并")


# ---------- 3. defaultdict vs Counter：什么时候用哪个 ----------
print("\n【3】分组 vs 计数 —— 别混")
print("  要「每个键对应一列表/集合」→ defaultdict(list/set)")
print("  要「每个键出现几次」→ Counter 或 defaultdict(int)")
print("  要「Top N 频次」→ Counter.most_common，别手写排序")


# ---------- 4. namedtuple：轻量只读记录 ----------
print("\n【4】namedtuple：带名字的元组")
Student = namedtuple("Student", ["name", "score"])
s = Student("小明", 90)
print("  字段访问:", s.name, s.score)
print("  下标也行:", s[0], s[1])
print("  解包:", *s)

# 不可变：想「改一个字段」用 _replace，返回新对象
s2 = s._replace(score=95)
print("  _replace:", s, "→", s2)

# 转 dict（序列化友好）
print("  _asdict:", s._asdict())

print("  小抄：namedtuple('类名', [字段...])；只读；改字段用 _replace")


# ---------- 5. deque：双端队列（第 25 课没细讲） ----------
print("\n【5】deque：两头都能 append/pop，比 list 头插快")
q: deque[int] = deque([1, 2, 3])
q.append(4)           # 右端加
q.appendleft(0)       # 左端加
print("   deque:", list(q))
print("  右 pop:", q.pop(), "→", list(q))
print("  左 pop:", q.popleft(), "→", list(q))

# 固定长度 deque → 滑动窗口
window: deque[int] = deque(maxlen=3)
for x in [1, 2, 3, 4, 5]:
    window.append(x)
    print(f"    加入 {x}，窗口:", list(window))
print("  小抄：deque(maxlen=n) 做最近 N 条；队列/栈/滑动窗口")


# ---------- 6. 易错点 ----------
print("\n【6】易错点速记")
print("  ① defaultdict(list()) 错！要 defaultdict(list) —— 传工厂函数，不是 list()")
print("  ② 只想查有没有键：用 key in d，别 d[key] —— defaultdict 会顺便创建键")
print("  ③ Counter 的 most_common(0) 返回 []；most_common() 返回全部按频次排")
print("  ④ namedtuple 字段名不能是 Python 关键字；类名首字母大写是习惯")
print("  ⑤ deque 左端用 appendleft/popleft，list 头插是 O(n) 慢")


# ---------- 7. collections 里还有哪些？（了解即可，日常少写） ----------
print("\n【7】collections 里还有哪些？")
# dir(collections) 还能看到 UserDict / UserList / UserString / OrderedDict / ChainMap / abc …
# 这一课四个（defaultdict/Counter/namedtuple/deque）占日常 90%；下面知道「干什么用」即可。

# ① UserDict / UserList / UserString：给「想继承并改行为」的人用的包装基类
#    不要写 class MyDict(dict): ……  内置 dict/list/str 在 C 里实现，直接子类化容易踩坑。
#    UserDict 内部持有一个真正的 dict（self.data），你重写 __setitem__ 等方法就行。
from collections import UserDict, OrderedDict, ChainMap

class UpperDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(str(key).upper(), value)

ud = UpperDict({"a": 1})
ud["b"] = 2
print("  UserDict 子类键自动大写:", dict(ud))

# ② OrderedDict：插入顺序 dict。Py3.7+ 普通 dict 也有序了，但 OrderedDict 还有 move_to_end 等。
od = OrderedDict([("first", 1), ("second", 2)])
od.move_to_end("first")          # 把 first 挪到末尾
print("  OrderedDict move_to_end:", list(od.keys()))

# ③ ChainMap：多个 dict 叠成一层查找链，先查第一个，没有再查第二个……
defaults = {"color": "red", "size": "M"}
user_prefs = {"color": "blue"}
merged = ChainMap(user_prefs, defaults)   # 像「局部覆盖全局配置」
print("  ChainMap 覆盖查 color:", merged["color"], "size:", merged["size"])

# ④ abc 子模块：MutableMapping / Sequence 等抽象基类，做 isinstance 检查或规范接口。
#    写框架、插件系统时可能见到；业务代码很少直接继承。

print("  易混：第 27 课 typing.TypedDict 里的 class UserDict 是「类型标注」，")
print("        和 collections.UserDict（可继承的 dict 包装类）完全不是一回事！")


# ---------- 8. 为什么 collections 包只有一个 __init__.py？ ----------
print("\n【8】collections 包为什么只有一个 __init__.py？")
import collections as coll_pkg
init_path = coll_pkg.__file__ or "(未知)"
print("  collections 模块文件:", init_path)
print("  Java 习惯：com.example.User 一个类一个 .java，包目录里很多源文件。")
print("  Python 包 = 文件夹 + __init__.py，但**不强制**一个类一个 .py。")
print("  标准库 collections 历史久、对外 API 稳定，实现全堆在一个 __init__.py 里（几千行）。")
print("  import collections 时 Python 执行这个 __init__.py，再把你看到的 Counter/deque 等挂到模块上。")
print("  这不算违规——是 Python 常见的组织方式，尤其小中型标准库模块。")
print("  你自己写项目：两三个类可以单文件；目录变大就拆成 counter.py / deque.py，")
print("  在 __init__.py 里 from .counter import Counter 统一对外，对外仍是 import collections。")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("defaultdict(list/set/int)：分组 / 去重分组 / 计数")
print("Counter：计数 + most_common + 可加合并")
print("namedtuple：轻量记录 + _replace + _asdict")
print("deque：双端队列 + maxlen 滑动窗口")
print("UserDict/OrderedDict/ChainMap：扩展 dict / 有序+move_to_end / 多层 dict 查找链")
print("包可以只有一个 __init__.py；大了再拆文件，__init__.py 做统一出口")
