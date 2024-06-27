from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str
    db_port: int


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


def load_config(path: str | None = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env('TOKEN'),
            admin_ids=list(map(int, env('ADMIN_IDS'))),
        ),
        db=DatabaseConfig(
            database=env('POSTGRES_DB'),
            db_host=env('POSTGRES_HOST'),
            db_password=env('POSTGRES_PASSWORD'),
            db_user=env('POSTGRES_USER'),
            db_port=int(env('POSTGRES_PORT'))
        ),
    )


config: Config = load_config('.env')
