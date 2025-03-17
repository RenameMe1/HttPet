"""Module work on the non-processor dependencies."""

from app.controllers.city import City, CityProtocol
from app.controllers.News import News, NewsProtocol
from app.controllers.output import ExcelOutput, OutputProtocol
from app.columns.env import env

__all__ = [
    "City",
    "CityProtocol",
    "News",
    "NewsProtocol",
    "ExcelOutput",
    "OutputProtocol",
    "env",
]
