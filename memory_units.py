from enum import Enum
from typing import NamedTuple


class InvalidSuffix(Exception):
    pass


class Scale(NamedTuple):
    power: int
    metric_suffix: str


SCALE_MAP = {
    "B": Scale(0, "B"),
    "K": Scale(1, "KB"),
    "M": Scale(2, "MB"),
    "G": Scale(3, "GB"),
    "T": Scale(4, "TB"),
    "P": Scale(5, "PB"),
    "E": Scale(6, "EB"),
    "Z": Scale(7, "ZB"),
}


class Unit(Enum):
    BASE = SCALE_MAP["B"]
    KILO = SCALE_MAP["K"]
    MEGA = SCALE_MAP["M"]
    GIGA = SCALE_MAP["G"]
    TERA = SCALE_MAP["T"]
    PETA = SCALE_MAP["P"]
    EXA = SCALE_MAP["E"]
    ZETA = SCALE_MAP["Z"]

    @staticmethod
    def from_suffix(suffix: str) -> "Unit":
        first_letter = suffix[0].upper()
        if first_letter not in SCALE_MAP:
            valid_suffixes = " ".join(
                scale.metric_suffix for scale in SCALE_MAP.values()
            )
            raise InvalidSuffix(f"{suffix}. Valid suffixes are: {valid_suffixes}")
        return Unit(SCALE_MAP[first_letter])
