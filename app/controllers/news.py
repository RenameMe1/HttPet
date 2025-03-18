"""Module work on news."""

from __future__ import annotations

import datetime
from typing import Protocol, TYPE_CHECKING, final

import aiohttp

from app.controllers.env import env

if TYPE_CHECKING:
    from typing import ClassVar

__all__ = [
    "INewsController",
    "NewsapiController",
]


class INewsController(Protocol):
    def __init__(self): ...
    def get_game_week_news(self): ...


@final
class NewsapiController:
    api_key: ClassVar = env.API_NEWSAPI_KEY
    news_url: ClassVar = "https://newsapi.org/v2/everything"

    def __init__(self) -> None: ...

    async def get_game_news_at_week(self):
        today = datetime.date.today()
        week_ago = today - datetime.timedelta(days=7)

        return await self._request_news(today, week_ago)

    async def _request_news(self, today, week_ago) -> list[dict[str, str]]:
        today = today.strftime("%Y-%m-%d")
        week_ago = week_ago.strftime("%Y-%m-%d")

        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.news_url,
                params=[
                    ("q", "pc game"),
                    ("from", "2025-03-09"),
                    ("to", "2025-03-16"),
                    ("sortBy", "popularity"),
                    ("apiKey", self.api_key),
                ],
            ) as response:
                response = await response.json()
                news = response["articles"]

        return self._changing_source_part(news)

    def _changing_source_part(self, news) -> list[dict[str, str]]:
        for the_new in news:
            the_new["source"] = the_new["source"]["name"]

        return news
