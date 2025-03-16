"""__docs__"""

from __future__ import annotations

import asyncio

from app.service.geo import GeoCity
from app.service.city import City
from app.service.news import News
from app.service.output import OutputProtocol, ExcelOutput


async def create_weather_tasks(*, output: OutputProtocol) -> None:
    tasks = _generate_asyncio_tasks()

    weathers = await asyncio.gather(*tasks)

    output.write(
        weathers,
        page="weather",
        columns=["wathter", "city"],
    )


async def create_news_task(*, output: OutputProtocol):
    news_api = News()

    news = await news_api.get_game_news_at_week()
    print(news)

    output.write(
        news,
        page="news",
        # columns[""],
    )


def _generate_asyncio_tasks():
    tasks = list()

    for geo in GeoCity:
        city = City(geo)
        task = asyncio.create_task(city.get_current_weather())

        tasks.append(task)

    return tasks


async def main():
    excel = ExcelOutput("output.xlsx")

    # await create_news_task(output=excel)
    await create_weather_tasks(output=excel)


if __name__ == "__main__":
    asyncio.run(main())
