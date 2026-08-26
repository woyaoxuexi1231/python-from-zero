"""第 37 课配套：os 读配置 + BaseSettings 收编（知识文件）。

跑法：
    cd backend
    python 37_config/37_config.py
对照看：先手动 os.getenv，再用 pydantic-settings 收成一个类。
需先在 37_config/ 下建一个 .env（见 37_config_exercise.py 顶部的说明）。
"""

import os

from dotenv import load_dotenv  # pip install python-dotenv

print("=" * 50)
print("阶段 1：纯 os.getenv 读环境变量（不来自文件）")
print("=" * 50)
# os.getenv 只碰"系统环境变量表"，跟文件无关。
port = os.getenv("APP_PORT", "8800")
print("os.getenv('APP_PORT') ->", repr(port), "类型:", type(port).__name__)

print()
print("=" * 50)
print("阶段 2：load_dotenv 把 .env 装进环境变量")
print("=" * 50)
# pydantic-settings 的 env_file 底层做的就是这件事。
load_dotenv()  # 默认找当前文件夹的 .env
port2 = os.getenv("APP_PORT", "8800")
print("load_dotenv 后 os.getenv('APP_PORT') ->", repr(port2))
# 这里你可以看到，若存在 .env 且里面写了 APP_PORT，值会由 '8800' 变成 .env 里的值。

print()
print("=" * 50)
print("阶段 3：BaseSettings 一键收编（自动转 int + 读 .env + 默认值）")
print("=" * 50)
from pydantic_settings import BaseSettings, SettingsConfigDict  # noqa: E402


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",            # 读当前目录的 .env
        env_file_encoding="utf-8",  # UTF-8 读，中文不乱码
        extra="ignore",             # 多余的字段忽略，不报错
    )

    app_port: int = 8800            # 类型是 int，自动转换
    gathering_title: str = "待定"


settings = Settings()
print("app_port ->", repr(settings.app_port), "类型:", type(settings.app_port).__name__)
print("gathering_title ->", settings.gathering_title)

print()
print("=" * 50)
print("阶段 4：@lru_cache 全局唯一")
print("=" * 50)
from functools import lru_cache  # noqa: E402


@lru_cache
def get_settings() -> Settings:
    return Settings()


a = get_settings()
b = get_settings()
print("两次 get_settings() 是同一个对象? ->", a is b)  # True