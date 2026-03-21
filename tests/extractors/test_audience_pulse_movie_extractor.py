from unittest import TestCase
from unittest.mock import patch

from infrastructure.extractors.audience_pulse_movie_extractor import AudiencePulseMovieExtractor

class AudiencePulseMovieExtractorTest(TestCase):  
    def test_get_movie_data(self):
        audience_pulse_adapter = AudiencePulseMovieExtractor()
        movie_data = audience_pulse_adapter.get_entities()
        self.assertIsNotNone(movie_data)

    @patch("infrastructure.extractors.audience_pulse_movie_extractor.open")
    def test_movie_data_missing_file(self, mock_open):
        mock_open.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider2.json"
        )
        audience_pulse_adapter = AudiencePulseMovieExtractor()
        with self.assertRaises(Exception) as ctx:
            audience_pulse_adapter.get_entities()
        self.assertIn("Error reading JSON file", str(ctx.exception))
        mock_open.assert_called_once()