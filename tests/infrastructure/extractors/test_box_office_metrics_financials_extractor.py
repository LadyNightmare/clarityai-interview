from unittest import TestCase
from unittest.mock import mock_open, patch

from domain.entities.exceptions.formatting_error import FormattingError
from infrastructure.extractors.box_office_metrics_financials_extractor import (
    BoxOfficeMetricsMovieFinancialsExtractor,
)


class BoxOfficeMetricsFinancialsMovieExtractorTest(TestCase):
    @patch(
        "infrastructure.extractors.box_office_metrics_financials_extractor.open",
        new_callable=mock_open,
        read_data=(
            "film_name,year_of_release,production_budget_usd,marketing_spend_usd\n"
            "Inception,2010,160000000,100000000\n"
        ),
    )
    def test_get_movie_data_maps_fields_from_headers(self, _mock_file):
        box_office_adapter = BoxOfficeMetricsMovieFinancialsExtractor()
        movie_data = box_office_adapter.get_entities()

        self.assertEqual(len(movie_data), 1)
        self.assertEqual(movie_data[0].film_name, "Inception")
        self.assertEqual(movie_data[0].year_of_release, 2010)
        self.assertEqual(movie_data[0].production_budget_usd, 160000000.0)
        self.assertEqual(movie_data[0].marketing_spend_usd, 100000000.0)

    @patch(
        "infrastructure.extractors.box_office_metrics_financials_extractor.open",
        new_callable=mock_open,
        read_data=(
            "film_name,year_of_release,production_budget_usd\n"
            "Inception,2010,160000000\n"
        ),
    )
    def test_get_movie_data_missing_required_header_raises_key_error(self, _mock_file):
        box_office_adapter = BoxOfficeMetricsMovieFinancialsExtractor()

        with self.assertRaises(KeyError) as ctx:
            box_office_adapter.get_entities()

        self.assertIn("marketing_spend_usd", str(ctx.exception))

    @patch(
        "infrastructure.extractors.box_office_metrics_financials_extractor.open",
        new_callable=mock_open,
        read_data=(
            "film_name,year_of_release,production_budget_usd,marketing_spend_usd\n"
            "Inception,2010,not_a_number,100000000\n"
        ),
    )
    def test_get_movie_data_invalid_numeric_value_raises_formatting_error(self, _mock_file):
        box_office_adapter = BoxOfficeMetricsMovieFinancialsExtractor()

        with self.assertRaises(FormattingError):
            box_office_adapter.get_entities()

    @patch("infrastructure.extractors.box_office_metrics_financials_extractor.open")
    def test_movie_data_missing_file(self, mock_file):
        mock_file.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider3_financials.csv"
        )
        box_office_adapter = BoxOfficeMetricsMovieFinancialsExtractor()

        with self.assertRaises(FileNotFoundError) as ctx:
            box_office_adapter.get_entities()

        self.assertIn("Error reading CSV file", str(ctx.exception))
        mock_file.assert_called_once()