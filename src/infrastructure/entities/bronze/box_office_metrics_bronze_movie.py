from dataclasses import dataclass
from domain.entities.bronze.bronze_entity import BronzeEntity
from domain.entities.silver.enumerations import BoxOfficeScope

@dataclass
class BoxOfficeMetricsBronzeMovie(BronzeEntity):
    film_name: str
    year_of_release: int
    box_office_gross_usd: float
    extractor_scope: BoxOfficeScope