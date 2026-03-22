from dataclasses import dataclass
from domain.entities.gold.gold_entity import GoldEntity
from domain.entities.silver.enumerations import ScoreSource
from domain.entities.silver.enumerations import Source

@dataclass
class GoldScore(GoldEntity):
    score: float
    num_reviews: int
    score_source: ScoreSource
    data_source: Source