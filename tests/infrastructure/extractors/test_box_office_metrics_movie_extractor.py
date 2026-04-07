from unittest import TestCase
from unittest.mock import mock_open, patch

from domain.entities.exceptions.formatting_error import FormattingError
from infrastructure.extractors.box_office_metrics_movie_extractor import BoxOfficeMetricsMovieExtractor


class BoxOfficeMetricsMovieExtractorTest(TestCase):
    @patch(
        "infrastructure.extractors.box_office_metrics_movie_extractor.open",
        new_callable=mock_open,
        read_data="film_name,year_of_release,box_office_gross_usd\nInception,2010,292576195\n",
    )
    def test_get_movie_data(self, _mock_file):
        box_office_adapter = BoxOfficeMetricsMovieExtractor()
        movie_data = box_office_adapter.get_entities()
        self.assertEqual(len(movie_data), 2)
        self.assertEqual(movie_data[0].film_name, "Inception")

    @patch("infrastructure.extractors.box_office_metrics_movie_extractor.open")
    def test_movie_data_missing_file(self, mock_file):
        mock_file.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider3_domestic.csv"
        )
        box_office_adapter = BoxOfficeMetricsMovieExtractor()
        with self.assertRaises(FileNotFoundError) as ctx:
            box_office_adapter.get_entities()
        self.assertIn("Error reading CSV file", str(ctx.exception))
        mock_file.assert_called_once()

    @patch(
        "infrastructure.extractors.box_office_metrics_movie_extractor.open",
        new_callable=mock_open,
        read_data="film_name,year_of_release,box_office_gross_usd\nInception,2010,not_a_number\n",
    )
    def test_movie_data_invalid_numeric_value_raises_formatting_error(self, _mock_file):
        box_office_adapter = BoxOfficeMetricsMovieExtractor()
        with self.assertRaises(FormattingError):
            box_office_adapter.get_entities()