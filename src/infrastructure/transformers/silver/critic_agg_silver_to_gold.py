from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.gold.gold_entity import GoldEntity
from domain.transformers.silver_to_gold_transformer import SilverToGoldTransformer
from domain.entities.silver.silver_score import SilverScore
from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.gold.gold_score import GoldScore
from domain.entities.gold.gold_box_office import GoldBoxOffice


class CriticAggSilverToGoldTransformer(SilverToGoldTransformer[list[SilverScore], list[GoldMovieData, GoldScore, GoldBoxOffice]]):
    def transform_entities(self, silver_entities: list[SilverScore]) -> list[GoldMovieData, GoldScore, GoldBoxOffice]:
        gold_entities = []
        for silver_entity in silver_entities:
            gold_score = GoldScore(
                movie_title=silver_entity.movie_title,
                release_year=silver_entity.release_year,
                score=silver_entity.score,
                num_reviews=silver_entity.num_reviews,
                score_source=silver_entity.score_source,
                data_source=silver_entity.data_source,
            )
            gold_movie = GoldMovieData(
                movie_title=silver_entity.movie_title,
                release_year=silver_entity.release_year,
                score_data=gold_score,
            )
            gold_entities.append(gold_movie)
            gold_entities.append(gold_score)       
        return gold_entities
