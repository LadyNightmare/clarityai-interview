import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.box_office_metrics_bronze_financials import BoxOfficeMetricsBronzeMovieFinancials
import csv
from domain.entities.exceptions.formatting_error import FormattingError

class BoxOfficeMetricsMovieFinancialsExtractor(EntityExtractor[BoxOfficeMetricsBronzeMovieFinancials]):
    def get_entities(self) -> list[BoxOfficeMetricsBronzeMovieFinancials]:
        file_path_financial = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_financials.csv")
        try:
            with open(file_path_financial, newline="") as f:
                movie_data = csv.DictReader(f)
                return [
                    BoxOfficeMetricsBronzeMovieFinancials(
                        film_name=str(movie["film_name"]),
                        year_of_release=int(movie["year_of_release"]),
                        production_budget_usd=float(movie["production_budget_usd"]),
                        marketing_spend_usd=float(movie["marketing_spend_usd"]),
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
