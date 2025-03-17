from __future__ import annotations

from enum import Enum

__all__ = ["GeoCity"]

type latitude = float
type longitude = float
type fullname = str

type geo_info = tuple(latitude, longitude, fullname)


class GeoCity(Enum):
    KRD: geo_info = (
        45.04484,
        38.97603,
        "Krasnodar",
    )
    NN: geo_info = (
        56.3333,
        44.0000,
        "Nizhny Novgorod",
    )
    MSK: geo_info = (
        55.75222,
        37.61556,
        "Moscow",
    )
