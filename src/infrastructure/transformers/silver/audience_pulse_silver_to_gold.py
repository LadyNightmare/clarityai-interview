from domain.transformers.silver_to_gold_transformer import SilverToGoldTransformer
from domain.entities.silver.silver_score import SilverScore
from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.gold.gold_score import GoldScore
from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.silver.silver_box_office import SilverBoxOffice

class AudiencePulseSilverToGoldTransformer(SilverToGoldTransformer[list[SilverScore, SilverBoxOffice], list[GoldMovieData, GoldScore, GoldBoxOffice]]):
    def transform_entities(self, silver_entities: list[SilverScore, SilverBoxOffice]) -> list[GoldMovieData, GoldScore, GoldBoxOffice]:
        gold_entities = []
        for silver_entity in silver_entities:
            if isinstance(silver_entity, SilverScore):
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
            elif isinstance(silver_entity, SilverBoxOffice):
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
        return gold_entities