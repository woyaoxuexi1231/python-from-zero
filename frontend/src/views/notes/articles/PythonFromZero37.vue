<template>
  <div class="article">
    <p>
      读 <code>config.py</code> 时撞见了 <code>os.getenv</code>，但你的课到现在没讲过 <code>os</code> 是啥。
      这一课就从 <code>os</code> 模块讲起：它帮你<strong>和操作系统打交道</strong>——读环境变量、拼路径、建文件夹……
      明白了 <code>os</code>，再看后端常用的 <code>BaseSettings</code>（pydantic-settings）如何把这些重复劳动收进一个类里。
    </p>

    <h2>这一课解决什么问题</h2>
    <ul>
      <li><code>os</code> 模块是干嘛的、最常用哪几个 API</li>
      <li><code>os.getenv</code> / <code>os.environ</code>：读环境变量</li>
      <li><code>os.path</code>：拼路径、取目录、判断存在</li>
      <li>为什么手写配置麻烦 → 引出 <code>BaseSettings</code></li>
      <li><code>SettingsConfigDict</code>、字段↔变量对应、取值优先级、<code>@lru_cache</code></li>
    </ul>

    <h2>Step 1：os 是什么</h2>
    <p>
      <code>os</code> 是标准库里的「操作系统接口」。Python 脚本跑在操作系统上，绕不开的杂活——
      当前在哪个目录、环境变量设了啥、某文件存不存在——都归 <code>os</code>（以及它的兄弟 <code>os.path</code>）管。
      你大概率以后天天用。
    </p>

    <h2>Step 2：读环境变量 os.getenv / os.environ</h2>
    <p>
      环境变量就是操作系统里的一堆「键=值」设置（比如 <code>PATH</code>、<code>HOME</code>）。Python 里最常见的两个读法：
    </p>
<pre><code>import os

# 1) os.getenv(名字, 默认值)：读不到就返回默认值，最常用
port = os.getenv("APP_PORT", "8800")
print(port)                  # '8800'（默认值）；若系统设了 APP_PORT 则返回那个值

# 2) os.environ：像字典一样的全局表，可读可改
print(os.environ.get("HOME", "/"))   # 取值，读不到给默认
print("PATH" in os.environ)          # 判断某个变量存不存在</code></pre>
    <div class="callout callout--principle">
      <span class="callout__label">原理</span>
      <p>
        <code>os.getenv(name, default)</code> 本质是 <code>os.environ.get(name, default)</code> 的简写、
        等价于 <code>os.environ[name] if name in os.environ else default</code>。
        它<strong>永远返回字符串</strong>——所以要数字还得自己转 <code>int(...)</code>，这正是后面 BaseSettings 要改进的点。
      </p>
    </div>

    <h2>Step 3：拼路径 os.path 系列</h2>
    <p>写脚本常要定位文件。手拼字符串用 <code>"/"</code> 会水土不服（Windows 用反斜杠），<code>os.path</code> 帮你跨平台拼：</p>
<pre><code>import os

base = "/home/user/project"

# join：跨平台拼路径
data = os.path.join(base, "data", "my_gathering.json")
print(data)                     # 本机会用对的分隔符拼好

print(os.path.dirname(data))    # 取所在目录
print(os.path.basename(data))   # 取文件名
print(os.path.exists(data))     # 该路径是否存在
os.makedirs("a/b/c", exist_ok=True)   # 递归建目录，已存不报错</code></pre>
    <p>
      顺便一提：你在 <code>config.py</code> 里看到的 <code>Path</code>（来自 <code>pathlib</code>）是更现代的替代，
      写法更像对象（<code>Path("a") / "b"</code>）。两者都能拼路径；课程里 <code>os.path</code> 是打基础，
      <code>pathlib</code> 第 20 课讲过。这条线先记住「python 有专门管路径的模块」。
    </p>

    <h2>Step 4：手写配置的痛点</h2>
    <p>现在你能看懂这段最原始写法了。它的毛病很明显：</p>
<pre><code>import os

PORT = int(os.getenv("APP_PORT", "8800"))   # 转类型靠手动 int()
HOST = os.getenv("APP_HOST", "127.0.0.1")
TITLE = os.getenv("GATHERING_TITLE", "待定")</code></pre>
    <ul>
      <li>每个配置一行 <code>os.getenv</code>，配置多了全是样板</li>
      <li>字符串 → 数字要手动 <code>int()</code>，忘写就出错</li>
      <li>类型写错不会立刻报错</li>
    </ul>

    <h2>Step 5：BaseSettings 一键收编配置</h2>
    <p>
      <code>pydantic-settings</code> 的 <code>BaseSettings</code> 就是来收拾上面这些毛病的：
      把配置声明成一个类，它自动完成「读环境变量 + 读 .env + 类型转换 + 默认值 + 校验」。
      它继承自 <code>pydantic</code> 的 <code>BaseModel</code>，所以拥有「类型注解 → 自动转换校验」的能力。
    </p>
<pre><code>from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",             # 额外去这个文件里读配置
        env_file_encoding="utf-8",   # 用 UTF-8 读，中文不乱码
        extra="ignore",              # 类里没声明的字段，.env 写了也忽略
    )

    app_port: int = 8800
    gathering_title: str = "待定"

s = Settings()
print(s.app_port)          # 类型是 int，不是字符串！自动转换好了</code></pre>
    <p>写死 <code>app_port: int</code>，pydantic 会把它读到的值自动转成整数，类型错了直接抛异常——你手写 <code>int(os.getenv(...))</code> 还不一定有这层保障。</p>

    <h2>关键澄清：环境变量 ≠ 配置文件（.env）</h2>
    <p>这里最容易绕，专门讲清楚：<code>os.getenv</code> 读的<strong>不是配置文件</strong>，而是<strong>操作系统维护的一张「键=值」全局表</strong>（环境变量表）。它不来自任何文件，来源是系统 / 用户 / shell 启动时加载的那些设置。</p>
<pre><code>import os
os.getenv("APP_PORT", "8800")   # 从"系统环境变量表"里读，跟文件没关系

# PowerShell 里先设一下再看：
# $env:APP_PORT = "9000"
# python -c "import os; print(os.getenv('APP_PORT'))"   # 9000</code></pre>
    <p>
      而 <code>.env</code> 是一行行 <code>键=值</code> 的<strong>配置文件</strong>。它不是环境变量本身；
      要想 <code>os.getenv</code> 读到它，得先有个工具把 <code>.env</code> 读出来<strong>装进环境变量表</strong>。最常用的工具是 <code>python-dotenv</code>：
    </p>
<pre><code>from dotenv import load_dotenv   # pip install python-dotenv
import os

load_dotenv()                     # 读 .env → 塞进 os.environ
os.getenv("APP_PORT")             # 这时才能读到 .env 里的值</code></pre>
    <p><code>BaseSettings</code> 里的 <code>env_file=".env"</code>，底层做的正是 <code>load_dotenv()</code> 这件事：读 .env → 放进环境变量 → 再去匹配字段。所以对你「像是读配置文件」，其实先变成环境变量再取值。整条线：</p>
<pre><code>读取优先顺序：
1. 真实环境变量（系统里已设）     ← os.getenv 只碰这一层
2. .env 文件（用工具读进环境变量表） ← BaseSettings 帮你做
3. 字段默认值</code></pre>

    <h2>字段名 ↔ 环境变量名：怎么对上号</h2>
    <p>默认按<strong>下划线风格、大小写不敏感</strong>匹配：</p>
    <table class="article-table">
      <thead>
        <tr>
          <th>字段</th>
          <th>能命中的环境变量</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>app_host</code></td>
          <td><code>APP_HOST</code> / <code>app_host</code></td>
        </tr>
        <tr>
          <td><code>gathering_title</code></td>
          <td><code>GATHERING_TITLE</code> / <code>gathering_title</code></td>
        </tr>
        <tr>
          <td><code>cors_origins</code></td>
          <td><code>CORS_ORIGINS</code>（值为 JSON 数组时自动解析成列表）</td>
        </tr>
      </tbody>
    </table>
    <p><code>cors_origins: list[str]</code> 这种列表类型，pydantic 也会自动把 JSON 文本解析成 Python 列表。</p>

    <h2>取值优先级 &amp; @lru_cache</h2>
    <p>一个字段最终取谁，按优先级：</p>
<pre><code>环境变量  &gt;  你显式传的参数  &gt;   .env 文件  &gt;   字段默认值</code></pre>
    <p>所以系统里设了 <code>APP_PORT</code>，会压过 <code>.env</code> 和默认值。最后看 <code>config.py</code> 里那段最像迷宫的代码：</p>
<pre><code>from functools import lru_cache

@lru_cache
def get_settings() -> Settings:
    return Settings()</code></pre>
    <ul>
      <li><code>@lru_cache</code>：给函数加「记忆」。第一次 <code>get_settings()</code> 真建一个配置；之后再调用<strong>直接返回同一个对象</strong>，不再重复读 .env。</li>
      <li>好处：全项目共享唯一配置，读一次、处处用。</li>
    </ul>
<pre><code>a = get_settings()
b = get_settings()
print(a is b)   # True：同一个对象</code></pre>

    <div class="callout callout--pitfall">
      <span class="callout__label">踩坑</span>
      <p>
        <code>extra="ignore"</code> 只是忽略<strong>多出来的字段</strong>，不会隐藏类型错误——
        <code>app_port: int</code> 若 .env 给非数字，仍会抛校验异常。
        想安全读一个可能没设的变量，思维上等价于 <code>os.getenv(name, default)</code>——只是类型更聪明。
      </p>
    </div>

    <h2>配课怎么练</h2>
    <ol>
      <li>跑 <code>backend/37_config/37_config.py</code>（需先建好 <code>37_config/.env</code>）。</li>
      <li>终端跑一句 <code>python -c "import os; print(os.getenv(\"PATH\"))"</code>，亲眼看到环境变量（跟文件无关）。</li>
      <li>验证优先级：<code>.env</code> 写 <code>app_port=8801</code>，再设系统 <code>$env:APP_PORT=9000</code>，看谁赢。</li>
      <li>去掉 <code>.env</code> 再跑，看 app_port 回退默认 8800。</li>
      <li>对照打开 <code>my_family_gathering/config.py</code>，逐行认出本课内容。</li>
    </ol>

    <h2>收束</h2>
    <p>
      带走：<code>os</code> 是操作系统接口，最常用 <code>os.getenv</code>（读环境变量）与 <code>os.path</code>（拼路径）；
      但配置多了手写 <code>os.getenv</code> 太啰嗦，所以后端用 <code>BaseSettings</code>——声明一个类，
      读环境变量、读 .env、类型转换、默认值、校验全自动；
      <code>SettingsConfigDict(env_file=...)</code> 打开读 .env 的能力，<code>@lru_cache</code> 保证全局唯一。
    </p>
  </div>
</template>