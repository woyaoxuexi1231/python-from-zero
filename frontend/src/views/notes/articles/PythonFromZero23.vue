<template>
  <div class="article">
    <p>
      想在多个函数前后打日志、计时、校验，又不想复制粘贴？
      装饰器就是「包一层」的语法糖：<code>@deco</code> 等价于 <code>func = deco(func)</code>。
    </p>

    <h2>铺垫：函数是一等公民</h2>
<pre><code>def greet(name: str) -&gt; str:
    return f"你好，{name}"

def apply(f, v):
    return f(v)

print(apply(greet, "小明"))</code></pre>

    <h2>手写包装器</h2>
<pre><code>def log_deco(func):
    def inner(name):
        print(f"[日志] 准备调用 {func.__name__}")
        result = func(name)
        print(f"[日志] 结束，结果={result!r}")
        return result
    return inner

def greet2(name: str) -&gt; str:
    return f"你好，{name}"

wrapped = log_deco(greet2)
print(wrapped("小红"))</code></pre>

    <h2>@ 语法糖</h2>
<pre><code>@log_deco
def greet3(name: str) -&gt; str:
    return f"你好，{name}"

print(greet3("hulei"))</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        装饰器接收函数，返回新函数。调用新函数时：先做额外事，再调原函数，再返回结果。
        原函数定义本身没被改写，只是名字指向了包装后的版本。
      </p>
    </div>

    <h2>*args / **kwargs 透传</h2>
<pre><code>def timed(func):
    def inner(*args, **kwargs):
        # ... 计时
        return func(*args, **kwargs)
    return inner</code></pre>
    <p>包装器不要写死参数形态，才能套在任意函数上。</p>

    <h2>functools.wraps</h2>
<pre><code>import functools

def deco(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        return func(*args, **kwargs)
    return inner</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        不加 wraps，<code>__name__</code>/<code>__doc__</code> 会变成 inner，调试和文档都错乱。
        带参装饰器是「三层」：外层收参数，中层收 func，内层才是调用时跑的——先会无参再学带参。
      </p>
    </div>

    <h2>建议你自己练的几件事</h2>
    <ol>
      <li>写日志装饰器，用 @ 套两个不同参数形式的函数。</li>
      <li>对比加不加 wraps 时的 __name__。</li>
      <li>阅读配课里的 lru_cache 示例，体会「装饰器也能来自标准库」。</li>
    </ol>

    <h2>收束</h2>
    <p>
      装饰器 = 高阶函数 + 语法糖。下一课上下文管理器：with 与资源清理。
    </p>
  </div>
</template>
