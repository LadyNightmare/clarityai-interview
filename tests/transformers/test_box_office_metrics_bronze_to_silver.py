from unittest import TestCase

from domain.entities.silver.enumerations import Source
from infrastructure.entities.bronze.box_office_metrics_bronze_financials import (
    BoxOfficeMetricsBronzeMovieFinancials,
)
from infrastructure.entities.bronze.box_office_metrics_bronze_movie import (
    BoxOfficeMetricsBronzeMovie,
)
from domain.entities.silver.enumerations import BoxOfficeScope
from infrastructure.transformers.box_office_metrics_bronze_to_silver_box_office import (
    BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer,
)
from infrastructure.transformers.box_office_metrics_bronze_to_silver_financials import (
    BoxOfficeMetricsBronzeToSilverFinancialsTransformer,
)


class BoxOfficeMetricsBronzeToSilverBoxOfficeTransformerTest(TestCase):
    def test_transform_entity_preserves_scope_and_source(self):
        bronze = BoxOfficeMetricsBronzeMovie(
            film_name="Global Hit",
            year_of_release=2022,
            box_office_gross_usd=150_000_000.0,
            extractor_scope=BoxOfficeScope.INTERNATIONAL,
        )
        transformer = BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer()
        silver = transformer.transform_entity(bronze)

        self.assertEqual(silver.movie_title, "Global Hit")
        self.assertEqual(silver.release_year, 2022)
        self.assertEqual(silver.box_office_gross_usd, 150_000_000.0)
        self.assertEqual(silver.box_office_scope, BoxOfficeScope.INTERNATIONAL)
        self.assertEqual(silver.data_source, Source.BOX_OFFICE_METRICS)


class BoxOfficeMetricsBronzeToSilverFinancialsTransformerTest(TestCase):
    def test_transform_entity_maps_budget_fields(self):
        bronze = BoxOfficeMetricsBronzeMovieFinancials(
            film_name="Indie Gem",
            year_of_release=2021,
            production_budget_usd=5_000_000.0,
            marketing_spend_usd=1_250_000.0,
        )
        transformer = BoxOfficeMetricsBronzeToSilverFinancialsTransformer()
        silver = transformer.transform_entity(bronze)

        self.assertEqual(silver.movie_title, "Indie Gem")
        self.assertEqual(silver.release_year, 2021)
        self.assertEqual(silver.production_budget_usd, 5_000_000.0)
        self.assertEqual(silver.marketing_spend_usd, 1_250_000.0)
        self.assertEqual(silver.data_source, Source.BOX_OFFICE_METRICS)
