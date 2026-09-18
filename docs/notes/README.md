# Python 从零 · 笔记

共 38 篇。按顺序读即可。

| 课次 | 标题 | 摘要 | 更新 |
| --- | --- | --- | --- |
| 1 | [第 1 课：你好，Python](01-你好，Python.md) | 程序如何执行、print、变量与对象、四种基本类型、函数与 return、类型标注。从直觉讲清楚，不绑死某一份练习文件。 | 2026-08-24 |
| 2 | [第 2 课：字符串、输入与类型转换](02-字符串、输入与类型转换.md) | 字符串拼接、f-string、input 永远返回 str、int/float/str 显式转换、与函数联用的数据流。 | 2026-08-24 |
| 3 | [第 3 课：if / else 判断](03-if - else 判断.md) | 比较运算符、缩进分支、elif 命中即停、在函数里 return 判断结果、与 input 联用。 | 2026-08-24 |
| 4 | [第 4 课：列表与循环](04-列表与循环.md) | 列表与索引、for 逐项处理、循环里判断、累计求和、append 收集结果。 | 2026-08-24 |
| 5 | [第 5 课：字典](05-字典.md) | 用键找值、读改加、in 防 KeyError、items 循环、字典作函数参数与返回值。 | 2026-08-24 |
| 6 | [第 6 课：成绩本——拼起来](06-成绩本——拼起来.md) | 数据 + 一事一职函数 + 主流程；None 表示找不到；平均分与及格名单。 | 2026-08-24 |
| 7 | [第 7 课：while 与菜单](07-while 与菜单.md) | while 条件循环、while True + break、continue、菜单选项与字符串比较。 | 2026-08-24 |
| 8 | [第 8 课：try / except](08-try - except.md) | ValueError 接住非法 int、具体 except 类型、失败提示后继续菜单、while + try 直到输对。 | 2026-08-24 |
| 9 | [第 9 课：文件与 JSON](09-文件与 JSON.md) | import、with open 与 UTF-8、json.dump/load、FileNotFoundError 默认成绩、持久化成绩本。 | 2026-08-24 |
| 10 | [第 10 课：元组与集合](10-元组与集合.md) | 不可变元组、拆包与多返回值、集合去重与 in、空集合必须用 set()。 | 2026-08-24 |
| 11 | [第 11 课：切片、range、enumerate](11-切片、range、enumerate.md) | 含头不含尾的切片、负数下标与步长、range 计数、enumerate 带编号循环。 | 2026-08-24 |
| 12 | [第 12 课：None、真假值、and / or](12-None、真假值、and - or.md) | is None 判断缺席、if 的假值列表、0 分不是没有、and/or 短路与默认值。 | 2026-08-24 |
| 13 | [第 13 课：函数进阶](13-函数进阶.md) | 默认参数、关键字参数、*args、多返回值复习、可变默认值陷阱。 | 2026-08-24 |
| 14 | [第 14 课：列表推导式](14-列表推导式.md) | 映射与过滤的短写法、与 for+append 对照、何时不该用推导式。 | 2026-08-24 |
| 15 | [第 15 课：lambda 与 map / filter / sorted](15-lambda 与 map - filter - sorted.md) | lambda 小函数、sorted(key=) 必会组合、map/filter 与推导式怎么选。 | 2026-08-24 |
| 16 | [第 16 课：类与对象](16-类与对象.md) | __init__ 与 self、方法绑数据、@property、__str__/__repr__、对象排序。 | 2026-08-24 |
| 17 | [第 17 课：复习通关（1～16）](17-复习通关（1～16）.md) | 不教新语法：成绩场景串起函数、异常、推导、集合、None、class 等，配课自检。 | 2026-08-24 |
| 18 | [第 18 课：模块与包](18-模块与包.md) | import / from…import / as、模块互引、__name__ == "__main__"、单文件模块入门。 | 2026-08-24 |
| 19 | [第 19 课：迭代器与生成器](19-迭代器与生成器.md) | iter/next/StopIteration、迭代器一次性、yield 惰性、生成器表达式。 | 2026-08-24 |
| 20 | [第 20 课：文件与路径实操](20-文件与路径实操.md) | pathlib 拼路径、iterdir/glob/rglob、逐行惰性读大文件、批量处理。 | 2026-08-24 |
| 21 | [第 21 课：复习通关（18～20）](21-复习通关（18～20）.md) | 模块 + 生成器 + pathlib：扫目录统计 txt，汇总写 JSON。 | 2026-08-24 |
| 22 | [第 22 课：OOP 进阶——继承与多态](22-OOP 进阶——继承与多态.md) | 继承、super()、方法重写、鸭子类型、isinstance/issubclass。 | 2026-08-24 |
| 23 | [第 23 课：装饰器](23-装饰器.md) | 函数一等公民、手写包装、@ 语法糖、*args/**kwargs、functools.wraps。 | 2026-08-24 |
| 24 | [第 24 课：上下文管理器 with](24-上下文管理器 with.md) | with 文件、__enter__/__exit__、异常吞不吞、@contextmanager、用完必清理。 | 2026-08-24 |
| 25 | [第 25 课：collections + itertools](25-collections + itertools.md) | defaultdict 分组、Counter 计数、namedtuple、chain/islice/groupby、排列组合、accumulate。 | 2026-08-24 |
| 26 | [第 26 课：dataclass 数据类](26-dataclass 数据类.md) | @dataclass 少写样板、default_factory、frozen/order、__post_init__ 校验、asdict 序列化。 | 2026-08-24 |
| 27 | [第 27 课：typing 类型标注进阶](27-typing 类型标注进阶.md) | list[str]/dict[K,V]、Optional 与 \| None、Union、Literal、TypedDict、Callable、与 dataclass 联用。 | 2026-08-24 |
| 28 | [第 28 课：collections 复习强化](28-collections 复习强化.md) | defaultdict 三种工厂、Counter 与 most_common、namedtuple、deque 滑动窗口；6 道新题练熟练。 | 2026-08-24 |
| 29 | [第 29 课：itertools 复习强化](29-itertools 复习强化.md) | chain/islice/groupby 先排序、product/permutations/combinations、accumulate 前缀累积；6 道新题。 | 2026-08-24 |
| 30 | [第 30 课：enum 枚举](30-enum 枚举.md) | Enum/IntEnum/StrEnum、name/value、反查与 auto()；用枚举替代魔法字符串，接近 Java enum。 | 2026-08-24 |
| 31 | [第 31 课：datetime 日期与时间](31-datetime 日期与时间.md) | datetime/date/time、strftime 格式化、strptime 解析、timedelta 加减、比较与 .replace；配文件名时间戳与到期日练习。 | 2026-08-24 |
| 32 | [第 32 课：re 正则表达式](32-re 正则表达式.md) | search/findall/fullmatch/sub、\d/\w/\s、+/*、[..]/(..)、raw 字符串；抠数字、校验手机号与 IP。 | 2026-08-24 |
| 33 | [第 33 课：argparse 命令行参数](33-argparse 命令行参数.md) | ArgumentParser、位置/可选参数、type/default、store_true、choices；用 parse_args(列表) 测 CLI，菜单升级成脚本入口。 | 2026-08-25 |
| 34 | [第 34 课：logging 分级日志](34-logging 分级日志.md) | DEBUG/INFO/WARNING/ERROR、getLogger、basicConfig、Handler+Formatter、ColorFormatter 上色；verbose 联动 argparse。 | 2026-08-25 |
| 35 | [第 35 课：pytest 写断言](35-pytest 写断言.md) | pip install pytest、test_ 命名、assert、raises、parametrize；给函数写可重复验证的测试。 | 2026-08-25 |
| 36 | [第 36 课：HTTP 调用与暴露（标准库 vs 三方）](36-HTTP 调用与暴露（标准库 vs 三方）.md) | 标准库对照 + 主流 HTTP 三方全景（优劣/热度/生产建议）与各库最小教程；ThreadingHTTPServer 原理；基础课收官。 | 2026-08-26 |
| 37 | [第 37 课：os 与配置读取（os.getenv / BaseSettings）](37-os 与配置读取（os.getenv - BaseSettings）.md) | os 是什么、os.getenv / os.path 常用 API；手写配置的痛点 → pydantic-settings 的 BaseSettings：读 .env、类型转换校验、字段↔变量对应、优先级，配合 @lru_cache 全局唯一。 | 2026-08-26 |
| — | [Python 标准库地图：模块分级与学习顺序](Python 标准库地图.md) | 内置 / 标准库 / PyPI 怎么分；★初学必学、◎常用、○以后；from-zero 进度与接下来先学哪 8 个。 | 2026-08-24 |
