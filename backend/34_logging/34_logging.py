# ============================================================
# 第 34 课（知识讲解）：logging —— 用分级日志替代满屏 print
# 运行方式：python 34_logging/34_logging.py
# 配套练习：34_logging_exercise.py（自检，全是新场景）
# ============================================================
import logging
import sys

# 痛点：脚本越写越大，print 满天飞——分不清「正常信息」「警告」「出错」；
# 关掉调试输出要改一堆 print；想写进文件还得再包一层。
# logging 按级别过滤、统一格式、可挂多个输出目标（控制台 / 文件）。
print("========== 第34课 logging ==========\n")


# ---------- 1. 五级日志：谁更重要 ----------
print("【1】五个级别（数字越小越「啰嗦」）")
print("  DEBUG    =", logging.DEBUG, "   — 开发细节，默认不显示")
print("  INFO     =", logging.INFO, "    — 正常流程「做到了什么」")
print("  WARNING  =", logging.WARNING, " — 可疑但还能跑")
print("  ERROR    =", logging.ERROR, "   — 出错，功能失败")
print("  CRITICAL =", logging.CRITICAL, "— 致命，可能要停")


# ---------- 2. 最小用法：getLogger + info ----------
print("\n【2】别 print，用 logger")
logger = logging.getLogger("demo")          # 名字随意，模块里常用 __name__
logger.info("程序启动")                     # 默认 WARNING 以上才显示 → 这条看不见
print("  未配置时 info 不显示（默认级别 WARNING）")


# ---------- 3. basicConfig：一次性配根 logger ----------
print("\n【3】basicConfig：级别 + 格式")
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(message)s",
    stream=sys.stdout,
)
root = logging.getLogger()
root.info("配置后 INFO 能看见了")           # INFO | 配置后 INFO 能看见了
root.debug("DEBUG 仍被过滤")                # 不输出
root.warning("注意磁盘快满了")              # WARNING | ...


# ---------- 4. 各级别长什么样 ----------
print("\n【4】同一脚本里打各级别")
log = logging.getLogger("levels")
log.setLevel(logging.DEBUG)                 # 这个 logger 单独降到 DEBUG
log.debug("调试：变量 x=42")
log.info("信息：读取了 100 条")
log.warning("警告：文件不存在，用默认")
log.error("错误：无法连接数据库")
log.critical("致命：配置缺失，退出")


# ---------- 5. 格式串里常用字段 ----------
print("\n【5】Formatter 字段")
fmt = logging.Formatter("%(asctime)s %(levelname)-8s %(name)s | %(message)s",
                        datefmt="%H:%M:%S")
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(fmt)
app_log = logging.getLogger("app")
app_log.handlers.clear()                  # 演示用：清掉继承的 handler 避免重复
app_log.addHandler(handler)
app_log.setLevel(logging.INFO)
app_log.propagate = False                   # 不往上冒泡，避免打两遍
app_log.info("带时间戳和 logger 名")


# ---------- 6. 按级别过滤：logger.setLevel ----------
print("\n【6】setLevel 决定「多啰嗦」")
worker = logging.getLogger("worker")
worker.setLevel(logging.WARNING)
worker.debug("细")                         # 被过滤
worker.info("常")                           # 被过滤
worker.warning("警")                        # 输出
worker.error("错")                          # 输出


# ---------- 7. 写进文件：FileHandler ----------
print("\n【7】同时打控制台和文件（演示 FileHandler 写法）")
file_logger = logging.getLogger("file_demo")
file_logger.setLevel(logging.INFO)
file_logger.handlers.clear()
file_logger.propagate = False

console_h = logging.StreamHandler(sys.stdout)
console_h.setFormatter(logging.Formatter("控制台 | %(message)s"))
file_h = logging.FileHandler("_demo_log.txt", encoding="utf-8")
file_h.setFormatter(logging.Formatter("%(asctime)s %(message)s"))

file_logger.addHandler(console_h)
file_logger.addHandler(file_h)
file_logger.info("这条会出现在控制台和 _demo_log.txt")
print("  （本课目录下会生成 _demo_log.txt，跑完可删）")


# ---------- 8. 和 argparse 联动：--verbose → DEBUG ----------
print("\n【8】承接第 33 课：verbose 开关调级别")
import argparse


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="带日志的问候")
    p.add_argument("name")
    p.add_argument("-v", "--verbose", action="store_true")
    return p


def setup_logging(verbose: bool) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(levelname)s | %(message)s",
        stream=sys.stdout,
        force=True,                             # Python 3.8+：重复 basicConfig 时重置
    )


def greet_with_log(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    setup_logging(args.verbose)
    log = logging.getLogger("greet")
    log.debug("verbose 模式：准备问候 %s", args.name)
    log.info("你好，%s", args.name)


greet_with_log(["Alice"])
greet_with_log(["Bob", "-v"])


# ---------- 9. 加餐：控制台彩色（ANSI） ----------
print("\n【9】控制台彩色：自定义 ColorFormatter")
# logging 本身不上色；终端认 ANSI 转义码（Win10+ / VS Code / Windows Terminal 一般可用）。
# 只给「控制台」Handler 上色；写文件仍用普通 Formatter，否则文件里会留下 \033[31m。

_COLORS = {
    logging.DEBUG:    "\033[36m",   # 青
    logging.INFO:     "\033[32m",   # 绿
    logging.WARNING:  "\033[33m",   # 黄
    logging.ERROR:    "\033[31m",   # 红
    logging.CRITICAL: "\033[35m",   # 紫
}
_RESET = "\033[0m"


class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        color = _COLORS.get(record.levelno, "")
        original = record.levelname
        record.levelname = f"{color}{original}{_RESET}"
        try:
            return super().format(record)
        finally:
            record.levelname = original          # 一定还原，避免污染后续 handler


color_log = logging.getLogger("color")
color_log.handlers.clear()
color_log.propagate = False
color_log.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(ColorFormatter("%(levelname)-8s | %(message)s"))
color_log.addHandler(ch)
color_log.debug("调试")
color_log.info("正常")
color_log.warning("警告")
color_log.error("出错")
color_log.critical("致命")
print("  （若终端无色：老版 CMD 可能不认 ANSI；可用 pip install colorama 再 colorama.init()）")


# ---------- 10. 易错点 ----------
print("\n【10】易错点速记")
print("  ① 模块里用 logger = logging.getLogger(__name__)，别到处 basicConfig")
print("  ② logger 名用 __name__ 能看清日志来自哪个文件")
print("  ③ 默认级别 WARNING —— info/debug 要先降 level 或 basicConfig")
print("  ④ 用 logger.info('x=%s', x) 而不是 f-string 拼接（懒格式化）")
print("  ⑤ basicConfig 只对根 logger 生效一次；重复调用常被忽略 → force=True")
print("  ⑥ 测试时用 StringIO + Handler 捕获，别靠肉眼看控制台")
print("  ⑦ 彩色只挂控制台 Handler；FileHandler 用普通 Formatter")


# ---------- 一句话小抄 ----------
print("\n========== 小抄 ==========")
print("logging.getLogger(__name__)     —— 拿 logger")
print("logging.DEBUG / INFO / WARNING  —— 级别常量")
print("logger.debug/info/warning/error —— 打日志")
print("basicConfig(level=, format=)    —— 脚本入口配一次")
print("Handler + Formatter             —— 自定义输出目标与格式")
print("ColorFormatter + ANSI           —— 控制台按级别上色")
print("verbose → level=DEBUG           —— 和 argparse 搭配")
