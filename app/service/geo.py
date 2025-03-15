from __future__ import annotations

from enum import Enum

__all__ = [
    'GeoCity'
]

type lat_type = float
type lon_type = float

class GeoCity(Enum):
    KRD: tuple(lat_type, lon_type) = (45.04484, 38.97603)
    MSK: tuple(lat_type, lon_type) = (55.75222, 37.61556)