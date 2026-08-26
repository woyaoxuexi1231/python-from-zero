"""第 37 课配套：练习文件。

先建一个 .env（和本文件同目录，即 backend/37_config/.env）：
    app_port=8801
    gathering_title=中秋家庭聚餐

再跑：
    cd backend
    python 37_config/37_config_exercise.py

练习内容：
1. 观察阶段 2：.env 里的 APP_PORT=8801 是否盖过了默认 8800。
2. 观察阶段 3：app_port 此时应变成 8801（int），gathering_title 变成 .env 里的值。
3. 改一改 .env，或删掉它，再跑一次看回退到默认值。
"""

import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

# 1) os 读环境变量
print("os.getenv('APP_PORT')       ->", repr(os.getenv("APP_PORT", "8800")))

# 2) BaseSettings 读（自动类型转换 + 读 .env）
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_port: int = 8800
    gathering_title: str = "待定"


s = Settings()
print("s.app_port                 ->", s.app_port, type(s.app_port).__name__)
print("s.gathering_title          ->", s.gathering_title)