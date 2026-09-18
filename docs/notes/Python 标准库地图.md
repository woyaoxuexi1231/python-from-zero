# Python 标准库地图：模块分级与学习顺序

`Python 生态` · 更新于 2026-08-24 · 标签：Python、生态、标准库

**摘要**：内置 / 标准库 / PyPI 怎么分；★初学必学、◎常用、○以后；from-zero 进度与接下来先学哪 8 个。

---

Python 标准库模块多、名字散，不像一门课那样按章排好。 这篇只做一件事：**官方有哪些模块、初学先学哪档、from-zero 学到哪了、后面按什么顺序扩**。

## 先分三层：别混在一块

| 层次 | 例子 | 要 pip install 吗 |
| --- | --- | --- |
| 内置（不用 import） | `list`、`print`、`open`、`def`、`class` | 否，装 Python 就有 |
| 标准库（import 即用） | `json`、`pathlib`、`dataclasses`、`typing` | 否 |
| 第三方 PyPI | `requests`、`pytest`、`fastapi` | 是（`pip` / `uv`） |

> **原理**
>
> 标准库叫「batteries included」：常用能力尽量自带。 但 HTTP、测试、Web 等领域，社区第三方往往比官方更好用—— 看到 `pip install xxx`，默认 **xxx 不是标准库**。 能在 docs.python.org/3/library/ 搜到模块名，才是官方。

## 学习分级：先学哪档

- ★ 初学必学 — 写小程序、from-zero、日常脚本离不开
- ◎ 常用 — 真实项目常碰；★ 学稳后再扩（约 1～2 个月内）
- ○ 知道即可 — 用时再查，不必背 API
- · 专项/少见 — GUI、底层网络等，初学可跳过

**策略**：先把所有 ★ 吃透；再按文末顺序加 ◎；○ 和 · 当字典。

## 内置（不用 import）

| 优先级 | 内容 | 干什么 |
| --- | --- | --- |
| ★ | `int` `float` `str` `bool` | 基本类型 |
| ★ | `list` `dict` `set` `tuple` | 容器 |
| ★ | `print` `len` `range` `sorted` `enumerate` `zip` | 常用内置函数 |
| ★ | `open` `input` | 读写文件、读用户输入 |
| ★ | `def` `class` `try/except` `raise` | 函数、类、异常 |
| ★ | `if` `for` `while` `with` | 控制流、上下文（with 文件） |
| ◎ | `isinstance` `hasattr` `getattr` `type` | 运行时类型与属性 |
| ◎ | `any` `all` `min` `max` `sum` | 聚合、判断 |

## 标准库模块（import 即用）

按领域分组；「from-zero」列标你课里是否已专门学过。

### 数据与容器

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ★ | `collections` | defaultdict、Counter、namedtuple、deque | 第 25 课 ✓ |
| ★ | `itertools` | chain、islice、groupby、product、accumulate | 第 25 课 ✓ |
| ★ | `dataclasses` | @dataclass、field、asdict | 第 26 课 ✓ |
| ★ | `typing` | Optional、Literal、TypedDict、Callable | 第 27 课 ✓ |
| ◎ | `enum` | Enum 枚举固定几种值 | 第 30 课 |

### 文件、路径、序列化

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ★ | `json` | dump、load、读写 JSON 文件 | 第 9 课 ✓ |
| ★ | `pathlib` | Path、拼路径、glob、iterdir | 第 20 课 ✓ |
| ★ | `os` / `sys` | 环境变量、argv、退出码 | 零散 |
| ○ | `csv` | 读写 CSV 表格 | 未学 |
| ○ | `pickle` | Python 对象二进制序列化（慎用不可信来源） | 未学 |

### 函数式、装饰器、资源管理

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ★ | `functools` | wraps、lru_cache、partial | 第 23 课 ✓ |
| ★ | `contextlib` | @contextmanager、suppress | 第 24 课 ✓ |

### 模块与包、迭代

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ★ | （内置 + `import` 机制） | 模块、`__name__ == "__main__"` | 第 18 课 ✓ |
| ★ | 生成器 / 迭代器（语言特性） | yield、iter、next | 第 19 课 ✓ |

### 文本、时间、命令行

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ◎ | `re` | 正则 search、match、sub | 第 32 课 |
| ◎ | `datetime` | now、strftime、timedelta | 第 31 课 |
| ◎ | `argparse` | 命令行参数，替代手写菜单 | 第 33 课 |
| ◎ | `logging` | 分级日志，替代满屏 print | 第 34 课 |

### 测试、网络、并发

| 优先级 | 模块 | 常用内容 | from-zero |
| --- | --- | --- | --- |
| ◎ | `unittest` | 官方单元测试 | 了解；实战用 pytest（第 35 课） |
| ◎ | `urllib.request` | 官方 HTTP（偏底层） | 第 36 课阶段 1 ✓；实战多用 requests |
| ◎ | `threading` / `concurrent.futures` | 线程、线程池 | 未学 |
| ○ | `asyncio` | 异步协程 | 以后 |
| ○ | `multiprocessing` | 多进程 | 以后 |
| ○ | `subprocess` | 调外部命令 | 以后 |
| ○ | `sqlite3` | 嵌入式数据库 | 以后 |

### 其它标准库（知道即可 / 专项）

| 优先级 | 模块 | 备注 |
| --- | --- | --- |
| ○ | `hashlib`、`secrets` | 哈希、安全随机数 |
| ○ | `xml.etree`、`html` | 解析 XML / HTML |
| · | `tkinter` | 内置 GUI，初学可跳过 |
| · | `socket`、`email`… | 底层网络、邮件，用时再查 |

## 第三方 PyPI（初学后会常碰）

| 优先级 | 包名 | 干什么 | 和官方关系 |
| --- | --- | --- | --- |
| ◎ | `pytest` | 写测试、断言 | 第 35 课 ✓；比 `unittest` 更顺手；需 pip |
| ◎ | `requests` | 发 HTTP 请求 | 第 36 课阶段 2 ✓；官方有 `urllib`，但 requests 更常用 |
| ◎ | `flask` | 写 Web / API（入门对照） | 第 36 课阶段 2 ✓；对照官方 `http.server` |
| ○ | `fastapi` | 写 Web / API（现代主流） | 后续项目再用；官方 `http.server` 仅演示级 |
| ○ | `pydantic` | 数据校验 | 常和 dataclass / FastAPI 搭配 |
| ○ | `numpy` / `pandas` | 数值、表格分析 | 标准库无对等物，走数据方向再学 |

> **踩坑**
>
> `dataclass`、`collections`、`itertools`、`typing` 都是**标准库**，`from xxx import` 即可，不要 pip。 教程写 `pip install requests` 的，才是第三方。

## from-zero 进度：★ 档覆盖到哪了

第 1～27 课已覆盖绝大部分 ★ 标准库与内置能力：

- 内置：类型、容器、循环、函数、类、异常
- `json`、`pathlib` — 存盘与路径
- `functools`、`contextlib` — 装饰器与 with
- `collections`、`itertools` — 容器与迭代工具
- `dataclasses`、`typing` — 数据类与类型标注

你现在处在：**★ 与 ◎ 基础路线已收官（含 pytest / HTTP 标准库 vs requests+Flask）；可大复习后开自己的项目**。

## 学完 ★ 之后，建议按这个顺序扩 ◎

2. `enum` — 订单/任务等固定状态（第 30 课 ✓）
4. `datetime` — 日志时间、文件名时间戳（第 31 课 ✓）
6. `re` — 从文本里抠字段（第 32 课 ✓）
8. `argparse` — 菜单程序升级成 CLI（第 33 课 ✓）
10. `logging` — 代替 print 调试（第 34 课 ✓）
12. `pytest`（第三方）— 给函数写断言（第 35 课 ✓）
14. `requests` + `Flask`（第三方）— HTTP 调用与暴露，对照标准库（第 36 课 ✓）
16. `threading` / `concurrent.futures` — 真需要并行时再学

## 官方文档去哪查

- **标准库索引**： Library Reference —— 按模块字母排列，相当于 API 总目录。
- **内置类型/函数**： Built-in Types、 Built-in Functions。
- **第三方**： pypi.org + 各项目文档。

## 收束

不必背全标准库几百个模块。记住分级： **★ 跟 from-zero 走**（你已在第 27 课）； **◎ 按上面 8 条慢慢加**； 其余 ○、· **知道有这东西，用时再查 Library Reference**。 这张表就是 Python 侧的「包地图」。

---

上一课：[第 37 课：os 与配置读取（os.getenv / BaseSettings）](37-os 与配置读取（os.getenv - BaseSettings）.md)　|　下一课：—
