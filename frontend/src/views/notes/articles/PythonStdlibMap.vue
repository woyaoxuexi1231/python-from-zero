<template>
  <div class="article">
    <p>
      Python 标准库模块多、名字散，不像一门课那样按章排好。
      这篇只做一件事：<strong>官方有哪些模块、初学先学哪档、from-zero 学到哪了、后面按什么顺序扩</strong>。
    </p>

    <h2>先分三层：别混在一块</h2>
    <table class="article-table">
      <thead>
        <tr>
          <th>层次</th>
          <th>例子</th>
          <th>要 pip install 吗</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>内置（不用 import）</td>
          <td><code>list</code>、<code>print</code>、<code>open</code>、<code>def</code>、<code>class</code></td>
          <td>否，装 Python 就有</td>
        </tr>
        <tr>
          <td>标准库（import 即用）</td>
          <td><code>json</code>、<code>pathlib</code>、<code>dataclasses</code>、<code>typing</code></td>
          <td>否</td>
        </tr>
        <tr>
          <td>第三方 PyPI</td>
          <td><code>requests</code>、<code>pytest</code>、<code>fastapi</code></td>
          <td>是（<code>pip</code> / <code>uv</code>）</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        标准库叫「batteries included」：常用能力尽量自带。
        但 HTTP、测试、Web 等领域，社区第三方往往比官方更好用——
        看到 <code>pip install xxx</code>，默认 <strong>xxx 不是标准库</strong>。
        能在
        <a href="https://docs.python.org/3/library/" target="_blank" rel="noopener">docs.python.org/3/library/</a>
        搜到模块名，才是官方。
      </p>
    </div>

    <h2>学习分级：先学哪档</h2>
    <ul class="tier-legend">
      <li><span class="tier tier--p0">★ 初学必学</span> — 写小程序、from-zero、日常脚本离不开</li>
      <li><span class="tier tier--p1">◎ 常用</span> — 真实项目常碰；★ 学稳后再扩（约 1～2 个月内）</li>
      <li><span class="tier tier--p2">○ 知道即可</span> — 用时再查，不必背 API</li>
      <li><span class="tier tier--p3">· 专项/少见</span> — GUI、底层网络等，初学可跳过</li>
    </ul>
    <p>
      <strong>策略</strong>：先把所有 ★ 吃透；再按文末顺序加 ◎；○ 和 · 当字典。
    </p>

    <h2>内置（不用 import）</h2>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>内容</th>
          <th>干什么</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>int</code> <code>float</code> <code>str</code> <code>bool</code></td>
          <td>基本类型</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>list</code> <code>dict</code> <code>set</code> <code>tuple</code></td>
          <td>容器</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>print</code> <code>len</code> <code>range</code> <code>sorted</code> <code>enumerate</code> <code>zip</code></td>
          <td>常用内置函数</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>open</code> <code>input</code></td>
          <td>读写文件、读用户输入</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>def</code> <code>class</code> <code>try/except</code> <code>raise</code></td>
          <td>函数、类、异常</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>if</code> <code>for</code> <code>while</code> <code>with</code></td>
          <td>控制流、上下文（with 文件）</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>isinstance</code> <code>hasattr</code> <code>getattr</code> <code>type</code></td>
          <td>运行时类型与属性</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>any</code> <code>all</code> <code>min</code> <code>max</code> <code>sum</code></td>
          <td>聚合、判断</td>
        </tr>
      </tbody>
    </table>

    <h2>标准库模块（import 即用）</h2>
    <p>按领域分组；「from-zero」列标你课里是否已专门学过。</p>

    <h3>数据与容器</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>collections</code></td>
          <td>defaultdict、Counter、namedtuple、deque</td>
          <td>第 25 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>itertools</code></td>
          <td>chain、islice、groupby、product、accumulate</td>
          <td>第 25 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>dataclasses</code></td>
          <td>@dataclass、field、asdict</td>
          <td>第 26 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>typing</code></td>
          <td>Optional、Literal、TypedDict、Callable</td>
          <td>第 27 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>enum</code></td>
          <td>Enum 枚举固定几种值</td>
          <td>第 30 课</td>
        </tr>
      </tbody>
    </table>

    <h3>文件、路径、序列化</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>json</code></td>
          <td>dump、load、读写 JSON 文件</td>
          <td>第 9 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>pathlib</code></td>
          <td>Path、拼路径、glob、iterdir</td>
          <td>第 20 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>os</code> / <code>sys</code></td>
          <td>环境变量、argv、退出码</td>
          <td>零散</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>csv</code></td>
          <td>读写 CSV 表格</td>
          <td>未学</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>pickle</code></td>
          <td>Python 对象二进制序列化（慎用不可信来源）</td>
          <td>未学</td>
        </tr>
      </tbody>
    </table>

    <h3>函数式、装饰器、资源管理</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>functools</code></td>
          <td>wraps、lru_cache、partial</td>
          <td>第 23 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td><code>contextlib</code></td>
          <td>@contextmanager、suppress</td>
          <td>第 24 课 ✓</td>
        </tr>
      </tbody>
    </table>

    <h3>模块与包、迭代</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td>（内置 + <code>import</code> 机制）</td>
          <td>模块、<code>__name__ == "__main__"</code></td>
          <td>第 18 课 ✓</td>
        </tr>
        <tr>
          <td><span class="tier tier--p0">★</span></td>
          <td>生成器 / 迭代器（语言特性）</td>
          <td>yield、iter、next</td>
          <td>第 19 课 ✓</td>
        </tr>
      </tbody>
    </table>

    <h3>文本、时间、命令行</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>re</code></td>
          <td>正则 search、match、sub</td>
          <td>第 32 课</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>datetime</code></td>
          <td>now、strftime、timedelta</td>
          <td>第 31 课</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>argparse</code></td>
          <td>命令行参数，替代手写菜单</td>
          <td>第 33 课</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>logging</code></td>
          <td>分级日志，替代满屏 print</td>
          <td>第 34 课</td>
        </tr>
      </tbody>
    </table>

    <h3>测试、网络、并发</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>常用内容</th>
          <th>from-zero</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>unittest</code></td>
          <td>官方单元测试</td>
          <td>了解；实战用 pytest（第 35 课）</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>urllib.request</code></td>
          <td>官方 HTTP（偏底层）</td>
          <td>第 36 课阶段 1 ✓；实战多用 requests</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>threading</code> / <code>concurrent.futures</code></td>
          <td>线程、线程池</td>
          <td>未学</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>asyncio</code></td>
          <td>异步协程</td>
          <td>以后</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>multiprocessing</code></td>
          <td>多进程</td>
          <td>以后</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>subprocess</code></td>
          <td>调外部命令</td>
          <td>以后</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>sqlite3</code></td>
          <td>嵌入式数据库</td>
          <td>以后</td>
        </tr>
      </tbody>
    </table>

    <h3>其它标准库（知道即可 / 专项）</h3>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>模块</th>
          <th>备注</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>hashlib</code>、<code>secrets</code></td>
          <td>哈希、安全随机数</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>xml.etree</code>、<code>html</code></td>
          <td>解析 XML / HTML</td>
        </tr>
        <tr>
          <td><span class="tier tier--p3">·</span></td>
          <td><code>tkinter</code></td>
          <td>内置 GUI，初学可跳过</td>
        </tr>
        <tr>
          <td><span class="tier tier--p3">·</span></td>
          <td><code>socket</code>、<code>email</code>…</td>
          <td>底层网络、邮件，用时再查</td>
        </tr>
      </tbody>
    </table>

    <h2>第三方 PyPI（初学后会常碰）</h2>
    <table class="article-table">
      <thead>
        <tr>
          <th>优先级</th>
          <th>包名</th>
          <th>干什么</th>
          <th>和官方关系</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>pytest</code></td>
          <td>写测试、断言</td>
          <td>第 35 课 ✓；比 <code>unittest</code> 更顺手；需 pip</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>requests</code></td>
          <td>发 HTTP 请求</td>
          <td>第 36 课阶段 2 ✓；官方有 <code>urllib</code>，但 requests 更常用</td>
        </tr>
        <tr>
          <td><span class="tier tier--p1">◎</span></td>
          <td><code>flask</code></td>
          <td>写 Web / API（入门对照）</td>
          <td>第 36 课阶段 2 ✓；对照官方 <code>http.server</code></td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>fastapi</code></td>
          <td>写 Web / API（现代主流）</td>
          <td>后续项目再用；官方 <code>http.server</code> 仅演示级</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>pydantic</code></td>
          <td>数据校验</td>
          <td>常和 dataclass / FastAPI 搭配</td>
        </tr>
        <tr>
          <td><span class="tier tier--p2">○</span></td>
          <td><code>numpy</code> / <code>pandas</code></td>
          <td>数值、表格分析</td>
          <td>标准库无对等物，走数据方向再学</td>
        </tr>
      </tbody>
    </table>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>dataclass</code>、<code>collections</code>、<code>itertools</code>、<code>typing</code>
        都是<strong>标准库</strong>，<code>from xxx import</code> 即可，不要 pip。
        教程写 <code>pip install requests</code> 的，才是第三方。
      </p>
    </div>

    <h2>from-zero 进度：★ 档覆盖到哪了</h2>
    <p>第 1～27 课已覆盖绝大部分 ★ 标准库与内置能力：</p>
    <ul>
      <li>内置：类型、容器、循环、函数、类、异常</li>
      <li><code>json</code>、<code>pathlib</code> — 存盘与路径</li>
      <li><code>functools</code>、<code>contextlib</code> — 装饰器与 with</li>
      <li><code>collections</code>、<code>itertools</code> — 容器与迭代工具</li>
      <li><code>dataclasses</code>、<code>typing</code> — 数据类与类型标注</li>
    </ul>
    <p>你现在处在：<strong>★ 与 ◎ 基础路线已收官（含 pytest / HTTP 标准库 vs requests+Flask）；可大复习后开自己的项目</strong>。</p>

    <h2>学完 ★ 之后，建议按这个顺序扩 ◎</h2>
    <ol>
      <li><code>enum</code> — 订单/任务等固定状态（第 30 课 ✓）</li>
      <li><code>datetime</code> — 日志时间、文件名时间戳（第 31 课 ✓）</li>
      <li><code>re</code> — 从文本里抠字段（第 32 课 ✓）</li>
      <li><code>argparse</code> — 菜单程序升级成 CLI（第 33 课 ✓）</li>
      <li><code>logging</code> — 代替 print 调试（第 34 课 ✓）</li>
      <li><code>pytest</code>（第三方）— 给函数写断言（第 35 课 ✓）</li>
      <li><code>requests</code> + <code>Flask</code>（第三方）— HTTP 调用与暴露，对照标准库（第 36 课 ✓）</li>
      <li><code>threading</code> / <code>concurrent.futures</code> — 真需要并行时再学</li>
    </ol>

    <h2>官方文档去哪查</h2>
    <ul>
      <li>
        <strong>标准库索引</strong>：
        <a href="https://docs.python.org/3/library/" target="_blank" rel="noopener">Library Reference</a>
        —— 按模块字母排列，相当于 API 总目录。
      </li>
      <li>
        <strong>内置类型/函数</strong>：
        <a href="https://docs.python.org/3/library/stdtypes.html" target="_blank" rel="noopener">Built-in Types</a>、
        <a href="https://docs.python.org/3/library/functions.html" target="_blank" rel="noopener">Built-in Functions</a>。
      </li>
      <li>
        <strong>第三方</strong>：
        <a href="https://pypi.org/" target="_blank" rel="noopener">pypi.org</a> + 各项目文档。
      </li>
    </ul>

    <h2>收束</h2>
    <p>
      不必背全标准库几百个模块。记住分级：
      <strong>★ 跟 from-zero 走</strong>（你已在第 27 课）；
      <strong>◎ 按上面 8 条慢慢加</strong>；
      其余 ○、· <strong>知道有这东西，用时再查 Library Reference</strong>。
      这张表就是 Python 侧的「包地图」。
    </p>
  </div>
</template>

<style scoped>
.article-table {
  width: 100%;
  border-collapse: collapse;
  margin: 1rem 0 1.25rem;
  font-size: 0.92rem;
  line-height: 1.45;
}

.article-table th,
.article-table td {
  border: 1px solid var(--border-subtle, rgba(0, 0, 0, 0.12));
  padding: 0.55rem 0.65rem;
  text-align: left;
  vertical-align: top;
}

.article-table th {
  background: var(--surface-muted, rgba(0, 0, 0, 0.04));
  font-weight: 600;
}

.article-table code {
  font-size: 0.88em;
}

.tier-legend {
  list-style: none;
  padding: 0;
  margin: 0.75rem 0 1rem;
}

.tier-legend li {
  margin: 0.35rem 0;
}

.tier {
  display: inline-block;
  min-width: 5.5rem;
  font-weight: 600;
  font-size: 0.88rem;
}

.tier--p0 { color: #0d7a4a; }
.tier--p1 { color: #1a5fb4; }
.tier--p2 { color: #856404; }
.tier--p3 { color: #6c757d; }
</style>
