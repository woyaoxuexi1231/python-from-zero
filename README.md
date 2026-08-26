# Python 从零开始

Python 入门课：每次只学一小块，跑通、改一改、真正理解，再进入下一课。

## 怎么运行

```powershell
cd python-from-zero
python 01_hello/01_hello.py            # 每课一个文件夹，跑里面的主课文件
# 最后一课(36)两阶段对照（同一端口 8899，同时只起一个服务）
# 阶段1 标准库：
python 36_requests/36_stdlib_server.py   # 终端1
python 36_requests/36_stdlib_client.py   # 终端2
# 阶段2 三方（需 pip install requests flask）：
python 36_requests/36_flask_server.py    # 终端1
python 36_requests/36_requests.py        # 终端2
```

**目录约定**：每一课都是一个独立文件夹（如 `01_hello/`、`18_modules/`），
主课文件与配套模块、数据文件都放进对应文件夹。

改代码 → 保存 → 再运行一次。看输出比只看代码更重要。

## 学习路线

| 课 | 文件 | 你会学会 |
|---|---|---|
| 1 | `01_hello/01_hello.py` | 运行程序、打印、变量、基本类型、函数和返回值 |
| 2 | `02_strings_and_input/02_strings_and_input.py` | 字符串、输入、类型转换 |
| 3 | `03_if_else/03_if_else.py` | if / else 判断 |
| 4 | `04_lists_and_loops/04_lists_and_loops.py` | 列表、循环 |
| 5 | `05_dicts/05_dicts.py` | 字典 |
| 6 | `06_gradebook/06_gradebook.py` | 成绩本：把前面的拼起来 |
| 7 | `07_while_menu/07_while_menu.py` | while、break、菜单：成绩本改成循环 |
| 8 | `08_try_except/08_try_except.py` | try / except：输入错误时提示，不崩 |
| 9 | `09_files_json/09_files_json.py` | 文件和 JSON：成绩写进文件，下次还能读 |
| 10 | `10_tuples_and_sets/10_tuples_and_sets.py` | 元组、集合：多返回值、去重、成员判断 |
| 11 | `11_slice_range_enumerate/11_slice_range_enumerate.py` | 切片、range、enumerate：取一段、带编号循环 |
| 12 | `12_none_and_or/12_none_and_or.py` | None、真假值、and / or |
| 13 | `13_functions/13_functions.py` | 默认参数、*args、多返回值 |
| 14 | `14_list_comprehension/14_list_comprehension.py` | 列表推导式：映射和过滤的短写法 |
| 15 | `15_lambda_map_filter/15_lambda_map_filter.py` | lambda 小函数、sorted(key=)、map / filter：函数当参数传 |
| 16 | `16_class_basics/16_class_basics.py` | 类与对象：把数据和行为绑一起，`__init__`、`self`、`@property`、对象排序 |
| 17 | `17_review/17_review.py`（主课）+ `17_review.json`（数据） | 复习课：第 1~16 课综合大通关（一个成绩管理场景串起全部知识点） |
| 18 | `18_modules/18_modules.py` | 模块与包：import、`from…import`、`as` 别名、`__name__`、自己写模块 |
| 19 | `19_iterators_generators/19_iterators_generators.py` | 迭代器与生成器：`iter`/`next`/`yield`、惰性求值、无限序列、生成器表达式 |
| 20 | `20_files_paths/20_files_paths.py` | 文件与路径实操：`pathlib` 拼/拆路径、`iterdir`/`glob`/`rglob` 遍历目录、惰性逐行读大文件、批量处理 |
| 21 | `21_review/21_review.py` | 复习课：第 18~20 课大通关（模块 import / 生成器 / pathlib 批量统计写 JSON） |
| 22 | `22_oop_inheritance/22_oop_inheritance.py`（知识）+ `22_oop_inheritance_exercise.py`（练习） | OOP 进阶：继承、`super()` 构造链、方法重写、多态/鸭子类型、`isinstance`/`issubclass`、魔术方法与 `@property` |
| 23 | `23_decorators/23_decorators.py`（知识）+ `23_decorators_exercise.py`（练习） | 装饰器：函数一等公民、手写包装、`@` 语法糖、`*args/**kwargs` 透传、`functools.wraps`、带参装饰器、`functools.lru_cache` |
| 24 | `24_context_manager/24_context_manager.py`（知识）+ `24_context_manager_exercise.py`（练习） | 上下文管理器：`with` 文件、`__enter__`/`__exit__`、异常吞不吞、`@contextmanager`、return 提前退出也清理、事务/连接/回滚场景 |
| 25 | `25_collections_itertools/25_collections_itertools.py`（知识）+ `25_collections_itertools_exercise.py`（练习） | 常用数据结构+itertools：list/dict/set 推导式、`defaultdict` 分组、`Counter` 计数、`namedtuple`、`chain/count/cycle/islice`、`groupby`、`product/permutations/combinations`、`accumulate` |
| 26 | `26_dataclasses/26_dataclasses.py`（知识）+ `26_dataclasses_exercise.py`（练习） | dataclass：`@dataclass` 少写样板、默认值与 `field(default_factory=...)`、`frozen`/`order`、`__post_init__` 校验、`asdict`/`astuple` 序列化 |
| 27 | `27_typing/27_typing.py`（知识）+ `27_typing_exercise.py`（练习） | typing 进阶：`list[str]`/`dict[K,V]`、`T \| None`/`Optional`、`Union`/`\|`、`Literal`、`TypedDict`、`Callable`、与 dataclass 联用 |
| 28 | `28_collections_review/28_collections_review.py`（知识）+ `28_collections_review_exercise.py`（练习） | collections 复习强化：defaultdict 三种工厂、Counter 合并与 most_common、namedtuple _replace、deque 滑动窗口；UserDict/OrderedDict/ChainMap 了解；单文件 __init__.py 包结构 |
| 29 | `29_itertools_review/29_itertools_review.py`（知识）+ `29_itertools_review_exercise.py`（练习） | itertools 复习强化：chain/from_iterable、islice+count/cycle、sort+groupby、product/permutations/combinations、accumulate 前缀累积 |
| 30 | `30_enum/30_enum.py`（知识）+ `30_enum_exercise.py`（练习） | enum：`Enum`/`IntEnum`/`StrEnum`、`name`/`value`、反查、`auto()`；替代魔法字符串 |
| 31 | `31_datetime/31_datetime.py`（知识）+ `31_datetime_exercise.py`（练习） | 时间与日期：`datetime`/`date`/`time`、`strftime` 格式化、`strptime` 解析、`timedelta` 加减、比较与 `.replace`；文件名时间戳、到期日 |
| 32 | `32_re/32_re.py`（知识）+ `32_re_exercise.py`（练习） | 正则：`search`/`findall`/`fullmatch`/`sub`、`\d`/`\w`/`\s`、`+`/`*`、`[...]`/`(...)`、raw 字符串；抠数字、校验手机号/IP |
| 33 | `33_argparse/33_argparse.py`（知识）+ `33_argparse_exercise.py`（练习） | argparse：位置/可选参数、`type`/`default`、`store_true`、`choices`；`parse_args(列表)` 测 CLI，菜单升级成命令行工具 |
| 34 | `34_logging/34_logging.py`（知识）+ `34_logging_exercise.py`（练习） | logging：五级日志、`getLogger`、`basicConfig`、`Handler`/`Formatter`、`ColorFormatter` 控制台上色；`verbose` 联动 argparse |
| 35 | `35_pytest/35_pytest.py`（知识）+ `test_tools_demo.py` + `35_pytest_exercise.py`（练习） | pytest（需 `pip install pytest`）：`assert`、`test_` 命名、`raises`、`parametrize`；给函数写可重复验证的测试 |
| 36 | 阶段1：`36_stdlib_server.py` + `36_stdlib_client.py`；阶段2：`36_flask_server.py` + `36_requests.py`；+ `36_requests_exercise.py` | HTTP 对照：标准库 `urllib`/`http.server` vs 三方 `requests`/`Flask`（需 pip）；同一套路由、不发外网；**基础课收官** |

先把第 1 课吃透。不要跳。每课做完练习再往下。
