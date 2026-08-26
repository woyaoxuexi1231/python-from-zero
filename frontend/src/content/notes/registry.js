/**
 * 学习笔记 / 随笔 / 部署文档 注册表。
 * 新增文章：在此追加 meta，并在 articles/ 下放对应组件。
 */
export const noteArticles = [
  {
    slug: 'python-from-zero-01',
    title: '第 1 课：你好，Python',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '程序如何执行、print、变量与对象、四种基本类型、函数与 return、类型标注。从直觉讲清楚，不绑死某一份练习文件。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero01.vue')
  },
  {
    slug: 'python-from-zero-02',
    title: '第 2 课：字符串、输入与类型转换',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '字符串拼接、f-string、input 永远返回 str、int/float/str 显式转换、与函数联用的数据流。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero02.vue')
  },
  {
    slug: 'python-from-zero-03',
    title: '第 3 课：if / else 判断',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '比较运算符、缩进分支、elif 命中即停、在函数里 return 判断结果、与 input 联用。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero03.vue')
  },
  {
    slug: 'python-from-zero-04',
    title: '第 4 课：列表与循环',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '列表与索引、for 逐项处理、循环里判断、累计求和、append 收集结果。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero04.vue')
  },
  {
    slug: 'python-from-zero-05',
    title: '第 5 课：字典',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '用键找值、读改加、in 防 KeyError、items 循环、字典作函数参数与返回值。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero05.vue')
  },
  {
    slug: 'python-from-zero-06',
    title: '第 6 课：成绩本——拼起来',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '数据 + 一事一职函数 + 主流程；None 表示找不到；平均分与及格名单。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero06.vue')
  },
  {
    slug: 'python-from-zero-07',
    title: '第 7 课：while 与菜单',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'while 条件循环、while True + break、continue、菜单选项与字符串比较。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero07.vue')
  },
  {
    slug: 'python-from-zero-08',
    title: '第 8 课：try / except',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'ValueError 接住非法 int、具体 except 类型、失败提示后继续菜单、while + try 直到输对。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero08.vue')
  },
  {
    slug: 'python-from-zero-09',
    title: '第 9 课：文件与 JSON',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'import、with open 与 UTF-8、json.dump/load、FileNotFoundError 默认成绩、持久化成绩本。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero09.vue')
  },
  {
    slug: 'python-from-zero-10',
    title: '第 10 课：元组与集合',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '不可变元组、拆包与多返回值、集合去重与 in、空集合必须用 set()。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero10.vue')
  },
  {
    slug: 'python-from-zero-11',
    title: '第 11 课：切片、range、enumerate',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '含头不含尾的切片、负数下标与步长、range 计数、enumerate 带编号循环。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero11.vue')
  },
  {
    slug: 'python-from-zero-12',
    title: '第 12 课：None、真假值、and / or',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'is None 判断缺席、if 的假值列表、0 分不是没有、and/or 短路与默认值。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero12.vue')
  },
  {
    slug: 'python-from-zero-13',
    title: '第 13 课：函数进阶',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '默认参数、关键字参数、*args、多返回值复习、可变默认值陷阱。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero13.vue')
  },
  {
    slug: 'python-from-zero-14',
    title: '第 14 课：列表推导式',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '映射与过滤的短写法、与 for+append 对照、何时不该用推导式。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero14.vue')
  },
  {
    slug: 'python-from-zero-15',
    title: '第 15 课：lambda 与 map / filter / sorted',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'lambda 小函数、sorted(key=) 必会组合、map/filter 与推导式怎么选。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero15.vue')
  },
  {
    slug: 'python-from-zero-16',
    title: '第 16 课：类与对象',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '__init__ 与 self、方法绑数据、@property、__str__/__repr__、对象排序。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero16.vue')
  },
  {
    slug: 'python-from-zero-17',
    title: '第 17 课：复习通关（1～16）',
    series: 'Python 从零',
    tags: ['Python', '入门', '复习'],
    summary: '不教新语法：成绩场景串起函数、异常、推导、集合、None、class 等，配课自检。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero17.vue')
  },
  {
    slug: 'python-from-zero-18',
    title: '第 18 课：模块与包',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'import / from…import / as、模块互引、__name__ == "__main__"、单文件模块入门。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero18.vue')
  },
  {
    slug: 'python-from-zero-19',
    title: '第 19 课：迭代器与生成器',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'iter/next/StopIteration、迭代器一次性、yield 惰性、生成器表达式。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero19.vue')
  },
  {
    slug: 'python-from-zero-20',
    title: '第 20 课：文件与路径实操',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'pathlib 拼路径、iterdir/glob/rglob、逐行惰性读大文件、批量处理。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero20.vue')
  },
  {
    slug: 'python-from-zero-21',
    title: '第 21 课：复习通关（18～20）',
    series: 'Python 从零',
    tags: ['Python', '入门', '复习'],
    summary: '模块 + 生成器 + pathlib：扫目录统计 txt，汇总写 JSON。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero21.vue')
  },
  {
    slug: 'python-from-zero-22',
    title: '第 22 课：OOP 进阶——继承与多态',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '继承、super()、方法重写、鸭子类型、isinstance/issubclass。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero22.vue')
  },
  {
    slug: 'python-from-zero-23',
    title: '第 23 课：装饰器',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '函数一等公民、手写包装、@ 语法糖、*args/**kwargs、functools.wraps。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero23.vue')
  },
  {
    slug: 'python-from-zero-24',
    title: '第 24 课：上下文管理器 with',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'with 文件、__enter__/__exit__、异常吞不吞、@contextmanager、用完必清理。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero24.vue')
  },
  {
    slug: 'python-from-zero-25',
    title: '第 25 课：collections + itertools',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'defaultdict 分组、Counter 计数、namedtuple、chain/islice/groupby、排列组合、accumulate。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero25.vue')
  },
  {
    slug: 'python-from-zero-26',
    title: '第 26 课：dataclass 数据类',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: '@dataclass 少写样板、default_factory、frozen/order、__post_init__ 校验、asdict 序列化。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero26.vue')
  },
  {
    slug: 'python-from-zero-27',
    title: '第 27 课：typing 类型标注进阶',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'list[str]/dict[K,V]、Optional 与 | None、Union、Literal、TypedDict、Callable、与 dataclass 联用。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero27.vue')
  },
  {
    slug: 'python-from-zero-28',
    title: '第 28 课：collections 复习强化',
    series: 'Python 从零',
    tags: ['Python', '入门', '复习'],
    summary: 'defaultdict 三种工厂、Counter 与 most_common、namedtuple、deque 滑动窗口；6 道新题练熟练。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero28.vue')
  },
  {
    slug: 'python-from-zero-29',
    title: '第 29 课：itertools 复习强化',
    series: 'Python 从零',
    tags: ['Python', '入门', '复习'],
    summary: 'chain/islice/groupby 先排序、product/permutations/combinations、accumulate 前缀累积；6 道新题。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero29.vue')
  },
  {
    slug: 'python-from-zero-30',
    title: '第 30 课：enum 枚举',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'Enum/IntEnum/StrEnum、name/value、反查与 auto()；用枚举替代魔法字符串，接近 Java enum。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero30.vue')
  },
  {
    slug: 'python-from-zero-31',
    title: '第 31 课：datetime 日期与时间',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'datetime/date/time、strftime 格式化、strptime 解析、timedelta 加减、比较与 .replace；配文件名时间戳与到期日练习。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero31.vue')
  },
  {
    slug: 'python-from-zero-32',
    title: '第 32 课：re 正则表达式',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'search/findall/fullmatch/sub、\\d/\\w/\\s、+/*、[..]/(..)、raw 字符串；抠数字、校验手机号与 IP。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonFromZero32.vue')
  },
  {
    slug: 'python-from-zero-33',
    title: '第 33 课：argparse 命令行参数',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'ArgumentParser、位置/可选参数、type/default、store_true、choices；用 parse_args(列表) 测 CLI，菜单升级成脚本入口。',
    updated: '2026-08-25',
    component: () => import('../../views/notes/articles/PythonFromZero33.vue')
  },
  {
    slug: 'python-from-zero-34',
    title: '第 34 课：logging 分级日志',
    series: 'Python 从零',
    tags: ['Python', '入门'],
    summary: 'DEBUG/INFO/WARNING/ERROR、getLogger、basicConfig、Handler+Formatter、ColorFormatter 上色；verbose 联动 argparse。',
    updated: '2026-08-25',
    component: () => import('../../views/notes/articles/PythonFromZero34.vue')
  },
  {
    slug: 'python-from-zero-35',
    title: '第 35 课：pytest 写断言',
    series: 'Python 从零',
    tags: ['Python', '入门', '测试'],
    summary: 'pip install pytest、test_ 命名、assert、raises、parametrize；给函数写可重复验证的测试。',
    updated: '2026-08-25',
    component: () => import('../../views/notes/articles/PythonFromZero35.vue')
  },
  {
    slug: 'python-from-zero-36',
    title: '第 36 课：HTTP 调用与暴露（标准库 vs 三方）',
    series: 'Python 从零',
    tags: ['Python', '入门', '网络'],
    summary: '标准库对照 + 主流 HTTP 三方全景（优劣/热度/生产建议）与各库最小教程；ThreadingHTTPServer 原理；基础课收官。',
    updated: '2026-08-26',
    component: () => import('../../views/notes/articles/PythonFromZero36.vue')
  },
  {
    slug: 'python-from-zero-37',
    title: '第 37 课：os 与配置读取（os.getenv / BaseSettings）',
    series: 'Python 从零',
    tags: ['Python', '入门', '配置'],
    summary: 'os 是什么、os.getenv / os.path 常用 API；手写配置的痛点 → pydantic-settings 的 BaseSettings：读 .env、类型转换校验、字段↔变量对应、优先级，配合 @lru_cache 全局唯一。',
    updated: '2026-08-26',
    component: () => import('../../views/notes/articles/PythonFromZero37.vue')
  },
  {
    slug: 'python-stdlib-map',
    title: 'Python 标准库地图：模块分级与学习顺序',
    series: 'Python 生态',
    tags: ['Python', '生态', '标准库'],
    summary: '内置 / 标准库 / PyPI 怎么分；★初学必学、◎常用、○以后；from-zero 进度与接下来先学哪 8 个。',
    updated: '2026-08-24',
    component: () => import('../../views/notes/articles/PythonStdlibMap.vue')
  }
]

export function getArticleBySlug (slug) {
  return noteArticles.find((a) => a.slug === slug) || null
}

export function listArticles ({ series } = {}) {
  if (!series) return noteArticles
  return noteArticles.filter((a) => a.series === series)
}

/** 从标题解析课次，如「第 3 课：…」→ 3 */
export function getLessonNumber (title) {
  const m = title.match(/第\s*(\d+)\s*课/)
  return m ? Number(m[1]) : null
}

/** 同系列内上一篇 / 下一篇 */
export function getAdjacentArticles (slug) {
  const article = getArticleBySlug(slug)
  if (!article) return { prev: null, next: null }
  const siblings = listArticles({ series: article.series })
  const idx = siblings.findIndex((a) => a.slug === slug)
  return {
    prev: idx > 0 ? siblings[idx - 1] : null,
    next: idx < siblings.length - 1 ? siblings[idx + 1] : null
  }
}

export const noteSeries = [
  { id: 'all', label: '📚 全部' },
  { id: 'Python 从零', label: '🐍 Python 从零' },
  { id: 'Python 生态', label: '🗺️ Python 生态' }
]
