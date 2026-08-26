<template>
  <div class="article">
    <p>
      菜单能转圈了，但选「新增分数」时若输入 <code>abc</code>，
      <code>int("abc")</code> 会直接崩溃，整个程序消失。
      这一课只干一件事：把会崩的那一行包起来，失败就提示，然后继续跑。
    </p>

    <h2>哪些操作会崩</h2>
<pre><code>print(int("18"))   # 正常
# int("abc")       # ValueError：值不对</code></pre>
    <p>不处理的话，报错处之后的代码都不会执行——菜单也一起没了。</p>

    <h2>try / except</h2>
<pre><code>try:
    print(int("abc"))
except ValueError:
    print("这不是整数")

print("程序还在跑")  # 会打印</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>try</code> 里放可能出错的代码；出错就跳到对应类型的 <code>except</code>，不崩。
        成功则 except 不执行。同一结构换合法输入，就只走 try。
      </p>
    </div>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        不要写裸 <code>except:</code>——会把所有错误（包括你自己的 bug）都吃掉，调试极痛苦。
        现在记住：<code>int()</code> 转失败 → <code>ValueError</code>。
      </p>
    </div>

    <h2>接到成绩本的 add_one</h2>
    <p>两种常见策略：失败就 return 回菜单；或循环直到输对。</p>
<pre><code>def add_one() -&gt; None:
    name = input("新增/修改谁？")
    while True:
        try:
            score = int(input("分数是多少？"))
            break
        except ValueError:
            print("请输入整数")
    add_score(scores, name, score)
    print(f"已保存：{name} = {score}")</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        这是第 7 课 while + 第 8 课 try 的组合：
        菜单本身就是「永远转圈，对了就 break」。输入校验同一套路。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>把 <code>int(score_text)</code> 包进 try；失败 print 后 return。</li>
      <li>升级：失败不放弃，while 直到整数。</li>
      <li>故意输入小数 <code>18.5</code>，观察 <code>int</code> 是否也 ValueError（是）。</li>
    </ol>

    <h2>收束</h2>
    <p>
      异常处理不是「消灭错误」，而是「预期内的失败要优雅接住」。
      下一课：把成绩写进文件——关掉程序，数据还在。
    </p>
  </div>
</template>
