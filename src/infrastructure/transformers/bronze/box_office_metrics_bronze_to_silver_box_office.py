from domain.entities.silver.silver_box_office import SilverBoxOffice
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer
from infrastructure.entities.bronze.box_office_metrics_bronze_movie import BoxOfficeMetricsBronzeMovie
from domain.entities.silver.enumerations import Source

class BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer(BronzeToSilverTransformer[BoxOfficeMetricsBronzeMovie, SilverBoxOffice]):
    def transform_entity(self, movie_data: BoxOfficeMetricsBronzeMovie) -> SilverBoxOffice:
        return SilverBoxOffice(
            movie_title=movie_data.film_name,
            release_year=movie_data.year_of_release,
            box_office_gross_usd=movie_data.box_office_gross_usd,
            box_office_scope=movie_data.extractor_scope,
            data_source=Source.BOX_OFFICE_METRICS,
        )