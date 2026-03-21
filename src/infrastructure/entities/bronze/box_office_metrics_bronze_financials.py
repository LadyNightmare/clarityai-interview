from dataclasses import dataclass
from domain.entities.bronze.bronze_entity import BronzeEntity

@dataclass
class BoxOfficeMetricsBronzeMovieFinancials(BronzeEntity):
    film_name: str
    year_of_release: int
    production_budget_usd: float
    marketing_spend_usd: float