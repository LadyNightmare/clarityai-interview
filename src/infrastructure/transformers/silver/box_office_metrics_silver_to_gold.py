from typing import Union

from domain.transformers.silver_to_gold_transformer import SilverToGoldTransformer
from domain.entities.silver.silver_box_office import SilverBoxOffice
from domain.entities.silver.silver_financials import SilverFinancials
from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.gold.gold_financials import GoldFinancials

SilverInput = Union[SilverBoxOffice, SilverFinancials]
GoldOutput = Union[GoldMovieData, GoldBoxOffice, GoldFinancials]


class BoxOfficeMetricsSilverToGoldTransformer(
    SilverToGoldTransformer[SilverInput, GoldOutput],
):
    def transform_entities(
        self,
        silver_entities: list[SilverInput],
    ) -> list[GoldOutput]:
        gold_entities = []
        for silver_entity in silver_entities:
            if isinstance(silver_entity, SilverBoxOffice):
                gold_box_office = GoldBoxOffice(
                    movie_title=silver_entity.movie_title,
                    release_year=silver_entity.release_year,
                    box_office_gross_usd=silver_entity.box_office_gross_usd,
                    box_office_scope=silver_entity.box_office_scope,
                    data_source=silver_entity.data_source,
                )
                gold_movie = GoldMovieData(
                    movie_title=silver_entity.movie_title,
                    release_year=silver_entity.release_year,
                    box_office_data=gold_box_office,
                )
                gold_entities.append(gold_movie)
                gold_entities.append(gold_box_office)
            elif isinstance(silver_entity, SilverFinancials):
                gold_financials = GoldFinancials(
                    movie_title=silver_entity.movie_title,
                    release_year=silver_entity.release_year,
                    production_budget_usd=silver_entity.production_budget_usd,
                    marketing_spend_usd=silver_entity.marketing_spend_usd,
                    data_source=silver_entity.data_source,
                )
                gold_movie = GoldMovieData(
                    movie_title=silver_entity.movie_title,
                    release_year=silver_entity.release_year,
                    financials_data=gold_financials,
                )
                gold_entities.append(gold_movie)
                gold_entities.append(gold_financials)
        return gold_entities