# 第 33 课：argparse 命令行参数

`Python 从零` · 更新于 2026-08-25 · 标签：Python、入门

**摘要**：ArgumentParser、位置/可选参数、type/default、store_true、choices；用 parse_args(列表) 测 CLI，菜单升级成脚本入口。

---

第 7 课的 `while` 菜单适合人机交互；日常脚本更常是「一条命令跑完」： `python tool.py Alice --times 3`。 手拆 `sys.argv` 又脆又难写帮助信息。`argparse` 让你**声明**参数，它负责解析、类型转换和 `-h`。

## 这一课解决什么问题

- 位置参数（必填、按顺序）
- 可选参数（`--name` / `-n`、默认值、`type=`）
- 开关（`action="store_true"`）
- `choices` 限制取值
- 用 `parse_args([...])` 测脚本，不依赖真实命令行

## 最小例子

```python
import argparse

parser = argparse.ArgumentParser(description="打招呼")
parser.add_argument("name", help="要问候的人")
parser.add_argument("--times", type=int, default=1)

# 演示/测试：传入列表；真实运行时写 parse_args() 读命令行
args = parser.parse_args(["hulei", "--times", "2"])
print(args.name, args.times)   # hulei 2
```

> **原理**
>
> `parse_args` 返回 `Namespace`：用属性取值（`args.name`），不是字典。 `type=int` 写在 `add_argument` 里，解析时自动转换——别再手写 `int(args.times)`。

## 开关与 choices

```python
parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--mode", choices=["fast", "safe"], default="safe")

parser.parse_args([]).verbose          # False（没写开关）
parser.parse_args(["-v"]).verbose      # True
parser.parse_args(["--mode", "fast"]).mode  # "fast"
```

> **踩坑**
>
> 位置参数**没有** `--`，顺序固定；可选参数以 `-`/`--` 开头。 `--out-file` 在 Namespace 里变成 `args.out_file`（横杠变下划线）。 非法参数会 `SystemExit`——练习一律传合法 `argv`；正式工具靠 `python tool.py -h` 看帮助。

## 推荐骨架

```python
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="...")
    p.add_argument("name")
    p.add_argument("--times", type=int, default=1)
    return p

def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    # 用 args 干活…

if __name__ == "__main__":
    main()   # 真实命令行；测试时 main(["Alice", "--times", "2"])
```

## 配课怎么练

2. 先跑 `33_argparse.py`，对照输出，看清位置 / 可选 / 开关三种形态。
4. 再打开 `33_argparse_exercise.py`，6 题：加法、问候、echo、mode、copy、report。
6. 每题都用 `parse_args(argv)` 传列表；题 3/5/6 用到 `store_true`。

## 收束

带走骨架：`ArgumentParser` → `add_argument` → `parse_args` → `args.xxx`。 菜单适合交互，CLI 适合脚本；两种入口可以并存。 下一课是 `logging`（第 34 课，用分级日志替代满屏 print）。 也可以把 26～33 串起来做一次统一复习。

---

上一课：[第 32 课：re 正则表达式](32-re 正则表达式.md)　|　下一课：[第 34 课：logging 分级日志](34-logging 分级日志.md)
