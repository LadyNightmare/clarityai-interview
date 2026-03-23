from unittest import TestCase
from unittest.mock import patch

from infrastructure.extractors.box_office_metrics_movie_extractor import BoxOfficeMetricsMovieExtractor

class BoxOfficeMetricsMovieExtractorTest(TestCase):
    def test_get_movie_data(self):
        box_office_adapter = BoxOfficeMetricsMovieExtractor()
        movie_data = box_office_adapter.get_entities()
        self.assertIsNotNone(movie_data)

    @patch("infrastructure.extractors.box_office_metrics_movie_extractor.open")
    def test_movie_data_missing_file(self, mock_open):
        mock_open.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider3_domestic.csv"
        )
        box_office_adapter = BoxOfficeMetricsMovieExtractor()
        with self.assertRaises(Exception) as ctx:
            box_office_adapter.get_entities()
        self.assertIn("Error reading JSON file", str(ctx.exception))
        mock_open.assert_called_once()