import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.box_office_metrics_bronze_movie import BoxOfficeMetricsBronzeMovie
from infrastructure.entities.enumerations import BoxOfficeScope

import csv

class BoxOfficeMetricsMovieExtractor(EntityExtractor[BoxOfficeMetricsBronzeMovie]):
    def get_entities(self) -> list[BoxOfficeMetricsBronzeMovie]:
        file_path_domestic = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_domestic.csv")
        file_path_international = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_international.csv")

        try:
            with open(file_path_domestic, newline="") as f:
                movie_data = csv.reader(f)
                header = next(movie_data)
                domestic_movies = [
                    BoxOfficeMetricsBronzeMovie(
                        film_name=str(movie[0]),
                        year_of_release=int(movie[1]),
                        box_office_gross_usd=float(movie[2]),
                        extractor_scope=BoxOfficeScope.DOMESTIC
                    )
                    for movie in movie_data
                ]
            with open(file_path_international, newline="") as f:
                movie_data = csv.reader(f)
                header = next(movie_data)
                international_movies = [
                    BoxOfficeMetricsBronzeMovie(
                        film_name=movie[0],
                        year_of_release=int(movie[1]),
                        box_office_gross_usd=float(movie[2]),
                        extractor_scope=BoxOfficeScope.INTERNATIONAL
                    )
                    for movie in movie_data
                ]
            return list(domestic_movies + international_movies)
        except FileNotFoundError as e:
            self._logger.error(f"Error reading JSON file: {e}")
            raise Exception(f"Error reading JSON file: {e}")
