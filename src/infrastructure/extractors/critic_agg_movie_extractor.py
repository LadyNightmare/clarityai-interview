import csv
import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.critic_agg_bronze_movie import CriticAggBronzeMovie
from domain.entities.exceptions.formatting_error import FormattingError

class CriticAggMovieExtractor(EntityExtractor[CriticAggBronzeMovie]):
    def get_entities(self) -> list[CriticAggBronzeMovie]:
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider1.csv")
        try:
            with open(file_path, newline="") as f:
                movie_data = csv.DictReader(f)
                return [
                    CriticAggBronzeMovie(
                        movie_title=str(movie["movie_title"]),
                        release_year=int(movie["release_year"]),
                        critic_score_percentage=float(movie["critic_score_percentage"]),
                        top_critic_score=float(movie["top_critic_score"]),
                        total_critic_reviews_counted=int(movie["total_critic_reviews_counted"]),
                    )
                    for movie in movie_data
                ]
        except FileNotFoundError as e:
            self._logger.error(f"Error reading CSV file, file not found: {e}")
            raise FileNotFoundError(f"Error reading CSV file: {e}")
        except KeyError as e:
            self._logger.error(f"Error reading CSV file, key error: {e}")
            raise KeyError(f"Error reading CSV file: {e}")
        except ValueError as e:
            self._logger.error(f"Error reading CSV file, formatting error: {e}")
            raise FormattingError(f"Error reading CSV file: {e}")