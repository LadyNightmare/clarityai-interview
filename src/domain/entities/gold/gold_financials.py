from dataclasses import dataclass
from domain.entities.silver.enumerations import Source
from domain.entities.gold.gold_entity import GoldEntity

@dataclass
class GoldFinancials(GoldEntity):
    production_budget_usd: float
    marketing_spend_usd: float
    data_source: Source