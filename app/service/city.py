"""Module work on weather."""
from __future__ import annotations

from typing import Protocol
import asyncio

import aiohttp

from app.service.geo import GeoCity, lat_type, lon_type

class CityProtocol(Protocol):
    def __init__(city: GeoCity): ...
    async def get_current_weather(): ...


class City:
    """Class work with API openweathermap.org."""
    __slots__ = [
        'city',
    ]

    weather_api: typing.ClassVar = 'https://api.openweathermap.org/data/2.5/weather'
    api_key: typing.ClassVar = '136c9d9a8cdbb0e521bb5283735b9740'

    def __init__(self, city: GeoCity):
        self.city = city

    async def get_current_weather(self):

        lat, lon = self.city.value
     
        return await self._request_weather_by_geo(lat, lon)

    async def _request_weather_by_geo(self, lat: lat_type, lon: lon_type):

        async with aiohttp.ClientSession() as session:
            async with session.get(
                    self.weather_api,
                    params = [
                            ('lat', lat), 
                            ('lon', lon),
                            ('appid', self.api_key),
                            ],
                    ) as response:

                response = await response.json()

                weather = response['weather'][0]

                return weather['description']

