import asyncio

from typing import Protocol

from app.controllers import OutputProtocol, News, City
from app.core import GeoCity


class GeneralReportProtocol(Protocol):
    def __init__(self, *, output: OutputProtocol) -> None: ...
    async def generate(self) -> None: ...


class GeneralReportService:
    def __init__(self, *, output: OutputProtocol) -> None:
        self.output = output

    async def generate(self) -> None:
        """Generate asyncio tasks which make report."""
        task_news = asyncio.create_task(self._get_news())
        task_weather = asyncio.create_task(self._get_weather())
        task_user = asyncio.create_task(self._get_user())

        await asyncio.gather(
            task_news,
            task_weather,
            task_user,
        )

    async def _get_weather(self) -> None:
        """Generate asyncio tasks which get weather info."""
        tasks = self._generate_asyncio_tasks()

        weathers = await asyncio.gather(*tasks)

        return self._to_store(weathers, "weather", ["wathter", "city"])

    @staticmethod
    def _generate_asyncio_tasks():
        """Generate asyncio tasks from enum of GeoCity ."""
        tasks = list()

        for geo in GeoCity:
            city = City(geo)
            task = asyncio.create_task(city.get_current_weather())

            tasks.append(task)

        return tasks

    async def _get_news(self) -> None:
        news_api = News()

        news = await news_api.get_game_news_at_week()

        self._to_store(news, "news")

    def _to_store(
        self,
        data,
        page_name: str,
        columns=None,
    ) -> None:
        """Store data using selected OutputProtocol."""
        self.output(
            data,
            page=page_name,
            columns=columns,
        )

    async def _get_user(self) -> None: ...
