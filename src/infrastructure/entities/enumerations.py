from enum import Enum, auto

class ScoreSource(Enum):
    AUDIENCE = auto()
    CRITIC = auto()

class Source(Enum):
    AUDIENCE_PULSE = auto()
    CRITIC_AGG = auto()
    BOX_OFFICE_METRICS = auto()

class BoxOfficeScope(Enum):
    DOMESTIC = auto()
    INTERNATIONAL = auto()