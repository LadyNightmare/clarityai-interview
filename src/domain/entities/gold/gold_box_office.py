from dataclasses import dataclass
from domain.entities.silver.enumerations import BoxOfficeScope
from domain.entities.silver.enumerations import Source
from domain.entities.gold.gold_entity import GoldEntity

@dataclass
class GoldBoxOffice(GoldEntity):
    box_office_gross_usd: float
    box_office_scope: BoxOfficeScope
    data_source: Source