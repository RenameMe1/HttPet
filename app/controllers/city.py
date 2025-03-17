"""Module work on weather."""

from __future__ import annotations

from typing import Protocol, TYPE_CHECKING

import aiohttp

from app.core.geo import GeoCity
from app.controllers import env

if TYPE_CHECKING:
    import typing


class CityProtocol(Protocol):
    def __init__(self, city: GeoCity): ...
    async def get_current_weather(self): ...


class City:
    """Class work with API openweathermap.org."""

    __slots__ = [
        "city",
    ]

    weather_api: typing.ClassVar = "https://api.openweathermap.org/data/2.5/weather"
    api_key: typing.ClassVar = env.API_OPENWEATHER_KEY

    def __init__(self, city: GeoCity):
        self.city = city

    async def get_current_weather(self) -> tuple[str, str]:
        lat, lon, city_name = self.city.value

        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.weather_api,
                params=[
                    ("lat", lat),
                    ("lon", lon),
                    ("appid", self.api_key),
                ],
            ) as response:
                response = await response.json()

        weather = response["weather"][0]

        return (weather["description"], city_name)
