<template>
  <div class="article">
    <p>
      状态、等级、颜色常写成 <code>"pending"</code>、<code>"done"</code> 字符串——拼错要运行时才炸，IDE 也不补全。
      第 27 课 <code>Literal</code> 能在类型上约束「只能是几个值」；这一课用 <strong>enum</strong>
      在运行时建真正的枚举类，接近 Java 的 <code>enum</code>。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>有限固定取值 → 用 <code>class X(Enum)</code>，别散落魔法字符串</li>
      <li>要成员名 / 绑定值 → <code>.name</code> / <code>.value</code></li>
      <li>字符串来反查 → <code>Status("pending")</code>；按名 → <code>Status["PENDING"]</code></li>
      <li>要当 int / str 用 → <code>IntEnum</code> / <code>StrEnum</code></li>
    </ul>

    <h2>基本 Enum</h2>
<pre><code>from enum import Enum

class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"

Status.PENDING.name    # "PENDING"
Status.PENDING.value   # "pending"
Status.PENDING is Status.PENDING   # True（单例）</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>Status.PENDING == "pending"</code> 是 <strong>False</strong>——成员不是 str。
        要比字符串用 <code>.value</code>；成员之间用 <code>==</code> 或 <code>is</code>。
      </p>
    </div>

    <h2>反查与遍历</h2>
<pre><code>Status["PENDING"]      # 按成员名
Status("pending")      # 按 value（非法会 ValueError）

[m.name for m in Status]    # 所有成员名</code></pre>

    <h2>auto / IntEnum / StrEnum</h2>
<pre><code>from enum import auto, IntEnum, StrEnum

class Priority(Enum):
    LOW = auto()      # 1, 2, 3 … 自动递增

class HttpCode(IntEnum):
    OK = 200
HttpCode.OK == 200    # True，可当 int

class Color(StrEnum):
    RED = "red"
Color.RED == "red"    # True，可当 str 拼接</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">和 Literal 的区别</span>
      <p>
        <code>Literal["a","b"]</code>：类型检查器用，运行时仍是普通 str。
        <code>Enum</code>：运行时真类，能迭代、反查、挂方法。API 边界常 enum 定义值，参数标注
        <code>Status</code> 或 <code>Literal</code> 视团队习惯。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>30_enum.py</code>，对照输出。</li>
      <li>再打开 <code>30_enum_exercise.py</code>，6 题：订单状态、反查、IntEnum、StrEnum、auto。</li>
      <li>题 1 先定义 <code>OrderStatus</code> 成员，后面几题复用。</li>
    </ol>

    <h2>收束</h2>
    <p>
      enum 的核心：把「就这几个取值」收成类，补全、防拼错、可读性都比裸字符串强。
      下一课可以继续 functools 进阶、logging，或做一个 18~30 的小复习——你哪块虚就补哪块。
    </p>
  </div>
</template>
