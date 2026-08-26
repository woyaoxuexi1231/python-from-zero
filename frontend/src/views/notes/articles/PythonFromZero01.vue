<template>
  <div class="article">
    <p>
      学 Python 的第一站，不是背语法表，而是建立几个直觉：
      <strong>程序怎么跑</strong>、<strong>值怎么存</strong>、<strong>类型是什么意思</strong>、
      <strong>函数到底帮你省了什么事</strong>。
      下面按这个顺序展开；例子都是独立写的，方便你边读边在交互环境里试。
    </p>

    <h2>程序是什么：从上往下执行的一串指令</h2>
    <p>
      你写的 <code>.py</code> 文件，本质是一份「说明书」。
      解释器打开它，从第一行读到最后一行：遇到赋值就记住，遇到函数调用就去干那件事。
      没有隐藏的魔法步骤——你看到的顺序，几乎就是它执行的顺序。
    </p>
    <p>
      入门阶段建议用两种方式练手：把代码存成文件再 <code>python xxx.py</code>；
      或者开 REPL（终端输入 <code>python</code>）一行一行试。
      文件适合保存完整思路，REPL 适合立刻验证「这句话到底会怎样」。
    </p>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        文件编码请用 UTF-8。在中文 Windows 上若用系统默认编码存盘，
        含中文的源码可能乱码，甚至直接 <code>SyntaxError</code>。
        跑含中文输出时，也可设环境变量 <code>PYTHONUTF8=1</code>，避免控制台编码打架。
      </p>
    </div>

    <h2>print：让计算机「开口说话」</h2>
    <p>
      <code>print</code> 是内置函数，作用很朴素：把东西写到标准输出（一般是终端）。
      初学时它几乎是你唯一的「眼睛」——看不见变量里有什么，就 print 出来看。
    </p>
<pre><code>print("hello")
print(1 + 2)
print("score:", 95)</code></pre>
    <p>
      字符串要用引号包起来。单引号、双引号在 Python 里等价；
      习惯上外层用哪种都可以，团队统一即可。
      多个参数写在同一个 <code>print</code> 里时，默认用空格隔开再输出。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>print</code> 不会「改变」你传进去的值，它只是把值的可读形式写出去。
        真正参与计算的，是你传进去之前的表达式；print 只是旁观记录员。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>print(你好)</code> 没有引号时，Python 会当成「去找名叫 你好 的变量」。
        找不到就 <code>NameError</code>。想输出文字，加引号；想输出变量，写变量名。
      </p>
    </div>

    <h2>变量：给值贴标签，不是「盒子里永远装着同一种东西」</h2>
    <p>
      很多教材说「变量是盒子」。这个比喻入门够用，但 Python 里更准确的说法是：
      <strong>名字指向对象</strong>。等号是赋值，读作「让左边这个名字，指向右边这个值」。
    </p>
<pre><code>title = "学习笔记"
count = 3
price = 19.9
ready = True

print(title)
count = count + 1   # 名字还叫 count，但指向了新的整数 4
print(count)</code></pre>
    <p>
      名字可以重新赋值。旧对象如果没人再引用，之后会被回收——你暂时不用管回收细节，
      只要知道：<strong>改的是「名字指向谁」，不是「盒子里的类型永远锁死」</strong>。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>=</code> 不是数学相等。判断相等用 <code>==</code>（后面课会用到）。
        现在先养成口癖：看到 <code>a = b</code> 就想「a 现在指向 b 那个值」。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        布尔字面量是 <code>True</code> / <code>False</code>（首字母大写）。
        写成 <code>true</code>、<code>TRUE</code> 都会 <code>NameError</code>。
        从 JavaScript / Java 转过来的人最容易在这里栽跟头。
      </p>
    </div>

    <h2>类型：值的「品种」，决定你能对它做什么</h2>
    <p>第一阶段先把四种基本类型吃熟：</p>
    <ul>
      <li><code>str</code>：文本，如 <code>"hi"</code></li>
      <li><code>int</code>：整数，如 <code>18</code></li>
      <li><code>float</code>：浮点数，如 <code>1.75</code></li>
      <li><code>bool</code>：真假，如 <code>True</code> / <code>False</code></li>
    </ul>
    <p>
      用 <code>type(x)</code> 可以问「这个值是什么类型」。
      它返回的是类对象，打印出来长得像 <code>&lt;class 'str'&gt;</code>。
    </p>
<pre><code>print(type("18"))   # str
print(type(18))     # int
print(type(18.0))   # float</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        Python 是<strong>动态类型、强类型</strong>（日常说法）：
        变量名不绑死类型，但运算时类型不对会明确报错，而不是悄悄乱转。
        例如 <code>"3" + 1</code> 会 <code>TypeError</code>，不会偷偷变成 <code>4</code> 或 <code>"31"</code>
        （后者要用显式转换，下一课再细讲）。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>"18"</code> 和 <code>18</code> 看起来像，其实完全不同。
        前者能拼接、切片；后者能加减乘除。
        输入、文件读进来的内容，几乎永远是字符串——所以「看起来像数字」不等于「是数字」。
      </p>
    </div>

    <p>
      再多想一步：<code>bool</code> 其实和「条件判断」绑在一起。
      之后写 <code>if</code> 时，你会发现很多值可以当成「真/假」来用
      （空字符串、0、<code>None</code> 等偏「假」）。现在先记住字面量怎么写就够。
    </p>

    <h2>函数：把「可复用的一小段意图」起个名字</h2>
    <p>
      函数解决的是重复与结构问题：同一套步骤会做很多次，或希望代码读起来像自然语言。
      <code>def</code> 定义，括号里是参数（输入），<code>return</code> 把结果交回调用方。
    </p>
<pre><code>def add(a, b):
    return a + b

print(add(3, 5))
total = add(10, 20)
print(total)</code></pre>

    <h3>定义 ≠ 执行</h3>
    <p>
      解释器读到 <code>def add(...):</code> 时，主要是<strong>登记</strong>：记住有个叫 add 的工具。
      真正算加法，要等到你写下 <code>add(3, 5)</code>——这叫<strong>调用</strong>。
      初学者常把「写完函数」当成「已经算过了」，其实还没跑。
    </p>

    <h3>return 和 print 不是一回事</h3>
    <ul>
      <li><code>print</code>：给人看（副作用：输出到屏幕）</li>
      <li><code>return</code>：给程序看（把值交回调用处，继续参与计算）</li>
    </ul>
<pre><code>def bad_add(a, b):
    print(a + b)      # 只显示，调用方拿不到结果

def good_add(a, b):
    return a + b      # 调用方可以接着用

x = good_add(2, 3)
print(x * 10)         # 50</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        调用函数时，实参的值绑定到形参名上，函数体跑完后局部名字通常就结束使命。
        <code>return</code> 既结束函数，又带走一个值。
        没有 <code>return</code> 时，Python 默认返回 <code>None</code>（表示「没有有意义的结果」）。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        算完忘了 <code>return</code>：函数里明明算过，外面却是 <code>None</code>。
        另一个坑：<code>print(greet())</code>——若 <code>greet</code> 自己已经 print 过且没有 return，
        你会先看到问候，再看到多出来的一行 <code>None</code>。
      </p>
    </div>

    <h2>类型标注：写给人看的说明书，不是运行时警察</h2>
    <p>
      你可能见过 <code>def add(a: int, b: int) -&gt; int:</code> 这种写法。
      冒号后面的类型、<code>-&gt;</code> 后面的返回类型，叫<strong>类型标注</strong>。
    </p>
<pre><code>def add(a: int, b: int) -&gt; int:
    return a + b

def greet(name: str) -&gt; None:
    print("你好，" + name)</code></pre>
    <p>
      它们主要帮编辑器、静态检查工具和读者理解意图。
      <strong>CPython 默认不会在运行时因为类型标注不符就拒绝执行</strong>——
      你仍可能把字符串传进标注为 int 的参数（当然结果可能报错或很怪）。
      入门阶段：标注是加分项，不是能不能跑的前提。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        把标注想成注释的升级版：结构化、可被工具读取。
        真正的「强制类型」要靠额外工具（如类型检查器）或运行时校验库，那是后话。
      </p>
    </div>

    <h2>字符串拼接的一点预告</h2>
    <p>
      <code>"你好，" + name</code> 要求两边都是字符串。
      若 <code>name</code> 是数字，会 <code>TypeError</code>。
      以后你会更常用 f-string（如 <code>f"你好，{name}"</code>），可读性更好；
      这堂课先建立「类型要匹配」的意识即可。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>在 REPL 里分别 print 字符串、整数、表达式，观察差别。</li>
      <li>写一个变量，print 它，再重新赋值，再 print——体会「名字换指向」。</li>
      <li>写 <code>multiply(a, b)</code>，返回乘积；调用 <code>multiply(6, 7)</code> 应得到 42。</li>
      <li>故意写一个只 <code>print</code> 不 <code>return</code> 的函数，外面再用变量接返回值，看看会怎样。</li>
    </ol>

    <h2>收束</h2>
    <p>
      这一课你要带走的不是某几行固定代码，而是四个习惯：
      用 print 验证假设；用变量管理值；用类型理解能做什么；用函数打包意图并用 return 交结果。
      下一站通常会进入「字符串与输入」：用户敲进来的永远是文本，
      以及如何把它变成数字——那是真实程序里更常见的战场。
    </p>
  </div>
</template>
