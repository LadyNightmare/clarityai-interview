from __future__ import annotations
from dataclasses import dataclass
from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.gold.gold_financials import GoldFinancials
from domain.entities.gold.gold_score import GoldScore
from domain.entities.gold.gold_entity import GoldEntity

@dataclass
class GoldMovieData(GoldEntity):
    box_office_data: GoldBoxOffice | None = None
    financials_data: GoldFinancials | None = None
    score_data: GoldScore | None = None