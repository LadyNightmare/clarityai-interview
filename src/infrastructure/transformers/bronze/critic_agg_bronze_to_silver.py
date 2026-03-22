from domain.entities.silver.silver_score import SilverScore
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer
from domain.entities.silver.enumerations import ScoreSource, Source
from infrastructure.entities.bronze.critic_agg_bronze_movie import CriticAggBronzeMovie

class CriticAggBronzeToSilverTransformer(BronzeToSilverTransformer[CriticAggBronzeMovie, SilverScore]):
    def transform_entity(self, movie_data: CriticAggBronzeMovie) -> SilverScore:
        return SilverScore(
            movie_title=movie_data.movie_title,
            release_year=movie_data.release_year,
            score=movie_data.top_critic_score,
            num_reviews=movie_data.total_critic_reviews_counted,
            score_source=ScoreSource.CRITIC ,
            data_source=Source.CRITIC_AGG,
            score_percentage=movie_data.critic_score_percentage,
        )