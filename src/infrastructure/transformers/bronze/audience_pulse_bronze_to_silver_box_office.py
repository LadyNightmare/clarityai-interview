from domain.entities.silver.silver_box_office import SilverBoxOffice
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer
from domain.entities.silver.enumerations import ScoreSource, Source
from infrastructure.entities.bronze.audience_pulse_bronze_movie import AudiencePulseBronzeMovie
from domain.entities.silver.enumerations import BoxOfficeScope


class AudiencePulseBronzeToSilverBoxOfficeTransformer(BronzeToSilverTransformer[AudiencePulseBronzeMovie, SilverBoxOffice]):
    def transform_entity(self, movie_data: AudiencePulseBronzeMovie) -> SilverBoxOffice:
        return SilverBoxOffice(
            movie_title=movie_data.title,
            release_year=movie_data.year,
            box_office_gross_usd=movie_data.domestic_box_office_gross,
            box_office_scope=BoxOfficeScope.DOMESTIC,
            data_source=Source.AUDIENCE_PULSE,
        )