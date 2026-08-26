<template>
  <div class="article">
    <p>
      脚本越写越大，<code>print</code> 满天飞：分不清正常信息、警告还是出错；
      想关掉调试输出要改一堆代码，想写进文件还得再包一层。
      <code>logging</code> 按<strong>级别</strong>过滤、统一格式，可挂控制台和文件等多个输出。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li>五级日志：<code>DEBUG</code> / <code>INFO</code> / <code>WARNING</code> / <code>ERROR</code> / <code>CRITICAL</code></li>
      <li><code>getLogger(__name__)</code> 拿模块级 logger，别到处 <code>print</code></li>
      <li><code>basicConfig</code> 配级别与格式（脚本入口配一次）</li>
      <li><code>Handler</code> + <code>Formatter</code>：自定义输出目标与时间戳格式</li>
      <li>和 <code>argparse</code> 的 <code>-v</code> 联动：<code>verbose → DEBUG</code></li>
      <li>加餐：自定义 <code>ColorFormatter</code>，控制台按级别上色</li>
    </ul>

    <h2>最小例子</h2>
<pre><code>import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
logger.debug("细节")      # 默认看不见
logger.info("程序启动")   # INFO | 程序启动
logger.warning("注意")    # WARNING | 注意</code></pre>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        级别数字越小越「啰嗦」：<code>DEBUG=10</code>、<code>INFO=20</code>、<code>WARNING=30</code>……
        logger 设了 <code>setLevel(INFO)</code> 后，只有 <code>levelno ≥ 20</code> 的记录才会输出。
        用 <code>logger.info("x=%s", x)</code> 懒格式化，别先 <code>f-string</code> 拼好再传。
      </p>
    </div>

    <h2>和 argparse 搭配</h2>
<pre><code>def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s | %(message)s", force=True)

# main 里：args.verbose 来自 -v / --verbose（第 33 课）</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        默认级别是 <code>WARNING</code>——<code>info</code>/<code>debug</code> 要先 <code>basicConfig</code> 或 <code>setLevel</code>。
        <code>basicConfig</code> 多次调用常被忽略；Python 3.8+ 用 <code>force=True</code> 重置。
        库代码里别 <code>basicConfig</code>，只 <code>getLogger(__name__)</code>，让调用方决定怎么配。
      </p>
    </div>

    <h2>测试时捕获日志</h2>
<pre><code>import io, logging

stream = io.StringIO()
handler = logging.StreamHandler(stream)
logger = logging.getLogger("test")
logger.handlers.clear()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False

logger.info("你好")
text = stream.getvalue().strip()   # 拿到输出正文</code></pre>

    <h2>加餐：控制台彩色</h2>
    <p>
      标准库不上色；终端认 ANSI（<code>\033[31m</code> 红、<code>\033[0m</code> 复位）。
      继承 <code>Formatter</code>，按 <code>record.levelno</code> 给 <code>levelname</code> 包颜色即可。
    </p>
<pre><code>_COLORS = {
    logging.DEBUG: "\033[36m", logging.INFO: "\033[32m",
    logging.WARNING: "\033[33m", logging.ERROR: "\033[31m",
    logging.CRITICAL: "\033[35m",
}
_RESET = "\033[0m"

class ColorFormatter(logging.Formatter):
    def format(self, record):
        color = _COLORS.get(record.levelno, "")
        original = record.levelname
        record.levelname = f"{color}{original}{_RESET}"
        try:
            return super().format(record)
        finally:
            record.levelname = original

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColorFormatter("%(levelname)-8s | %(message)s"))</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <strong>只给控制台 Handler 上色</strong>；<code>FileHandler</code> 用普通 Formatter，否则日志文件会留下转义码。
        改完 <code>levelname</code> 必须还原。老版 CMD 可能无色，可用 <code>colorama</code>；省事库还有 <code>colorlog</code> / <code>rich</code>。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>先跑 <code>34_logging.py</code>，对照各级别输出、<code>verbose</code> 与【9】彩色演示。</li>
      <li>再打开 <code>34_logging_exercise.py</code>，6 题：logger、级别映射、StringIO 捕获、过滤、问候日志。</li>
      <li>题 4/6 用 <code>StringIO</code> + <code>Handler</code>，不要 <code>basicConfig</code>。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走骨架：<code>getLogger</code> → <code>setLevel</code> → <code>info/warning/error</code>；
      脚本入口 <code>basicConfig</code> 一次；需要文件再加 <code>FileHandler</code>；
      控制台要彩色就挂 <code>ColorFormatter</code>。
      下一课是 <code>pytest</code>（第 35 课，第三方，给函数写断言）。
      也可以先把 26～34 串起来做一个小 CLI 工具复习。
    </p>
  </div>
</template>
