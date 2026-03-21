from __future__ import annotations

from dataclasses import dataclass
from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.silver.enumerations import ScoreSource
from domain.entities.silver.enumerations import Source

@dataclass
class SilverScore(SilverEntity):
    score: float
    score_source: ScoreSource
    data_source: Source
    num_reviews: int
    score_percentage: float | None = None