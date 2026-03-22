from unittest import TestCase

from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.gold.gold_score import GoldScore
from domain.entities.silver.enumerations import ScoreSource, Source
from domain.entities.silver.silver_score import SilverScore
from infrastructure.transformers.silver.critic_agg_silver_to_gold import (
    CriticAggSilverToGoldTransformer,
)


class CriticAggSilverToGoldTransformerTest(TestCase):
    def test_empty_list_returns_empty(self):
        transformer = CriticAggSilverToGoldTransformer()
        self.assertEqual(transformer.transform_entities([]), [])

    def test_single_silver_score_produces_gold_movie_and_score(self):
        silver = SilverScore(
            movie_title="Example Film",
            release_year=2024,
            score=8.2,
            score_source=ScoreSource.CRITIC,
            data_source=Source.CRITIC_AGG,
            num_reviews=120,
            score_percentage=87.5,
        )
        transformer = CriticAggSilverToGoldTransformer()
        out = transformer.transform_entities([silver])

        self.assertEqual(len(out), 2)
        gold_movie, gold_score = out[0], out[1]
        self.assertIsInstance(gold_movie, GoldMovieData)
        self.assertIsInstance(gold_score, GoldScore)
        self.assertIs(gold_movie.score_data, gold_score)
        self.assertEqual(gold_movie.movie_title, "Example Film")
        self.assertEqual(gold_movie.release_year, 2024)
        self.assertEqual(gold_score.movie_title, "Example Film")
        self.assertEqual(gold_score.release_year, 2024)
        self.assertEqual(gold_score.score, 8.2)
        self.assertEqual(gold_score.num_reviews, 120)
        self.assertEqual(gold_score.score_source, ScoreSource.CRITIC)
        self.assertEqual(gold_score.data_source, Source.CRITIC_AGG)

    def test_multiple_scores_repeat_movie_score_pairs(self):
        rows = [
            SilverScore(
                movie_title="A",
                release_year=2020,
                score=7.0,
                score_source=ScoreSource.CRITIC,
                data_source=Source.CRITIC_AGG,
                num_reviews=1,
            ),
            SilverScore(
                movie_title="B",
                release_year=2021,
                score=8.0,
                score_source=ScoreSource.CRITIC,
                data_source=Source.CRITIC_AGG,
                num_reviews=2,
            ),
        ]
        transformer = CriticAggSilverToGoldTransformer()
        out = transformer.transform_entities(rows)
        self.assertEqual(len(out), 4)
        self.assertIsInstance(out[0], GoldMovieData)
        self.assertIsInstance(out[1], GoldScore)
        self.assertIsInstance(out[2], GoldMovieData)
        self.assertIsInstance(out[3], GoldScore)
        self.assertEqual(out[1].movie_title, "A")
        self.assertEqual(out[3].movie_title, "B")
