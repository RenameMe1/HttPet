"""Module work on env variables."""

from __future__ import annotations

import typing

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import ValidationError

__all__ = [
    "env",
]


class _EnvVariables(BaseSettings):
    API_OPENWEATHER_KEY: typing.Annotated[
        str,
        ("API access key for openweathermap.org."),
    ]

    API_NEWSAPI_KEY: typing.Annotated[
        str,
        ("API access key for newsapi.org"),
    ]


class _DotEnvFileVariables(_EnvVariables):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


def _define_variable_source():
    try:
        env = _EnvVariables()
    except ValidationError:
        env = _DotEnvFileVariables()

    return env


env = _define_variable_source()
