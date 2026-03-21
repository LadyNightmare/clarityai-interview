import os

from domain.entities.bronze.entity_extractor import EntityExtractor
from infrastructure.entities.bronze.box_office_metrics_bronze_financials import BoxOfficeMetricsBronzeMovieFinancials
import csv

class BoxOfficeMetricsMovieFinancialsExtractor(EntityExtractor[BoxOfficeMetricsBronzeMovieFinancials]):
    def get_entities(self) -> list[BoxOfficeMetricsBronzeMovieFinancials]:
        file_path_financial = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "provider3_financials.csv")
        try:
            with open(file_path_financial, newline="") as f:
                movie_data = csv.reader(f,)
                header = next(movie_data)
                return [
                    BoxOfficeMetricsBronzeMovieFinancials(
                        film_name=str(movie[0]) ,
                        year_of_release=int(movie[1]),
                        production_budget_usd=float(movie[2]),
                        marketing_spend_usd=float(movie[3]),
                    )
                    for movie in movie_data
                ]
        except FileNotFoundError as e:
            self._logger.error(f"Error reading JSON file: {e}")
            raise Exception(f"Error reading JSON file: {e}")
