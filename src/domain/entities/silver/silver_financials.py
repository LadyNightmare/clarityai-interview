from dataclasses import dataclass
from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.silver.enumerations import Source


@dataclass
class SilverFinancials(SilverEntity):
    production_budget_usd: float
    marketing_spend_usd : float
    data_source: Source