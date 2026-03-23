from unittest import TestCase
from unittest.mock import patch

from infrastructure.extractors.critic_agg_movie_extractor import CriticAggMovieExtractor

class CriticAggMovieExtractorTest(TestCase):
    def test_get_movie_data(self):
        critic_agg_adapter = CriticAggMovieExtractor()
        movie_data = critic_agg_adapter.get_entities()
        self.assertIsNotNone(movie_data)

    @patch("infrastructure.extractors.critic_agg_movie_extractor.open")
    def test_movie_data_missing_file(self, mock_open):
        mock_open.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider1.csv"
        )
        critic_agg_adapter = CriticAggMovieExtractor()
        with self.assertRaises(Exception) as ctx:
            critic_agg_adapter.get_entities()
        self.assertIn("Error reading CSV file", str(ctx.exception))
        mock_open.assert_called_once()
