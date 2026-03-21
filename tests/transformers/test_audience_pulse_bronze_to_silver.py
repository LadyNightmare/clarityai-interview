from unittest import TestCase

from domain.entities.silver.enumerations import ScoreSource, Source
from infrastructure.entities.bronze.audience_pulse_bronze_movie import (
    AudiencePulseBronzeMovie,
)
from domain.entities.silver.enumerations import BoxOfficeScope
from infrastructure.transformers.audience_pulse_bronze_to_silver_box_office import (
    AudiencePulseBronzeToSilverBoxOfficeTransformer,
)
from infrastructure.transformers.audience_pulse_bronze_to_silver_score import (
    AudiencePulseBronzeToSilverScoreTransformer,
)

class AudiencePulseBronzeToSilverScoreTransformerTest(TestCase):
    def test_transform_entity_maps_fields(self):
        bronze = AudiencePulseBronzeMovie(
            title="Crowd Pleaser",
            year=2023,
            audience_average_score=4.5,
            total_audience_ratings=5000,
            domestic_box_office_gross=1_000_000.0,
        )
        transformer = AudiencePulseBronzeToSilverScoreTransformer()
        silver = transformer.transform_entity(bronze)

        self.assertEqual(silver.movie_title, "Crowd Pleaser")
        self.assertEqual(silver.release_year, 2023)
        self.assertEqual(silver.score, 4.5)
        self.assertEqual(silver.num_reviews, 5000)
        self.assertEqual(silver.score_source, ScoreSource.AUDIENCE)
        self.assertEqual(silver.data_source, Source.AUDIENCE_PULSE)
        self.assertIsNone(silver.score_percentage)


class AudiencePulseBronzeToSilverBoxOfficeTransformerTest(TestCase):
    def test_transform_entity_maps_domestic_gross_and_scope(self):
        bronze = AudiencePulseBronzeMovie(
            title="Crowd Pleaser",
            year=2023,
            audience_average_score=4.5,
            total_audience_ratings=5000,
            domestic_box_office_gross=2_500_000.50,
        )
        transformer = AudiencePulseBronzeToSilverBoxOfficeTransformer()
        silver = transformer.transform_entity(bronze)

        self.assertEqual(silver.movie_title, "Crowd Pleaser")
        self.assertEqual(silver.release_year, 2023)
        self.assertEqual(silver.box_office_gross_usd, 2_500_000.50)
        self.assertEqual(silver.box_office_scope, BoxOfficeScope.DOMESTIC)
        self.assertEqual(silver.data_source, Source.AUDIENCE_PULSE)
