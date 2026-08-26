<template>
  <div class="article">
    <p>
      1~17 课代码都挤在一个文件里。现实要分文件、再拼回来。
      这一课：<code>import</code>、<code>from…import</code>、<code>as</code>、<code>__name__</code>，以及自己写模块。
    </p>

    <h2>一个 .py 就是一个模块</h2>
    <p>
      同目录放 <code>tools.py</code>，里面有函数和变量；
      另一个文件就可以借来用。文件夹 + <code>__init__.py</code> 才叫包——本课先用单文件模块。
    </p>

    <h2>三种引入方式</h2>
<pre><code>import tools
print(tools.greet("小明"))
print(tools.PI)

from tools import square, greet
print(square(7))

import calc as c
print(c.mean([10, 20, 30]))</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>import 模块</code>：带前缀，不撞名，来源清晰。
        <code>from…import</code>：短，但同名易撞。
        <code>as</code>：改名避冲突或缩短长名。
      </p>
    </div>

    <h2>模块之间也能互相 import</h2>
    <p>
      <code>calc.py</code> 可以 <code>from tools import add</code>，再对外提供 <code>sum_list</code>。
      模块像积木，不是孤岛。
    </p>

    <h2>__name__ == "__main__"</h2>
<pre><code># tools.py 末尾
if __name__ == "__main__":
    print("被直接运行了")</code></pre>
    <ul>
      <li>直接 <code>python tools.py</code> → <code>__name__</code> 是 <code>"__main__"</code>，演示代码会跑</li>
      <li>被别人 import → <code>__name__</code> 是 <code>"tools"</code>，演示代码不跑</li>
    </ul>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        从第 18 课起每课一个文件夹。请在对应目录下运行主课文件，
        或保证工作目录能找到同目录模块，否则 <code>ImportError</code>。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>自己写一个小模块，用三种方式分别引入。</li>
      <li>给模块加 <code>if __name__ == "__main__"</code>，对比直接跑与被 import。</li>
      <li>打开 calc 看它如何复用 tools。</li>
    </ol>

    <h2>收束</h2>
    <p>
      拆文件靠模块；拼回来靠 import；主程序守卫靠 __name__。
      下一课扒开 for：迭代器与生成器、yield 惰性求值。
    </p>
  </div>
</template>
