from __future__ import annotations

from enum import Enum

__all__ = ["GeoCity"]


class GeoCity(Enum):
    KRD = (
        45.04484,
        38.97603,
        "Krasnodar",
    )
    NN = (
        56.3333,
        44.0000,
        "Nizhny Novgorod",
    )
    MSK = (
        55.75222,
        37.61556,
        "Moscow",
    )
