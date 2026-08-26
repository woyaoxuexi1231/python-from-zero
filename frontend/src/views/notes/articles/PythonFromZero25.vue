<template>
  <div class="article">
    <p>
      前面很多课都在手写循环、分组、计数。标准库
      <code>collections</code> 和 <code>itertools</code> 把这些高频模式打包好了——
      <strong>不用造轮子</strong>，但要会认工具、会组合。
      这一课不追求背完 API，而是建立「看到这类需求，知道去哪个抽屉找」的直觉。
    </p>

    <h2>三种推导式：list / dict / set</h2>
    <p>
      第 14 课学过列表推导。同一套写法也能造字典和集合：
      方括号是列表，花括号里写 <code>键: 值</code> 是字典，花括号里只写元素是集合。
    </p>
<pre><code>lst = [i * 2 for i in range(5)]             # [0, 2, 4, 6, 8]
dct = {c: i for i, c in enumerate("abc")}   # {'a': 0, 'b': 1, 'c': 2}
st  = {x % 3 for x in range(10)}            # {0, 1, 2} —— 自动去重</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        推导式本质仍是「遍历 → 变换 / 过滤 → 收集」，只是写成表达式。
        集合推导天然去重；字典推导后写的同名键会覆盖先写的。
      </p>
    </div>

    <h2>defaultdict：缺键自动造默认值</h2>
    <p>
      普通 <code>bucket = {}</code> 和 <code>defaultdict(list)</code> 都能存键值对，
      差别只在一件事：<strong>读一个还不存在的键时，怎么办？</strong>
    </p>

    <h3>普通 dict：缺键就 KeyError</h3>
<pre><code>bucket = {}
for w in ["apple", "banana", "apple"]:
    bucket[w].append(w)   # 第一次碰到 "apple" → KeyError</code></pre>
    <p>
      因为 <code>bucket["apple"]</code> 还不存在，没法 <code>.append</code>。
      你得先自己准备好空列表，常见写法是：
    </p>
<pre><code>bucket = {}
for w in ["apple", "banana", "apple"]:
    if w not in bucket:
        bucket[w] = []      # 缺键时手动造一个空 list
    bucket[w].append(w)

# 或者写成一行：
# bucket.setdefault(w, []).append(w)</code></pre>

    <h3>defaultdict：缺键时自动调用工厂</h3>
<pre><code>from collections import defaultdict

bucket = defaultdict(list)   # 缺键时自动执行 list()，得到 []
for w in ["apple", "banana", "apple"]:
    bucket[w].append(w)
# bucket["apple"] → ['apple', 'apple']，不会 KeyError</code></pre>
    <p>
      <code>defaultdict(list)</code> 等于把上面那段 <code>if w not in bucket</code> 自动化了：
      第一次访问 <code>bucket[w]</code> 时，内部先 <code>bucket[w] = list()</code>，再把这个列表给你用。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        两者最终结构可以一样（都是「单词 → 列表」），不是两种不同的数据结构。
        <code>defaultdict</code> 是 dict 的子类，只是改了「缺键时的行为」：
        普通 dict 抛 <code>KeyError</code>；defaultdict 调用你传入的工厂，造默认值再塞进去。
      </p>
    </div>

    <p>
      常用工厂：<code>list</code>（分组）、<code>set</code>（去重收集）、
      <code>int</code>（默认 0，适合计数）。
      分组统计时，往往比手写 <code>if key not in d</code> 更干净。
    </p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>defaultdict(list)</code> 里的 <code>list</code> 是工厂函数本身，不是 <code>list()</code>。
        写成 <code>defaultdict(list())</code> 会立刻造一个空列表当「工厂」，类型不对，直接报错。
        另外：只是「查一下有没有」也尽量用 <code>key in bucket</code>，
        因为 <code>bucket[key]</code> 在 defaultdict 里会<strong>顺便创建</strong>缺键，可能弄脏字典。
      </p>
    </div>

    <h2>Counter：一键计数</h2>
<pre><code>from collections import Counter

cnt = Counter("abracadabra")
print(dict(cnt))           # {'a': 5, 'b': 2, 'r': 2, ...}
print(cnt.most_common(2))  # [('a', 5), ('b', 2)]</code></pre>
    <p>
      传入任意可迭代对象即可计数。
      日志里找 Top N、词频统计、字符出现次数，几乎第一反应就是它。
    </p>

    <h2>namedtuple：带字段名的轻量元组</h2>
<pre><code>from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p[0])   # 3 3 —— 名字和下标都能用
x, y = p           # 还能像元组一样解包</code></pre>
    <p>
      不可变、轻量、能解包。字段少、不需要改、不需要方法时很合适。
      下一课 dataclass 是它的「可变、默认可控」升级版。
    </p>

    <h2>itertools：处理迭代器的工具箱</h2>
    <p>
      先建立直觉：这些函数大多返回<strong>迭代器</strong>（惰性，用到才算），
      不是立刻造出完整列表。想立刻看结果，外面套 <code>list(...)</code>；
      数据很大时，尽量直接 <code>for</code> 消费，别全展开。
    </p>
<pre><code>import itertools</code></pre>

    <h3>chain：把多段数据首尾相连</h3>
    <p>
      你有几个列表（或任意可迭代对象），想当成<strong>一条流</strong>挨个处理，
      又不想先 <code>a + b + c</code> 拼出大列表占内存——用 <code>chain</code>。
    </p>
<pre><code>list(itertools.chain([1, 2], [3], [4, 5]))
# → [1, 2, 3, 4, 5]

# 等价于手写：
# for part in ([1, 2], [3], [4, 5]):
#     for x in part:
#         ...</code></pre>
    <p>
      典型场景：多个日志文件各读出一批行，想统一过滤；
      或「本页结果 + 缓存结果」合成一次遍历。
    </p>

    <h3>count：从某数开始，一直往上加</h3>
<pre><code>itertools.count(10)        # 10, 11, 12, 13, ... 永不结束
itertools.count(0, 2)      # 0, 2, 4, 6, ...  步长 2</code></pre>
    <p>
      接近「无限版的 <code>range</code>」。自己写就是 <code>while True: yield n; n += 1</code>。
      单独 <code>list(count())</code> 会卡死——必须配合下面的 <code>islice</code>，或自己在循环里 <code>break</code>。
    </p>

    <h3>cycle：把一段内容无限循环播放</h3>
<pre><code>itertools.cycle("AB")      # A, B, A, B, A, B, ... 永不结束
itertools.cycle([0, 1])    # 0, 1, 0, 1, ...</code></pre>
    <p>
      典型场景：轮询分配（任务轮流给 worker A/B/C）、
      交替取色、模拟「转圈」的状态。同样是无限的，要截断。
    </p>

    <h3>islice：只取迭代器的前几段</h3>
    <p>
      名字来自 slice（切片）。对<strong>任意</strong>可迭代对象，取「从哪到哪」，
      重点是<strong>截断无限流</strong>，而不是替代列表切片的全部功能。
    </p>
<pre><code># islice(可迭代, stop)           → 前 stop 个
# islice(可迭代, start, stop)    → 下标 start 到 stop 之前
# islice(可迭代, start, stop, step)

list(itertools.islice(itertools.count(10), 5))
# → [10, 11, 12, 13, 14]

list(itertools.islice(itertools.cycle("AB"), 6))
# → ['A', 'B', 'A', 'B', 'A', 'B']

list(itertools.islice(range(100), 2, 10, 3))
# → [2, 5, 8]   从 2 开始，到 10 之前，步长 3</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>count</code> / <code>cycle</code> 负责「源源不断产出」；
        <code>islice</code> 负责「我只要这么多」。
        组合起来：惰性生成 + 有限消费，中间不会把无限序列整份存进内存。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        千万别写 <code>list(itertools.count())</code> 或 <code>list(itertools.cycle(...))</code>
        而不设上限——会一直吃内存直到崩。
        永远先想清楚「我只要前多少个」。
      </p>
    </div>

    <h3>accumulate：一路往前累加（或累积）</h3>
<pre><code>list(itertools.accumulate([1, 2, 3, 4]))
# → [1, 3, 6, 10]
# 含义：1；1+2；1+2+3；1+2+3+4

list(itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b))
# → [1, 2, 6, 24]   前缀积

list(itertools.accumulate([5, 1, 8, 3], max))
# → [5, 5, 8, 8]   到目前为止的最大值</code></pre>
    <p>
      默认是加法前缀和；第二个参数可以换任意「二元函数」：
      乘积、取 max/min、自定义合并。
      场景：每日余额流水 → 累计余额；成绩列表 → 到目前最高分。
    </p>

    <h2>groupby：只认「连续相邻」的相同元素</h2>
    <p>
      名字像 SQL 的 GROUP BY，但行为更窄：
      <strong>只把挨在一起、且 key 相同的元素归成一组</strong>。中间被别的值隔开，就会拆成多组。
    </p>
<pre><code>data = ["a", "a", "b", "b", "b", "a"]
for key, group in itertools.groupby(data):
    print(key, list(group))
# a ['a', 'a']
# b ['b', 'b', 'b']
# a ['a']          ← 两段 a 不会合并</code></pre>
    <p>想「真正按字段分组」（同班的人凑一起），先排序再 groupby：</p>
<pre><code>rows = [("A", 80), ("B", 70), ("A", 95), ("B", 88)]
rows = sorted(rows, key=lambda r: r[0])   # 先按班级排好，同班才会相邻
for cls, group in itertools.groupby(rows, key=lambda r: r[0]):
    scores = [score for _, score in group]
    print(cls, scores)
# A [80, 95]
# B [70, 88]</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>group</code> 本身是迭代器，而且和 <code>groupby</code> 共用底层游标——
        循环里若不用 <code>list(group)</code> 立刻吃掉，下一轮开始后上一组就空了。
        需要保留分组结果时，马上转成 list。
      </p>
    </div>

    <h2>排列组合：product / permutations / combinations</h2>
    <p>三个都用来「枚举可能性」。差别在：能不能重复、要不要在乎顺序。</p>

    <h3>product：笛卡尔积（可重复）</h3>
<pre><code># 每个位置都从 "AB" 里选，长度 2 → 2×2 = 4 种
["".join(t) for t in itertools.product("AB", repeat=2)]
# → ['AA', 'AB', 'BA', 'BB']

# 也可以多个来源：
list(itertools.product([1, 2], ["x", "y"]))
# → [(1, 'x'), (1, 'y'), (2, 'x'), (2, 'y')]</code></pre>
    <p>场景：小字符集生成全部密码串、嵌套 for 的扁平写法、测试用例笛卡尔展开。</p>

    <h3>permutations：排列（有序、元素不重复）</h3>
<pre><code>list(itertools.permutations("ABC", 2))
# → [('A','B'), ('A','C'), ('B','A'), ('B','C'), ('C','A'), ('C','B')]
# AB 和 BA 算两种；没有 AA（不会重复使用同一位置的元素）</code></pre>
    <p>场景：赛程排座次、从 n 个人里抽 k 个排顺序。</p>

    <h3>combinations：组合（无序、元素不重复）</h3>
<pre><code>list(itertools.combinations("ABC", 2))
# → [('A','B'), ('A','C'), ('B','C')]
# AB 有，BA 没有——顺序不算新组合</code></pre>
    <p>场景：从题库抽两道题、两人配对（A-B 和 B-A 同一对）。</p>

    <div class="callout callout--principle">
      <span class="callout__label">怎么选</span>
      <p>
        要不要顺序？要 → <code>permutations</code>；不要 → <code>combinations</code>。
        能不能重复用同一字符？要重复 → <code>product</code>。
        规模会爆炸：<code>"abc"</code> 长度 3 的 product 就有 27 种；字符集再大先用小例子验证。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 <code>defaultdict(set)</code> 建「单词 → 行号列表」倒排索引（行号要去重、排序）。</li>
      <li>用 <code>Counter</code> 找一段文本里出现最多的词。</li>
      <li>用 <code>islice</code> 从一个无限生成器只取前 N 个；对照 <code>count</code> / <code>cycle</code> 体会截断。</li>
      <li>用 <code>product</code> 生成长度为 k 的全部串；做完配课 exercise 自检。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走一张小抄：<code>defaultdict</code> 分组、<code>Counter</code> 计数、
      <code>namedtuple</code> 轻量记录；
      <code>chain</code> 串流、<code>count/cycle + islice</code> 有限消费无限源、
      <code>accumulate</code> 前缀累积、<code>groupby</code> 相邻分组、
      <code>product/permutations/combinations</code> 枚举。
      下一课 dataclass：给「主要是数据」的类少写样板代码。
    </p>
  </div>
</template>
