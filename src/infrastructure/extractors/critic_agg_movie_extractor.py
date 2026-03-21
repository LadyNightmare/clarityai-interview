import csv
import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.critic_agg_bronze_movie import CriticAggBronzeMovie

class CriticAggMovieExtractor(EntityExtractor[CriticAggBronzeMovie]):
    def get_entities(self) -> list[CriticAggBronzeMovie]:
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider1.csv")
        try:
            with open(file_path, newline="") as f:
                movie_data = csv.reader(f)
                header = next(movie_data)
                return [
                    CriticAggBronzeMovie(
                        movie_title=str(movie[0]),
                        release_year=int(movie[1]),
                        critic_score_percentage=float(movie[2]),
                        top_critic_score=float(movie[3]),
                        total_critic_reviews_counted=int(movie[4]),
                    )
                    for movie in movie_data
                ]
        except FileNotFoundError as e:
            self._logger.error(f"Error reading CSV file: {e}")
            raise Exception(f"Error reading CSV file: {e}")