import os

from domain.entities.bronze.bronze_entity import BronzeEntity
from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.audience_pulse_bronze_movie import AudiencePulseBronzeMovie
import json

class AudiencePulseMovieExtractor(EntityExtractor[AudiencePulseBronzeMovie]):
    def get_entities(self) -> list[AudiencePulseBronzeMovie]:
        file_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider2.json")
        try:
            with open(file_path, 'r') as f:
                movie_data = json.load(f)
                return [
                    AudiencePulseBronzeMovie(
                        title=str(movie['title']),
                        year=int(movie['year']),
                        audience_average_score=float(movie['audience_average_score']),
                        total_audience_ratings=int(movie['total_audience_ratings']),
                        domestic_box_office_gross=float(movie['domestic_box_office_gross']),
                    )
                    for movie in movie_data
                ]
        except FileNotFoundError as e:
            self._logger.error(f"Error reading JSON file: {e}")
            raise Exception(f"Error reading JSON file: {e}")