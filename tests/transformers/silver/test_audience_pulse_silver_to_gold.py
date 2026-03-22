from unittest import TestCase

from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.gold.gold_score import GoldScore
from domain.entities.silver.enumerations import (
    BoxOfficeScope,
    ScoreSource,
    Source,
)
from domain.entities.silver.silver_box_office import SilverBoxOffice
from domain.entities.silver.silver_score import SilverScore
from infrastructure.transformers.silver.audience_pulse_silver_to_gold import (
    AudiencePulseSilverToGoldTransformer,
)


class AudiencePulseSilverToGoldTransformerTest(TestCase):
    def test_empty_list_returns_empty(self):
        transformer = AudiencePulseSilverToGoldTransformer()
        self.assertEqual(transformer.transform_entities([]), [])

    def test_silver_score_branch(self):
        silver = SilverScore(
            movie_title="Crowd Pleaser",
            release_year=2023,
            score=4.5,
            score_source=ScoreSource.AUDIENCE,
            data_source=Source.AUDIENCE_PULSE,
            num_reviews=5000,
        )
        transformer = AudiencePulseSilverToGoldTransformer()
        out = transformer.transform_entities([silver])

        self.assertEqual(len(out), 2)
        gold_movie, gold_score = out[0], out[1]
        self.assertIsInstance(gold_movie, GoldMovieData)
        self.assertIsInstance(gold_score, GoldScore)
        self.assertIs(gold_movie.score_data, gold_score)
        self.assertEqual(gold_score.score_source, ScoreSource.AUDIENCE)
        self.assertEqual(gold_score.data_source, Source.AUDIENCE_PULSE)

    def test_silver_box_office_branch(self):
        silver = SilverBoxOffice(
            movie_title="Crowd Pleaser",
            release_year=2023,
            box_office_gross_usd=2_500_000.50,
            box_office_scope=BoxOfficeScope.DOMESTIC,
            data_source=Source.AUDIENCE_PULSE,
        )
        transformer = AudiencePulseSilverToGoldTransformer()
        out = transformer.transform_entities([silver])

        self.assertEqual(len(out), 2)
        gold_movie, gold_bo = out[0], out[1]
        self.assertIsInstance(gold_movie, GoldMovieData)
        self.assertIsInstance(gold_bo, GoldBoxOffice)
        self.assertIs(gold_movie.box_office_data, gold_bo)
        self.assertEqual(gold_bo.box_office_gross_usd, 2_500_000.50)
        self.assertEqual(gold_bo.box_office_scope, BoxOfficeScope.DOMESTIC)
        self.assertEqual(gold_bo.data_source, Source.AUDIENCE_PULSE)

    def test_mixed_inputs_preserve_order(self):
        score = SilverScore(
            movie_title="S",
            release_year=2020,
            score=9.0,
            score_source=ScoreSource.AUDIENCE,
            data_source=Source.AUDIENCE_PULSE,
            num_reviews=100,
        )
        box = SilverBoxOffice(
            movie_title="B",
            release_year=2019,
            box_office_gross_usd=1.0,
            box_office_scope=BoxOfficeScope.INTERNATIONAL,
            data_source=Source.AUDIENCE_PULSE,
        )
        transformer = AudiencePulseSilverToGoldTransformer()
        out = transformer.transform_entities([score, box])

        self.assertEqual(len(out), 4)
        self.assertIsInstance(out[0], GoldMovieData)
        self.assertIsInstance(out[1], GoldScore)
        self.assertIsInstance(out[2], GoldMovieData)
        self.assertIsInstance(out[3], GoldBoxOffice)
