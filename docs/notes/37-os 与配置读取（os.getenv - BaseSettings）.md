# 第 37 课：os 与配置读取（os.getenv / BaseSettings）

`Python 从零` · 更新于 2026-08-26 · 标签：Python、入门、配置

**摘要**：os 是什么、os.getenv / os.path 常用 API；手写配置的痛点 → pydantic-settings 的 BaseSettings：读 .env、类型转换校验、字段↔变量对应、优先级，配合 @lru_cache 全局唯一。

---

读 `config.py` 时撞见了 `os.getenv`，但你的课到现在没讲过 `os` 是啥。 这一课就从 `os` 模块讲起：它帮你**和操作系统打交道**——读环境变量、拼路径、建文件夹…… 明白了 `os`，再看后端常用的 `BaseSettings`（pydantic-settings）如何把这些重复劳动收进一个类里。

## 这一课解决什么问题

- `os` 模块是干嘛的、最常用哪几个 API
- `os.getenv` / `os.environ`：读环境变量
- `os.path`：拼路径、取目录、判断存在
- 为什么手写配置麻烦 → 引出 `BaseSettings`
- `SettingsConfigDict`、字段↔变量对应、取值优先级、`@lru_cache`

## Step 1：os 是什么

`os` 是标准库里的「操作系统接口」。Python 脚本跑在操作系统上，绕不开的杂活—— 当前在哪个目录、环境变量设了啥、某文件存不存在——都归 `os`（以及它的兄弟 `os.path`）管。 你大概率以后天天用。

## Step 2：读环境变量 os.getenv / os.environ

环境变量就是操作系统里的一堆「键=值」设置（比如 `PATH`、`HOME`）。Python 里最常见的两个读法：

```python
import os

# 1) os.getenv(名字, 默认值)：读不到就返回默认值，最常用
port = os.getenv("APP_PORT", "8800")
print(port)                  # '8800'（默认值）；若系统设了 APP_PORT 则返回那个值

# 2) os.environ：像字典一样的全局表，可读可改
print(os.environ.get("HOME", "/"))   # 取值，读不到给默认
print("PATH" in os.environ)          # 判断某个变量存不存在
```

> **原理**
>
> `os.getenv(name, default)` 本质是 `os.environ.get(name, default)` 的简写、 等价于 `os.environ[name] if name in os.environ else default`。 它**永远返回字符串**——所以要数字还得自己转 `int(...)`，这正是后面 BaseSettings 要改进的点。

## Step 3：拼路径 os.path 系列

写脚本常要定位文件。手拼字符串用 `"/"` 会水土不服（Windows 用反斜杠），`os.path` 帮你跨平台拼：

```python
import os

base = "/home/user/project"

# join：跨平台拼路径
data = os.path.join(base, "data", "my_gathering.json")
print(data)                     # 本机会用对的分隔符拼好

print(os.path.dirname(data))    # 取所在目录
print(os.path.basename(data))   # 取文件名
print(os.path.exists(data))     # 该路径是否存在
os.makedirs("a/b/c", exist_ok=True)   # 递归建目录，已存不报错
```

顺便一提：你在 `config.py` 里看到的 `Path`（来自 `pathlib`）是更现代的替代， 写法更像对象（`Path("a") / "b"`）。两者都能拼路径；课程里 `os.path` 是打基础， `pathlib` 第 20 课讲过。这条线先记住「python 有专门管路径的模块」。

## Step 4：手写配置的痛点

现在你能看懂这段最原始写法了。它的毛病很明显：

```python
import os

PORT = int(os.getenv("APP_PORT", "8800"))   # 转类型靠手动 int()
HOST = os.getenv("APP_HOST", "127.0.0.1")
TITLE = os.getenv("GATHERING_TITLE", "待定")
```

- 每个配置一行 `os.getenv`，配置多了全是样板
- 字符串 → 数字要手动 `int()`，忘写就出错
- 类型写错不会立刻报错

## Step 5：BaseSettings 一键收编配置

`pydantic-settings` 的 `BaseSettings` 就是来收拾上面这些毛病的： 把配置声明成一个类，它自动完成「读环境变量 + 读 .env + 类型转换 + 默认值 + 校验」。 它继承自 `pydantic` 的 `BaseModel`，所以拥有「类型注解 → 自动转换校验」的能力。

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",             # 额外去这个文件里读配置
        env_file_encoding="utf-8",   # 用 UTF-8 读，中文不乱码
        extra="ignore",              # 类里没声明的字段，.env 写了也忽略
    )

    app_port: int = 8800
    gathering_title: str = "待定"

s = Settings()
print(s.app_port)          # 类型是 int，不是字符串！自动转换好了
```

写死 `app_port: int`，pydantic 会把它读到的值自动转成整数，类型错了直接抛异常——你手写 `int(os.getenv(...))` 还不一定有这层保障。

## 关键澄清：环境变量 ≠ 配置文件（.env）

这里最容易绕，专门讲清楚：`os.getenv` 读的**不是配置文件**，而是**操作系统维护的一张「键=值」全局表**（环境变量表）。它不来自任何文件，来源是系统 / 用户 / shell 启动时加载的那些设置。

```python
import os
os.getenv("APP_PORT", "8800")   # 从"系统环境变量表"里读，跟文件没关系

# PowerShell 里先设一下再看：
# $env:APP_PORT = "9000"
# python -c "import os; print(os.getenv('APP_PORT'))"   # 9000
```

而 `.env` 是一行行 `键=值` 的**配置文件**。它不是环境变量本身； 要想 `os.getenv` 读到它，得先有个工具把 `.env` 读出来**装进环境变量表**。最常用的工具是 `python-dotenv`：

```python
from dotenv import load_dotenv   # pip install python-dotenv
import os

load_dotenv()                     # 读 .env → 塞进 os.environ
os.getenv("APP_PORT")             # 这时才能读到 .env 里的值
```

`BaseSettings` 里的 `env_file=".env"`，底层做的正是 `load_dotenv()` 这件事：读 .env → 放进环境变量 → 再去匹配字段。所以对你「像是读配置文件」，其实先变成环境变量再取值。整条线：

```text
读取优先顺序：
1. 真实环境变量（系统里已设）     ← os.getenv 只碰这一层
2. .env 文件（用工具读进环境变量表） ← BaseSettings 帮你做
3. 字段默认值
```

## 字段名 ↔ 环境变量名：怎么对上号

默认按**下划线风格、大小写不敏感**匹配：

| 字段 | 能命中的环境变量 |
| --- | --- |
| `app_host` | `APP_HOST` / `app_host` |
| `gathering_title` | `GATHERING_TITLE` / `gathering_title` |
| `cors_origins` | `CORS_ORIGINS`（值为 JSON 数组时自动解析成列表） |

`cors_origins: list[str]` 这种列表类型，pydantic 也会自动把 JSON 文本解析成 Python 列表。

## 取值优先级 & @lru_cache

一个字段最终取谁，按优先级：

```text
环境变量  >  你显式传的参数  >   .env 文件  >   字段默认值
```

所以系统里设了 `APP_PORT`，会压过 `.env` 和默认值。最后看 `config.py` 里那段最像迷宫的代码：

```python
from functools import lru_cache

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

- `@lru_cache`：给函数加「记忆」。第一次 `get_settings()` 真建一个配置；之后再调用**直接返回同一个对象**，不再重复读 .env。
- 好处：全项目共享唯一配置，读一次、处处用。

```python
a = get_settings()
b = get_settings()
print(a is b)   # True：同一个对象
```

> **踩坑**
>
> `extra="ignore"` 只是忽略**多出来的字段**，不会隐藏类型错误—— `app_port: int` 若 .env 给非数字，仍会抛校验异常。 想安全读一个可能没设的变量，思维上等价于 `os.getenv(name, default)`——只是类型更聪明。

## 配课怎么练

2. 跑 `backend/37_config/37_config.py`（需先建好 `37_config/.env`）。
4. 终端跑一句 `python -c "import os; print(os.getenv(\"PATH\"))"`，亲眼看到环境变量（跟文件无关）。
6. 验证优先级：`.env` 写 `app_port=8801`，再设系统 `$env:APP_PORT=9000`，看谁赢。
8. 去掉 `.env` 再跑，看 app_port 回退默认 8800。
10. 对照打开 `my_family_gathering/config.py`，逐行认出本课内容。

## 收束

带走：`os` 是操作系统接口，最常用 `os.getenv`（读环境变量）与 `os.path`（拼路径）； 但配置多了手写 `os.getenv` 太啰嗦，所以后端用 `BaseSettings`——声明一个类， 读环境变量、读 .env、类型转换、默认值、校验全自动； `SettingsConfigDict(env_file=...)` 打开读 .env 的能力，`@lru_cache` 保证全局唯一。

---

上一课：[第 36 课：HTTP 调用与暴露（标准库 vs 三方）](36-HTTP 调用与暴露（标准库 vs 三方）.md)　|　下一课：[Python 标准库地图：模块分级与学习顺序](Python 标准库地图.md)
