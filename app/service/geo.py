from __future__ import annotations

from enum import Enum

__all__ = ["GeoCity"]

type latitude = float
type longitude = float
type fullname = str


class GeoCity(Enum):
    KRD: tuple(latitude, longitude, fullname) = (
        45.04484,
        38.97603,
        "Krasnodar",
    )
    MSK: tuple(latitude, longitude, fullname) = (
        55.75222,
        37.61556,
        "Moscow",
    )
