from unittest import TestCase

from domain.entities.silver.enumerations import ScoreSource, Source
from infrastructure.entities.bronze.critic_agg_bronze_movie import CriticAggBronzeMovie
from infrastructure.transformers.critic_agg_bronze_to_silver import (
    CriticAggBronzeToSilverTransformer,
)


class CriticAggBronzeToSilverTransformerTest(TestCase):
    def test_transform_entity_maps_fields(self):
        bronze = CriticAggBronzeMovie(
            movie_title="Example Film",
            release_year=2024,
            critic_score_percentage=87.5,
            top_critic_score=8.2,
            total_critic_reviews_counted=120,
        )
        transformer = CriticAggBronzeToSilverTransformer()
        silver = transformer.transform_entity(bronze)

        self.assertEqual(silver.movie_title, "Example Film")
        self.assertEqual(silver.release_year, 2024)
        self.assertEqual(silver.score, 8.2)
        self.assertEqual(silver.num_reviews, 120)
        self.assertEqual(silver.score_source, ScoreSource.CRITIC)
        self.assertEqual(silver.data_source, Source.CRITIC_AGG)
        self.assertEqual(silver.score_percentage, 87.5)
