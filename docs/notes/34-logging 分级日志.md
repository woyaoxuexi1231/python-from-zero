# 第 34 课：logging 分级日志

`Python 从零` · 更新于 2026-08-25 · 标签：Python、入门

**摘要**：DEBUG/INFO/WARNING/ERROR、getLogger、basicConfig、Handler+Formatter、ColorFormatter 上色；verbose 联动 argparse。

---

脚本越写越大，`print` 满天飞：分不清正常信息、警告还是出错； 想关掉调试输出要改一堆代码，想写进文件还得再包一层。 `logging` 按**级别**过滤、统一格式，可挂控制台和文件等多个输出。

## 这一课解决什么问题

- 五级日志：`DEBUG` / `INFO` / `WARNING` / `ERROR` / `CRITICAL`
- `getLogger(__name__)` 拿模块级 logger，别到处 `print`
- `basicConfig` 配级别与格式（脚本入口配一次）
- `Handler` + `Formatter`：自定义输出目标与时间戳格式
- 和 `argparse` 的 `-v` 联动：`verbose → DEBUG`
- 加餐：自定义 `ColorFormatter`，控制台按级别上色

## 最小例子

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)
logger.debug("细节")      # 默认看不见
logger.info("程序启动")   # INFO | 程序启动
logger.warning("注意")    # WARNING | 注意
```

> **原理**
>
> 级别数字越小越「啰嗦」：`DEBUG=10`、`INFO=20`、`WARNING=30`…… logger 设了 `setLevel(INFO)` 后，只有 `levelno ≥ 20` 的记录才会输出。 用 `logger.info("x=%s", x)` 懒格式化，别先 `f-string` 拼好再传。

## 和 argparse 搭配

```python
def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s | %(message)s", force=True)

# main 里：args.verbose 来自 -v / --verbose（第 33 课）
```

> **踩坑**
>
> 默认级别是 `WARNING`——`info`/`debug` 要先 `basicConfig` 或 `setLevel`。 `basicConfig` 多次调用常被忽略；Python 3.8+ 用 `force=True` 重置。 库代码里别 `basicConfig`，只 `getLogger(__name__)`，让调用方决定怎么配。

## 测试时捕获日志

```python
import io, logging

stream = io.StringIO()
handler = logging.StreamHandler(stream)
logger = logging.getLogger("test")
logger.handlers.clear()
logger.addHandler(handler)
logger.setLevel(logging.INFO)
logger.propagate = False

logger.info("你好")
text = stream.getvalue().strip()   # 拿到输出正文
```

## 加餐：控制台彩色

标准库不上色；终端认 ANSI（`\033[31m` 红、`\033[0m` 复位）。 继承 `Formatter`，按 `record.levelno` 给 `levelname` 包颜色即可。

```python
_COLORS = {
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
handler.setFormatter(ColorFormatter("%(levelname)-8s | %(message)s"))
```

> **踩坑**
>
> **只给控制台 Handler 上色**；`FileHandler` 用普通 Formatter，否则日志文件会留下转义码。 改完 `levelname` 必须还原。老版 CMD 可能无色，可用 `colorama`；省事库还有 `colorlog` / `rich`。

## 配课怎么练

2. 先跑 `34_logging.py`，对照各级别输出、`verbose` 与【9】彩色演示。
4. 再打开 `34_logging_exercise.py`，6 题：logger、级别映射、StringIO 捕获、过滤、问候日志。
6. 题 4/6 用 `StringIO` + `Handler`，不要 `basicConfig`。

## 收束

带走骨架：`getLogger` → `setLevel` → `info/warning/error`； 脚本入口 `basicConfig` 一次；需要文件再加 `FileHandler`； 控制台要彩色就挂 `ColorFormatter`。 下一课是 `pytest`（第 35 课，第三方，给函数写断言）。 也可以先把 26～34 串起来做一个小 CLI 工具复习。

---

上一课：[第 33 课：argparse 命令行参数](33-argparse 命令行参数.md)　|　下一课：[第 35 课：pytest 写断言](35-pytest 写断言.md)
