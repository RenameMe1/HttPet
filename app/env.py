from __future__ import annotations

import typing

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import ValidationError

all = [
    "env",
]


class _EnvVariable(BaseSettings):
    API_OPENWEATHER_KEY: typing.Annotated[
        str,
        ("API access key for openweathermap.org."),
    ]


class _EnvFileVariable(_EnvVariable):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def _define_variable_source():
    try:
        env = _EnvVariable()
    except ValidationError:
        env = _EnvFileVariable()

    return env


env = _define_variable_source()
