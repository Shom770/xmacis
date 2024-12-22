"""Defines the different codes you can apply to `xmacis` to retrieve data at a station."""
from enum import Enum

__all__ = ["Element", "ElementType", "Interval", "Normal", "ReduceBy"]

from typing import Sequence


class ElementType(Enum):
    """An enum class used as a parameter for the `xmacis` wrapper to specify elements that should be returned."""

    MAXIMUM_TEMPERATURE = "maxt"
    MINIMUM_TEMPERATURE = "mint"
    AVERAGE_TEMPERATURE = "avgt"
    TEMPERATURE_AT_OBSERVATION = "obst"

    PRECIPITATION = "pcpn"
    SNOW = "snow"
    SNOW_DEPTH = "snwd"

    COOLING_DEGREE_DAYS = "cdd"
    HEATING_DEGREE_DAYS = "hdd"
    GROWING_DEGREE_DAYS = "gdd"


class Interval(Enum):
    """An enum class representing the intervals that data should be returned by xmacis."""

    DAILY = "dly"
    MONTHLY = "mly"
    YEARLY = "yly"


class ReduceBy(Enum):
    """An enum class representing the different ways you can reduce the heap of data into values."""

    MAXIMUM = "max"
    MINIMUM = "min"
    SUM = "sum"
    MEAN = "mean"
    STANDARD_DEVIATION = "stddev"
    LIST = "list"


class Normal(Enum):
    """An enum class representing the different types of normals that the user could use to differentiate the data."""
    CURRENT = 1
    FROM_1991 = 91
    DEPARTURE = "departure"
    DEPARTURE_1991 = "91departure"
    FROM_1981 = 81
    DEPARTURE_1981 = "81departure"


class Element:
    """Represents a complex element with intervals, reduce codes, etc."""

    def __init__(
        self,
        element_type: ElementType,
        *,
        interval: Interval | Sequence[int] | str = None,
        duration: str | int = None,
        normal: Normal | str | int = None,
        reduce_by: ReduceBy | str = None
    ):
        self.element_type = element_type
        self.interval = interval
        self.duration = duration
        self.normal = normal
        self.reduce_by = reduce_by

    def _build_dict(self, **kwargs):
        return {name: value for name, value in kwargs.items() if value is not None}

    def as_dict(self):
        return self._build_dict(
            name=self.element_type.value,
            interval=self.interval.value if isinstance(self.interval, Interval) else self.interval,
            duration=self.duration,
            normal=self.normal.value if isinstance(self.normal, Normal) else self.normal,
            reduce=self.reduce_by.value if isinstance(self.reduce_by, ReduceBy) else self.reduce_by
        )
