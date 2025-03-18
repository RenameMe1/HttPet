import asyncio

import logging
from typing import Protocol

from app.controllers import (
    IOutputController,
    NewsapiController,
    CityController,
    UserController,
)
from app.core import GeoCity

__all__ = (
    "GeneralReportProtocol",
    "GeneralReportService",
)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class GeneralReportProtocol(Protocol):
    def __init__(self, *, output: IOutputController) -> None: ...
    async def generate(self) -> None: ...


class GeneralReportService:
    def __init__(self, *, output: IOutputController) -> None:
        self.output = output

    async def generate(self) -> None:
        """Generate asyncio tasks which make report."""
        tasks = (
            asyncio.create_task(self._generate_news_report()),
            asyncio.create_task(self._generate_weather_report()),
            asyncio.create_task(self._generate_user_report()),
        )

        await asyncio.gather(
            *tasks,
        )

    async def _generate_weather_report(self) -> None:
        """Generate asyncio tasks which get weather info."""
        tasks = self._generate_asyncio_tasks()

        weathers = await asyncio.gather(*tasks)

        return self._to_store(
            weathers,
            page="weather",
            columns=["wathter", "city"],
        )

    @staticmethod
    def _generate_asyncio_tasks():
        """Generate asyncio tasks from enum of GeoCity ."""
        tasks = list()

        for geo in GeoCity:
            city = CityController(geo)
            task = asyncio.create_task(city.get_current_weather())

            tasks.append(task)

        return tasks

    async def _generate_news_report(self) -> None:
        news_api = NewsapiController()

        news = await news_api.get_game_news_at_week()

        self._to_store(
            news,
            page="news",
        )

    async def _generate_user_report(self) -> None:
        user_api = UserController()
        users = await user_api.get_users(amount=50)

        self._to_store(
            users,
            page="users",
        )

    def _to_store(
        self,
        data,
        page: str,
        columns=None,
    ) -> None:
        """Store data using selected IOutputController."""
        logger.info(f"Write page: {page}")

        self.output.write(
            data,
            page=page,
            columns=columns,
        )
