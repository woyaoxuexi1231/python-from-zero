<template>
  <div class="article">
    <p>
      第一课你学会了变量、类型和函数。真实程序里，数据往往来自<strong>用户输入</strong>或<strong>文件</strong>——
      而它们几乎总是以<strong>字符串</strong>的形式出现。
      这一课解决三件事：怎么拼字符串、怎么读输入、怎么在「文本」和「数字」之间安全转换。
    </p>

    <h2>字符串拼接：<code>+</code> 的含义取决于类型</h2>
    <p>
      两个字符串可以用 <code>+</code> 拼在一起，这叫<strong>拼接</strong>，不是数学加法。
      两个数字用 <code>+</code> 才是加法。同一个符号，操作数类型不同，行为就不同。
    </p>
<pre><code>first = "hu"
last = "lei"
full = first + last
print(full)   # hulei</code></pre>
    <p>
      变量里存的是字符串，<code>+</code> 就按字符串规则走。
      变量里存的是整数，<code>+</code> 就按算术规则走。
      第一课说的「类型决定你能做什么」，在这里第一次真正派上用场。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        Python 是强类型语言：<code>+</code> 不会偷偷把字符串和数字混算。
        左边是 <code>str</code>、右边是 <code>int</code>，直接 <code>+</code> 会 <code>TypeError</code>——
        这是保护，不是刁难。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>print("年龄是" + 18)</code> 会报错。
        想输出「年龄是18」，要么把数字转成字符串：<code>"年龄是" + str(18)</code>，
        要么用下面要说的 f-string。
      </p>
    </div>

    <h2>显式转换：<code>str()</code>、<code>int()</code>、<code>float()</code></h2>
    <p>
      类型不对时，不要指望 Python 猜你的意图——<strong>自己转</strong>。
      三个最常用的转换函数：
    </p>
    <ul>
      <li><code>str(x)</code>：任意值 → 字符串（拼进句子时用）</li>
      <li><code>int(s)</code>：看起来像整数的字符串 → 整数（做加减乘除时用）</li>
      <li><code>float(s)</code>：看起来像小数的字符串 → 浮点数</li>
    </ul>
<pre><code>age = 18
print("年龄是" + str(age))   # 数字 → 字符串，再拼接

age_text = "18"
age_number = int(age_text)   # 字符串 → 整数，再计算
print(age_number + 1)        # 19</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>int("18.5")</code> 会 <code>ValueError</code>——带小数点要用 <code>float()</code>。
        <code>int("hello")</code> 也会 <code>ValueError</code>——内容根本不是数字。
        用户输入不可信，后面第 8 课会用 <code>try/except</code> 优雅处理；现在先知道「转失败会报错」。
      </p>
    </div>

    <h2>f-string：现在写 Python 最顺手的拼串方式</h2>
    <p>
      在字符串前加 <code>f</code>，花括号里写变量或表达式，Python 会把值嵌进去。
      比一堆 <code>+</code> 和 <code>str()</code> 可读得多，也是日常代码里的默认选择。
    </p>
<pre><code>name = "hulei"
age = 18
print(f"我叫{name}，今年{age}岁")
print(f"明年 {age + 1} 岁")   # 花括号里可以写表达式</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        f-string 在运行时求值花括号里的表达式，再转成字符串嵌进去。
        所以 <code>f"{age + 1}"</code> 会先算加法，再显示——类型对了，表达式随便写。
      </p>
    </div>

    <p>
      第一课预告过 <code>"你好，" + name</code> 要求两边都是字符串；
      f-string 里数字可以直接写进 <code>{age}</code>，不必手动 <code>str()</code>。
      两种写法都对，新代码优先 f-string。
    </p>

    <h2><code>input()</code>：程序第一次「听你说」</h2>
    <p>
      <code>input("提示语")</code> 会暂停程序，在终端显示提示，等你打字并按回车。
      你输入的内容，作为<strong>字符串</strong>返回给程序。
    </p>
<pre><code>user_name = input("请输入你的名字：")
print(f"你好，{user_name}")
print(type(user_name))   # &lt;class 'str'&gt;</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <strong>无论你敲的是 18 还是 hello，<code>input()</code> 返回的永远是 <code>str</code>。</strong>
        这是整课最重要的记忆点之一。
        看起来像数字 ≠ 是数字；要参与运算，必须 <code>int()</code> 或 <code>float()</code>。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>age = input("年龄：")</code> 之后写 <code>age + 1</code> 会 <code>TypeError</code>——
        你在给字符串做加法，不是给整数。
        正确顺序：先 <code>input</code>，再 <code>int(...)</code>，再计算。
      </p>
    </div>

    <h2>把输入和函数接起来</h2>
    <p>
      第一课学的函数，在这一课开始真正干活：读入 → 转换 → 交给函数 → 输出。
    </p>
<pre><code>def next_year(current_age: int) -> int:
    return current_age + 1

age_text = input("请输入你的年龄：")
age_number = int(age_text)
print(f"明年你 {next_year(age_number)} 岁")</code></pre>
    <p>
      注意数据流：<code>input</code> 产出字符串 → <code>int</code> 产出整数 →
      <code>next_year</code> 接收整数、返回整数 → f-string 负责展示。
      每一步类型清晰，程序就不容易乱。
    </p>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        类型标注（如 <code>current_age: int</code>）在这里特别有用：
        它提醒读者「这个函数期望整数，别传字符串进来」。
        运行时 Python 仍不会自动帮你检查，但你自己会在调用前做好 <code>int()</code> 转换。
      </p>
    </div>

    <h2>一条完整的小练习思路</h2>
    <p>配课文件里的练习可以概括成四步：</p>
    <ol>
      <li><code>input</code> 读一个「数字」（其实是字符串）</li>
      <li>写 <code>double(n: int) -&gt; int</code>，返回两倍</li>
      <li><code>int(...)</code> 把输入转成整数</li>
      <li>用 f-string 打印：你输入的是 X，两倍是 Y</li>
    </ol>
<pre><code>my_num = input("请输入一个数字：")
my_num_int = int(my_num)

def double(n: int) -> int:
    return n * 2

print(f"你输入的数字是 {my_num}，两倍是 {double(my_num_int)}")</code></pre>
    <p>
      这里 <code>my_num</code> 和 <code>my_num_int</code> 可以同名覆盖（<code>my_num = int(my_num)</code>），
      但分开两个名字，调试时更容易看清「转换前 / 转换后」——初学阶段这样写更清楚。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>用 <code>+</code> 和 f-string 各写一遍同一句自我介绍，体会可读性差别。</li>
      <li><code>input</code> 读年龄，分别用 <code>int</code> 和 <code>float</code> 转换，试试输入 <code>18.5</code> 时谁成功、谁报错。</li>
      <li>写 <code>greet(name: str) -&gt; str</code>，返回 <code>f"你好，{name}"</code>，再和 <code>input</code> 联用。</li>
      <li>故意对 <code>input</code> 的结果不算 <code>int</code> 就传给需要整数的函数，观察 <code>TypeError</code> 报什么。</li>
    </ol>

    <h2>收束</h2>
    <p>
      这一课的核心就一句：<strong>外界进来的数据，先当字符串；要算数，显式转；要展示，f-string 最省心。</strong>
      下一课进入 <code>if / else</code>——程序可以根据条件走不同分支，
      比如「年龄是否成年」「输入是否为空」。判断逻辑，是写交互程序的真正起点。
    </p>
  </div>
</template>
