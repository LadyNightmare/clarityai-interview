from dataclasses import dataclass
from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.silver.enumerations import BoxOfficeScope
from domain.entities.silver.enumerations import Source

@dataclass
class SilverBoxOffice(SilverEntity):
    box_office_gross_usd: float
    box_office_scope: BoxOfficeScope
    data_source: Source