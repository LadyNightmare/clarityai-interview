import io
from unittest import TestCase
from unittest.mock import patch

from application.use_cases.extract_bronze_entities_use_case import ExtractBronzeEntitiesUseCase
from application.use_cases.transform_bronze_to_silver_use_case import (
    TransformBronzeToSilverUseCase,
)
from application.use_cases.transform_silver_to_gold_use_case import TransformSilverToGoldUseCase
from domain.entities.exceptions.formatting_error import FormattingError
from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.gold.gold_financials import GoldFinancials
from domain.entities.gold.gold_movie_data import GoldMovieData
from infrastructure.extractors.box_office_metrics_financials_extractor import (
    BoxOfficeMetricsMovieFinancialsExtractor,
)
from infrastructure.extractors.box_office_metrics_movie_extractor import (
    BoxOfficeMetricsMovieExtractor,
)
from infrastructure.transformers.bronze.box_office_metrics_bronze_to_silver_box_office import (
    BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer,
)
from infrastructure.transformers.bronze.box_office_metrics_bronze_to_silver_financials import (
    BoxOfficeMetricsBronzeToSilverFinancialsTransformer,
)
from infrastructure.transformers.silver.box_office_metrics_silver_to_gold import (
    BoxOfficeMetricsSilverToGoldTransformer,
)


class BoxOfficeMetricsPipelineAcceptanceTest(TestCase):
    def test_end_to_end_pipeline_with_controlled_input(self):
        domestic_csv = (
            "film_name,year_of_release,box_office_gross_usd\n"
            "Inception,2010,292576195\n"
        )
        international_csv = (
            "film_name,year_of_release,box_office_gross_usd\n"
            "Inception,2010,535700000\n"
        )
        financials_csv = (
            "film_name,year_of_release,production_budget_usd,marketing_spend_usd\n"
            "Inception,2010,160000000,100000000\n"
        )

        def _open_side_effect(file, *args, **kwargs):
            path = str(file)
            if path.endswith("provider3_domestic.csv"):
                return io.StringIO(domestic_csv)
            if path.endswith("provider3_international.csv"):
                return io.StringIO(international_csv)
            if path.endswith("provider3_financials.csv"):
                return io.StringIO(financials_csv)
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=_open_side_effect):
            bronze_box_office = ExtractBronzeEntitiesUseCase(
                BoxOfficeMetricsMovieExtractor()
            ).handle()
            bronze_financials = ExtractBronzeEntitiesUseCase(
                BoxOfficeMetricsMovieFinancialsExtractor()
            ).handle()

            silver_box_office = [
                TransformBronzeToSilverUseCase(
                    BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer()
                ).handle(movie)
                for movie in bronze_box_office
            ]
            silver_financials = [
                TransformBronzeToSilverUseCase(
                    BoxOfficeMetricsBronzeToSilverFinancialsTransformer()
                ).handle(movie)
                for movie in bronze_financials
            ]

            gold_entities = TransformSilverToGoldUseCase(
                BoxOfficeMetricsSilverToGoldTransformer()
            ).handle(silver_box_office + silver_financials)

        self.assertEqual(len(bronze_box_office), 2)
        self.assertEqual(len(bronze_financials), 1)
        self.assertEqual(len(silver_box_office), 2)
        self.assertEqual(len(silver_financials), 1)
        self.assertEqual(len(gold_entities), 6)

        self.assertEqual(
            sum(isinstance(entity, GoldMovieData) for entity in gold_entities), 3
        )
        self.assertEqual(
            sum(isinstance(entity, GoldBoxOffice) for entity in gold_entities), 2
        )
        self.assertEqual(
            sum(isinstance(entity, GoldFinancials) for entity in gold_entities), 1
        )

    def test_end_to_end_fails_on_malformed_financials_input(self):
        domestic_csv = (
            "film_name,year_of_release,box_office_gross_usd\n"
            "Inception,2010,292576195\n"
        )
        international_csv = (
            "film_name,year_of_release,box_office_gross_usd\n"
            "Inception,2010,535700000\n"
        )
        invalid_financials_csv = (
            "film_name,year_of_release,production_budget_usd,marketing_spend_usd\n"
            "Inception,2010,not_a_number,100000000\n"
        )

        def _open_side_effect(file, *args, **kwargs):
            path = str(file)
            if path.endswith("provider3_domestic.csv"):
                return io.StringIO(domestic_csv)
            if path.endswith("provider3_international.csv"):
                return io.StringIO(international_csv)
            if path.endswith("provider3_financials.csv"):
                return io.StringIO(invalid_financials_csv)
            raise FileNotFoundError(path)

        with patch("builtins.open", side_effect=_open_side_effect):
            with self.assertRaises(FormattingError):
                ExtractBronzeEntitiesUseCase(
                    BoxOfficeMetricsMovieFinancialsExtractor()
                ).handle()
