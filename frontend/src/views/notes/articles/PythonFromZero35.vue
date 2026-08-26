<template>
  <div class="article">
    <p>
      改完函数靠肉眼看 <code>print</code>，边界容易漏，别人也无法一键验证。
      <code>pytest</code> 是<strong>第三方</strong>测试库（需 <code>pip install pytest</code>）：
      自动发现 <code>test_*.py</code>，用 <code>assert</code> 判定对错。
      这是 from-zero 工程习惯三件套的第一件：<strong>测试</strong>。
      命令行推荐 <code>python -m pytest</code>（不依赖 Scripts 是否在 PATH）。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>安装与运行：<code>pip install pytest</code> → <code>python -m pytest path -v</code></li>
      <li>命名约定：文件 <code>test_*.py</code>，函数 <code>test_</code> 开头</li>
      <li><code>assert 实际 == 期望</code></li>
      <li><code>pytest.raises</code>：测会不会抛错</li>
      <li><code>@pytest.mark.parametrize</code>：一组输入少写重复</li>
      <li>fixture 一瞥（知道即可）</li>
    </ul>

    <h2>最小例子</h2>
<pre><code># tools.py
def add(a, b):
    return a + b

# test_tools_demo.py
from tools import add

def test_add_positive():
    assert add(2, 3) == 5</code></pre>
    <p>在 <code>backend</code> 下执行：</p>
<pre><code>python -m pytest 35_pytest/ -v</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        pytest 扫描符合命名的文件/函数，执行它们；
        <code>assert</code> 失败就标红并打印期望与实际的差异。
        无输出的 assert 通过 = 好事。
      </p>
    </div>

    <h2>测异常</h2>
<pre><code>import pytest

def test_bad_range():
    with pytest.raises(ValueError, match="lo"):
        clamp(1, 10, 0)</code></pre>

    <h2>参数化</h2>
<pre><code>@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_many(a, b, expected):
    assert add(a, b) == expected</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>pytest</code> <strong>不是</strong>标准库，没装会 <code>ModuleNotFoundError</code>。
        函数名忘了 <code>test_</code> 前缀 → 静默不跑。
        在错误目录执行可能导致 <code>import tools</code> 失败——请在 <code>backend</code> 目录跑。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li><code>pip install pytest</code>（若尚未安装）。</li>
      <li>跑 <code>35_pytest.py</code>，再跑 <code>python -m pytest 35_pytest/ -v</code> 看全绿。</li>
      <li>打开 <code>35_pytest_exercise.py</code>，实现 6 题：sub、is_even、clip、first_word、safe_div、letter_grade。</li>
      <li>选做：仿 <code>test_tools_demo.py</code> 给练习函数写 <code>test_*.py</code>。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走骨架：业务函数 + <code>test_*.py</code> + <code>assert</code> + <code>python -m pytest -v</code>。
      下一课是 HTTP（第 36 课）：先标准库 <code>urllib</code>/<code>http.server</code>，
      再对照三方 <code>requests</code>/<code>Flask</code>；基础课最后一课。
      学完 pytest + HTTP，适合大复习后自己开项目。
    </p>
  </div>
</template>
