<template>
  <div class="article">
    <p>
      第 25 课 <code>namedtuple</code> 给元组起了字段名，但不可变、默认值写法受限。
      <code>@dataclass</code> 是更现代的「数据类」：少写
      <code>__init__</code> / <code>__repr__</code> / <code>__eq__</code>，
      还能加默认值、校验、排序。接近 Java 的 <code>record</code> 或 Lombok <code>@Data</code>。
    </p>

    <h2>最简用法：让装饰器生成样板</h2>
<pre><code>from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(3, 4)
print(p)                 # Point(x=3, y=4)
print(p == Point(3, 4))  # True</code></pre>
    <p>
      你只声明字段；装饰器根据注解自动生成构造、打印、相等比较。
      精力放在「有哪些字段、字段什么意思」，而不是抄样板代码。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>@dataclass</code> 是装饰器（第 23 课）：接收类，返回「补全了方法」的类。
        运行时仍然是普通 class，没有魔法类型；只是省了你手写那几段固定代码。
      </p>
    </div>

    <h2>默认值与 field：配方 vs 已经造好的东西</h2>
    <p>
      不可变默认值可以直接写：<code>y: int = 0</code>。
      可变类型（list / dict / set）不行——默认值表达式在<strong>定义类时只算一次</strong>，
      所有实例会共用同一个对象。
    </p>
<pre><code># 错误：所有实例共用同一个 []
# tags: list[str] = []

from dataclasses import dataclass, field

@dataclass
class Article:
    title: str
    tags: list[str] = field(default_factory=list)</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        Python 的默认值存的是「已经造好的对象」的引用，不是「每次新建的配方」。
        所以 <code>= []</code> 只执行一次；<code>field(default_factory=list)</code>
        才是配方——每次缺省时调用 <code>list()</code>，每个实例拿到新列表。
        这和第 13 课「函数默认参数别用 <code>[]</code>」是同一类陷阱。
      </p>
    </div>

    <p><code>field</code> 本身不是字段，而是<strong>给字段写配置</strong>的工具。常用参数：</p>
    <ul>
      <li><code>default=...</code>：固定默认值（适合 int / str / None）</li>
      <li><code>default_factory=list</code>：每次缺省时调用工厂造新值</li>
      <li><code>init=False</code>：不进构造参数</li>
      <li><code>compare=False</code>：不参与 <code>==</code> / 排序</li>
    </ul>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        写成 <code>field(default_factory=list())</code> 也不对——
        括号会立刻调用，传进去的是空列表，不是工厂函数。
        正确是传 <code>list</code> 本身。
      </p>
    </div>

    <h2>frozen=True：不可变，能当 dict 的键</h2>
<pre><code>@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

palette = {Color(255, 0, 0): "红色"}
# palette[Color(255, 0, 0)] → "红色"</code></pre>
    <p>
      冻结后不能改字段；因为可哈希，可以放进 set、当 dict 键——
      语义接近 namedtuple 的不可变，但写法仍是 dataclass。
    </p>

    <h2>order=True：排序与比较</h2>
<pre><code>@dataclass(order=True)
class Student:
    score: int
    name: str = field(compare=False)   # 只比 score，不比 name

sorted([Student(85, "小明"), Student(92, "hulei"), Student(78, "小红")])</code></pre>
    <p>按字段声明顺序依次比较；用 <code>compare=False</code> 排除不想参与比较的字段。</p>

    <h2>__post_init__：构造后校验或算派生字段</h2>
<pre><code>@dataclass
class Rect:
    width: int
    height: int
    area: int = field(init=False)

    def __post_init__(self):
        if self.width &lt;= 0 or self.height &lt;= 0:
            raise ValueError("宽和高必须为正")
        self.area = self.width * self.height</code></pre>
    <p>
      <code>__init__</code> 由 dataclass 自动生成；
      <code>__post_init__</code> 在它跑完之后执行。
      适合「字段都赋好了，再检查合法性或补算 area」。
      <code>field(init=False)</code> 表示该字段不进构造参数。
    </p>

    <h2>asdict / astuple：转字典和元组</h2>
<pre><code>from dataclasses import asdict, astuple

@dataclass
class User:
    name: str
    age: int

u = User("hulei", 18)
asdict(u)    # {'name': 'hulei', 'age': 18}
astuple(u)   # ('hulei', 18)</code></pre>
    <p>配合 <code>json.dump</code> 序列化时很常用；比手写字典转换省事。</p>

    <h2>和 namedtuple / 普通 class 怎么选</h2>
    <ul>
      <li><strong>namedtuple</strong>：轻量、不可变、字段少、不需要方法</li>
      <li><strong>dataclass</strong>：需要默认值、可变、校验、方法、排序——日常首选</li>
      <li><strong>普通 class</strong>：行为复杂、继承体系重、不只是「存数据」时用</li>
    </ul>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 frozen 坐标类，当 dict 键存棋盘颜色。</li>
      <li>写带 <code>default_factory</code> 的 Todo，验证两个实例的 tags 不会串。</li>
      <li>在 <code>__post_init__</code> 里校验邮箱必须含 <code>@</code>。</li>
      <li>用 <code>asdict</code> 把一批 User 转成 <code>list[dict]</code>；做完配课 exercise 自检。</li>
    </ol>

    <h2>收束</h2>
    <p>
      dataclass 让你把精力放在字段含义和业务逻辑，而不是重复写构造和比较。
      记住一句就够：可变默认值用 <code>default_factory</code>，不要写 <code>= []</code>。
      下一课 typing：把「可能没有、多种类型、固定几个值」写进类型标注。
    </p>
  </div>
</template>
