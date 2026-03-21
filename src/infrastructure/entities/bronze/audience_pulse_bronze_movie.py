from dataclasses import dataclass
from domain.entities.bronze.bronze_entity import BronzeEntity

@dataclass
class AudiencePulseBronzeMovie(BronzeEntity):
    title: str
    year: int
    audience_average_score: float
    total_audience_ratings: int
    domestic_box_office_gross: float