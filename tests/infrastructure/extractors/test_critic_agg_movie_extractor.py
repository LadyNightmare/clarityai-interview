from unittest import TestCase
from unittest.mock import mock_open, patch

from domain.entities.exceptions.formatting_error import FormattingError
from infrastructure.extractors.critic_agg_movie_extractor import CriticAggMovieExtractor


class CriticAggMovieExtractorTest(TestCase):
    @patch(
        "infrastructure.extractors.critic_agg_movie_extractor.open",
        new_callable=mock_open,
        read_data=(
            "movie_title,release_year,critic_score_percentage,top_critic_score,total_critic_reviews_counted\n"
            "Inception,2010,87,8.1,450\n"
        ),
    )
    def test_get_movie_data(self, _mock_file):
        critic_agg_adapter = CriticAggMovieExtractor()
        movie_data = critic_agg_adapter.get_entities()
        self.assertEqual(len(movie_data), 1)
        self.assertEqual(movie_data[0].movie_title, "Inception")

    @patch("infrastructure.extractors.critic_agg_movie_extractor.open")
    def test_movie_data_missing_file(self, mock_file):
        mock_file.side_effect = FileNotFoundError(
            2, "No such file or directory", "provider1.csv"
        )
        critic_agg_adapter = CriticAggMovieExtractor()
        with self.assertRaises(FileNotFoundError) as ctx:
            critic_agg_adapter.get_entities()
        self.assertIn("Error reading CSV file", str(ctx.exception))
        mock_file.assert_called_once()

    @patch(
        "infrastructure.extractors.critic_agg_movie_extractor.open",
        new_callable=mock_open,
        read_data=(
            "movie_title,release_year,critic_score_percentage,top_critic_score,total_critic_reviews_counted\n"
            "Inception,2010,not_a_number,8.1,450\n"
        ),
    )
    def test_movie_data_invalid_numeric_value_raises_formatting_error(self, _mock_file):
        critic_agg_adapter = CriticAggMovieExtractor()
        with self.assertRaises(FormattingError):
            critic_agg_adapter.get_entities()
