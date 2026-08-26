<template>
  <div class="article">
    <p>
      程序不能永远走直线。真实场景里，要根据条件走不同分支：
      成年还是未成年、分数够不够及格、输入合不合法。
      这一课的核心就是 <code>if / elif / else</code>，以及比较运算符产出的
      <code>True</code> / <code>False</code>。
    </p>

    <h2>比较：问一个「是或否」的问题</h2>
    <p>
      一个等号 <code>=</code> 是赋值；两个等号 <code>==</code> 是比较。
      比较的结果永远是布尔值。
    </p>
<pre><code>print(3 &gt; 1)      # True
print(18 &gt;= 18)   # True
print(3 == 5)     # False
print(3 != 5)     # True（不等于）</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        写条件时把 <code>==</code> 写成 <code>=</code>，在 Python 里通常直接
        <code>SyntaxError</code>（if 后面不能赋值）。养成「条件里用双等号」的肌肉记忆。
      </p>
    </div>

    <h2>if / else：二选一</h2>
    <p>
      <code>if</code> 后面跟条件；为 <code>True</code> 时执行缩进块，否则走 <code>else</code>。
      Python 用缩进表示归属——少空、多空都会报错，这是语法的一部分，不是风格偏好。
    </p>
<pre><code>age = 20
if age &gt;= 18:
    print("成年")
else:
    print("未成年")</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        缩进块是「只在这个条件下执行」的一组语句。
        块外的代码无论条件真假都会继续跑——判断只影响分支，不截断整个程序。
      </p>
    </div>

    <h2>elif：多个分支，命中即停</h2>
    <p>
      <code>elif</code> 是 else if 的缩写：上面都不对，再试这个。
      从上往下检查，第一个为真的分支执行后，后面全部跳过。
    </p>
<pre><code>score = 85
if score &gt;= 90:
    print("优秀")
elif score &gt;= 60:
    print("及格")
else:
    print("不及格")</code></pre>
    <p>
      顺序很重要：若先写 <code>&gt;= 60</code> 再写 <code>&gt;= 90</code>，
      95 分会先被「及格」截住，永远到不了「优秀」。
    </p>

    <h2>在函数里判断并 return</h2>
    <p>
      把判断封进函数，调用方只关心结果。返回布尔或字符串都常见。
    </p>
<pre><code>def is_adult(age: int) -&gt; bool:
    return age &gt;= 18

def grade(score: int) -&gt; str:
    if score &gt;= 90:
        return "优秀"
    elif score &gt;= 60:
        return "及格"
    else:
        return "不及格"</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>return age &gt;= 18</code> 比写完整 if/else 返回 True/False 更短，语义相同。
        条件表达式本身就是布尔值，可以直接交回去。
      </p>
    </div>

    <h2>和 input 接起来</h2>
<pre><code>user_age = int(input("请输入年龄："))
if is_adult(user_age):
    print(f"{user_age} 岁，已经成年")
else:
    print(f"{user_age} 岁，还未成年")</code></pre>
    <p>
      记住第 2 课：先 <code>input</code>，再 <code>int</code>，再判断。
      转换失败会崩——第 8 课再用 <code>try/except</code> 接住。
    </p>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写 <code>abs_value(n)</code>：非负返回 n，否则返回 <code>-n</code>。</li>
      <li>用 input 读一个整数，调用上面的函数，f-string 打印绝对值。</li>
      <li>故意把 elif 的分数阈值顺序写反，观察 95 分会落在哪一档。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走三件事：比较产出真假；缩进划定分支；elif 从上到下命中即停。
      下一课进入列表与 <code>for</code>——一次处理「一排东西」。
    </p>
  </div>
</template>
