from unittest import TestCase

from domain.entities.gold.gold_box_office import GoldBoxOffice
from domain.entities.gold.gold_financials import GoldFinancials
from domain.entities.gold.gold_movie_data import GoldMovieData
from domain.entities.silver.enumerations import BoxOfficeScope, Source
from domain.entities.silver.silver_box_office import SilverBoxOffice
from domain.entities.silver.silver_financials import SilverFinancials
from infrastructure.transformers.silver.box_office_metrics_silver_to_gold import (
    BoxOfficeMetricsSilverToGoldTransformer,
)


class BoxOfficeMetricsSilverToGoldTransformerTest(TestCase):
    def test_empty_list_returns_empty(self):
        transformer = BoxOfficeMetricsSilverToGoldTransformer()
        self.assertEqual(transformer.transform_entities([]), [])

    def test_silver_box_office_produces_movie_and_gold_box_office(self):
        silver = SilverBoxOffice(
            movie_title="Global Hit",
            release_year=2022,
            box_office_gross_usd=150_000_000.0,
            box_office_scope=BoxOfficeScope.INTERNATIONAL,
            data_source=Source.BOX_OFFICE_METRICS,
        )
        transformer = BoxOfficeMetricsSilverToGoldTransformer()
        out = transformer.transform_entities([silver])

        self.assertEqual(len(out), 2)
        gold_movie, gold_bo = out[0], out[1]
        self.assertIsInstance(gold_movie, GoldMovieData)
        self.assertIsInstance(gold_bo, GoldBoxOffice)
        self.assertIs(gold_movie.box_office_data, gold_bo)
        self.assertEqual(gold_movie.movie_title, "Global Hit")
        self.assertEqual(gold_movie.release_year, 2022)
        self.assertEqual(gold_bo.box_office_gross_usd, 150_000_000.0)
        self.assertEqual(gold_bo.box_office_scope, BoxOfficeScope.INTERNATIONAL)
        self.assertEqual(gold_bo.data_source, Source.BOX_OFFICE_METRICS)

    def test_silver_financials_produces_movie_and_gold_financials(self):
        silver = SilverFinancials(
            movie_title="Indie Gem",
            release_year=2021,
            production_budget_usd=5_000_000.0,
            marketing_spend_usd=1_250_000.0,
            data_source=Source.BOX_OFFICE_METRICS,
        )
        transformer = BoxOfficeMetricsSilverToGoldTransformer()
        out = transformer.transform_entities([silver])

        self.assertEqual(len(out), 2)
        gold_movie, gold_fin = out[0], out[1]
        self.assertIsInstance(gold_movie, GoldMovieData)
        self.assertIsInstance(gold_fin, GoldFinancials)
        self.assertIs(gold_movie.financials_data, gold_fin)
        self.assertEqual(gold_fin.production_budget_usd, 5_000_000.0)
        self.assertEqual(gold_fin.marketing_spend_usd, 1_250_000.0)
        self.assertEqual(gold_fin.data_source, Source.BOX_OFFICE_METRICS)

    def test_mixed_silver_types_in_one_batch(self):
        box = SilverBoxOffice(
            movie_title="A",
            release_year=2020,
            box_office_gross_usd=10.0,
            box_office_scope=BoxOfficeScope.DOMESTIC,
            data_source=Source.BOX_OFFICE_METRICS,
        )
        fin = SilverFinancials(
            movie_title="A",
            release_year=2020,
            production_budget_usd=1.0,
            marketing_spend_usd=2.0,
            data_source=Source.BOX_OFFICE_METRICS,
        )
        transformer = BoxOfficeMetricsSilverToGoldTransformer()
        out = transformer.transform_entities([box, fin])

        self.assertEqual(len(out), 4)
        self.assertIsInstance(out[0], GoldMovieData)
        self.assertIsInstance(out[1], GoldBoxOffice)
        self.assertIsInstance(out[2], GoldMovieData)
        self.assertIsInstance(out[3], GoldFinancials)
