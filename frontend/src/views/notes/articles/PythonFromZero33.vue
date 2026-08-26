<template>
  <div class="article">
    <p>
      第 7 课的 <code>while</code> 菜单适合人机交互；日常脚本更常是「一条命令跑完」：
      <code>python tool.py Alice --times 3</code>。
      手拆 <code>sys.argv</code> 又脆又难写帮助信息。<code>argparse</code> 让你<strong>声明</strong>参数，它负责解析、类型转换和 <code>-h</code>。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>位置参数（必填、按顺序）</li>
      <li>可选参数（<code>--name</code> / <code>-n</code>、默认值、<code>type=</code>）</li>
      <li>开关（<code>action="store_true"</code>）</li>
      <li><code>choices</code> 限制取值</li>
      <li>用 <code>parse_args([...])</code> 测脚本，不依赖真实命令行</li>
    </ul>

    <h2>最小例子</h2>
<pre><code>import argparse

parser = argparse.ArgumentParser(description="打招呼")
parser.add_argument("name", help="要问候的人")
parser.add_argument("--times", type=int, default=1)

# 演示/测试：传入列表；真实运行时写 parse_args() 读命令行
args = parser.parse_args(["hulei", "--times", "2"])
print(args.name, args.times)   # hulei 2</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>parse_args</code> 返回 <code>Namespace</code>：用属性取值（<code>args.name</code>），不是字典。
        <code>type=int</code> 写在 <code>add_argument</code> 里，解析时自动转换——别再手写 <code>int(args.times)</code>。
      </p>
    </div>

    <h2>开关与 choices</h2>
<pre><code>parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--mode", choices=["fast", "safe"], default="safe")

parser.parse_args([]).verbose          # False（没写开关）
parser.parse_args(["-v"]).verbose      # True
parser.parse_args(["--mode", "fast"]).mode  # "fast"</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        位置参数<strong>没有</strong> <code>--</code>，顺序固定；可选参数以 <code>-</code>/<code>--</code> 开头。
        <code>--out-file</code> 在 Namespace 里变成 <code>args.out_file</code>（横杠变下划线）。
        非法参数会 <code>SystemExit</code>——练习一律传合法 <code>argv</code>；正式工具靠 <code>python tool.py -h</code> 看帮助。
      </p>
    </div>

    <h2>推荐骨架</h2>
<pre><code>def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="...")
    p.add_argument("name")
    p.add_argument("--times", type=int, default=1)
    return p

def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    # 用 args 干活…

if __name__ == "__main__":
    main()   # 真实命令行；测试时 main(["Alice", "--times", "2"])</code></pre>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>33_argparse.py</code>，对照输出，看清位置 / 可选 / 开关三种形态。</li>
      <li>再打开 <code>33_argparse_exercise.py</code>，6 题：加法、问候、echo、mode、copy、report。</li>
      <li>每题都用 <code>parse_args(argv)</code> 传列表；题 3/5/6 用到 <code>store_true</code>。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走骨架：<code>ArgumentParser</code> → <code>add_argument</code> → <code>parse_args</code> → <code>args.xxx</code>。
      菜单适合交互，CLI 适合脚本；两种入口可以并存。
      下一课是 <code>logging</code>（第 34 课，用分级日志替代满屏 print）。
      也可以把 26～33 串起来做一次统一复习。
    </p>
  </div>
</template>
