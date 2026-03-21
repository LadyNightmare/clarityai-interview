from domain.entities.silver.silver_financials import SilverFinancials
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer
from infrastructure.entities.bronze.box_office_metrics_bronze_financials import (
    BoxOfficeMetricsBronzeMovieFinancials,
)
from domain.entities.silver.enumerations import Source

class BoxOfficeMetricsBronzeToSilverFinancialsTransformer(BronzeToSilverTransformer[BoxOfficeMetricsBronzeMovieFinancials, SilverFinancials]):
    def transform_entity(self, movie_data: BoxOfficeMetricsBronzeMovieFinancials) -> SilverFinancials:
        return SilverFinancials(
            movie_title=movie_data.film_name,
            release_year=movie_data.year_of_release,
            production_budget_usd=movie_data.production_budget_usd,
            marketing_spend_usd=movie_data.marketing_spend_usd,
            data_source=Source.BOX_OFFICE_METRICS,
        )