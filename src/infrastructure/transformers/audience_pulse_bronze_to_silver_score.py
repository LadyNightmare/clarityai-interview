from domain.entities.silver.silver_score import SilverScore
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer
from domain.entities.silver.enumerations import ScoreSource, Source
from infrastructure.entities.bronze.audience_pulse_bronze_movie import AudiencePulseBronzeMovie


class AudiencePulseBronzeToSilverScoreTransformer(BronzeToSilverTransformer[AudiencePulseBronzeMovie, SilverScore]):
    def transform_entity(self, movie_data: AudiencePulseBronzeMovie) -> SilverScore:
        return SilverScore(
            movie_title=movie_data.title,
            release_year=movie_data.year,
            score=movie_data.audience_average_score,
            num_reviews=movie_data.total_audience_ratings,
            score_source=ScoreSource.AUDIENCE,
            data_source=Source.AUDIENCE_PULSE,
        )