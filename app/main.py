"""__docs__"""

from __future__ import annotations

import asyncio

from app.service.geo import GeoCity
from app.service.city import City
from app.service.output import OutputProtocol, ExcelOutput


async def create_weather_tasks(*, output: OutputProtocol) -> None:
    tasks = _generate_asyncio_tasks()

    weathers = await asyncio.gather(*tasks)

    output.write(
        weathers,
        page="weather",
        columns=["wathter", "city"],
    )


def _generate_asyncio_tasks():
    tasks = list()

    for geo in GeoCity:
        city = City(geo)
        task = asyncio.create_task(city.get_current_weather())

        tasks.append(task)

    return tasks


if __name__ == "__main__":
    excel = ExcelOutput("output.xlsx")
    asyncio.run(create_weather_tasks(output=excel))
