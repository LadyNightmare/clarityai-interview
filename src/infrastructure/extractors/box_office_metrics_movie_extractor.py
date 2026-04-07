import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.box_office_metrics_bronze_movie import BoxOfficeMetricsBronzeMovie
from domain.entities.silver.enumerations import BoxOfficeScope
from domain.entities.exceptions.formatting_error import FormattingError
import csv

class BoxOfficeMetricsMovieExtractor(EntityExtractor[BoxOfficeMetricsBronzeMovie]):
    def get_entities(self) -> list[BoxOfficeMetricsBronzeMovie]:
        file_path_domestic = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_domestic.csv")
        file_path_international = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_international.csv")

        try:
            with open(file_path_domestic, newline="") as f:
                movie_data = csv.DictReader(f)
                domestic_movies = [
                    BoxOfficeMetricsBronzeMovie(
                        film_name=str(movie["film_name"]),
                        year_of_release=int(movie["year_of_release"]),
                        box_office_gross_usd=float(movie["box_office_gross_usd"]),
                        extractor_scope=BoxOfficeScope.DOMESTIC
                    )
                    for movie in movie_data
                ]
            with open(file_path_international, newline="") as f:
                movie_data = csv.DictReader(f)
                international_movies = [
                    BoxOfficeMetricsBronzeMovie(
                        film_name=str(movie["film_name"]),
                        year_of_release=int(movie["year_of_release"]),
                        box_office_gross_usd=float(movie["box_office_gross_usd"]),
                        extractor_scope=BoxOfficeScope.INTERNATIONAL
                    )
                    for movie in movie_data
                ]
            return list(domestic_movies + international_movies)
        except FileNotFoundError as e:
            self._logger.error(f"Error reading CSV file, file not found: {e}")
            raise FileNotFoundError(f"Error reading CSV file: {e}")
        except KeyError as e:
            self._logger.error(f"Error reading CSV file, key error: {e}")
            raise KeyError(f"Error reading CSV file: {e}")
        except ValueError as e:
            self._logger.error(f"Error reading CSV file, formatting error: {e}")
            raise FormattingError(f"Error reading CSV file: {e}")
