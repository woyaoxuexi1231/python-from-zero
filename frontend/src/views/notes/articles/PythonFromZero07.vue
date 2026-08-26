<template>
  <div class="article">
    <p>
      第 6 课成绩本是一条直线：打印 → 查一次 → 加一次 → 结束。
      真正的小工具会<strong>转圈</strong>：做完回到菜单，直到选退出。
      工具是 <code>while</code>、<code>break</code>、<code>continue</code>。
    </p>

    <h2>for vs while</h2>
    <ul>
      <li><code>for</code>：事先知道转几圈（列表有几项）</li>
      <li><code>while</code>：条件还成立就继续，圈数事先不一定知道</li>
    </ul>
<pre><code>count = 3
while count &gt; 0:
    print(count)
    count = count - 1
print("到 0 了，循环结束")</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        while 里忘了改条件变量，会变成死循环。
        菜单场景用 <code>while True</code> + <code>break</code> 更常见，退出条件写在分支里。
      </p>
    </div>

    <h2>while True + break</h2>
<pre><code>n = 1
while True:
    print(n)
    if n == 3:
        break
    n = n + 1</code></pre>
    <p><code>break</code>：立刻离开当前循环。菜单的「退出」几乎都这么写。</p>

    <h2>continue：跳过本圈剩余部分</h2>
<pre><code>n = 0
while n &lt; 5:
    n = n + 1
    if n == 3:
        continue
    print(n)   # 1 2 4 5，跳过 3</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>break</code> 离开整个循环；<code>continue</code> 只结束这一圈，马上再测条件。
        两者都只影响最近一层循环。
      </p>
    </div>

    <h2>菜单：while + if 拼起来</h2>
    <p>
      <code>input()</code> 永远是字符串，所以和 <code>"1"</code> 比，不要和整数 <code>1</code> 比。
    </p>
<pre><code>def print_menu() -&gt; None:
    print("1. 查看成绩单")
    print("2. 查询一个人")
    print("3. 新增/修改")
    print("0. 退出")

while True:
    print_menu()
    choice = input("请选择：")
    if choice == "1":
        print_report(scores)
    elif choice == "2":
        lookup()
    elif choice == "3":
        add_one()
    elif choice == "0":
        print("再见")
        break
    else:
        print("没有这个选项")</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>choice == 1</code>（整数）永远对不上——用户输入是 <code>"1"</code>。
        分数输入 <code>abc</code> 时 <code>int</code> 仍会崩；下一课用 try/except 接住。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>把成绩本函数接到菜单选项上，确认能反复进出。</li>
      <li>加选项「平均分和及格名单」，打印后仍回到菜单。</li>
      <li>故意选不存在的选项，确认走 else 而不是崩。</li>
    </ol>

    <h2>收束</h2>
    <p>
      菜单的骨架就是：<code>while True</code> → 读选择 → 分支干活 → 退出就 break。
      下一课专治「输入不合法直接崩」：<code>try / except</code>。
    </p>
  </div>
</template>
