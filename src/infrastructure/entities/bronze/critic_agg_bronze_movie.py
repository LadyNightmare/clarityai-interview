from dataclasses import dataclass
from domain.entities.bronze.bronze_entity import BronzeEntity

@dataclass
class CriticAggBronzeMovie(BronzeEntity):
    movie_title: str
    release_year: int
    critic_score_percentage: float
    top_critic_score: float
    total_critic_reviews_counted: int