from infrastructure.extractors.critic_agg_movie_extractor import CriticAggMovieExtractor

from infrastructure.extractors.audience_pulse_movie_extractor import AudiencePulseMovieExtractor
from infrastructure.extractors.box_office_metrics_movie_extractor import BoxOfficeMetricsMovieExtractor
from infrastructure.extractors.box_office_metrics_financials_extractor import (
    BoxOfficeMetricsMovieFinancialsExtractor,
)


from infrastructure.transformers.box_office_metrics_bronze_to_silver_box_office import BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer
from infrastructure.transformers.critic_agg_bronze_to_silver import CriticAggBronzeToSilverTransformer

from infrastructure.transformers.audience_pulse_bronze_to_silver_box_office import AudiencePulseBronzeToSilverBoxOfficeTransformer
from infrastructure.transformers.audience_pulse_bronze_to_silver_score import AudiencePulseBronzeToSilverScoreTransformer
from infrastructure.transformers.box_office_metrics_bronze_to_silver_financials import BoxOfficeMetricsBronzeToSilverFinancialsTransformer

if __name__ == "__main__":
    print("Critic Agg")
    critic_agg_extractor = CriticAggMovieExtractor()
    movie_data = critic_agg_extractor.get_entities()
    print(movie_data)
    print("--------------------------------")

    critic_agg_silver_transformer = CriticAggBronzeToSilverTransformer()
    for movie in movie_data:
        movie_info = critic_agg_silver_transformer.transform_entity(movie)
        print(movie_info)

    print("--------------------------------")

    print("Audience Pulse")

    audience_pulse_extractor = AudiencePulseMovieExtractor()
    movie_data = audience_pulse_extractor.get_entities()
    print(movie_data)
    print("--------------------------------")

    audience_pulse_silver_box_office_transformer = AudiencePulseBronzeToSilverBoxOfficeTransformer()
    for movie in movie_data:
        movie_info = audience_pulse_silver_box_office_transformer.transform_entity(movie)
        print(movie_info)

    audience_pulse_silver_score_transformer = AudiencePulseBronzeToSilverScoreTransformer()
    for movie in movie_data:
        movie_info = audience_pulse_silver_score_transformer.transform_entity(movie)
        print(movie_info)

    print("--------------------------------")

    print("Box Office Metrics")

    box_office_metrics_extractor = BoxOfficeMetricsMovieExtractor()
    movie_data = box_office_metrics_extractor.get_entities()
    print(movie_data)
    print("--------------------------------")

    box_office_metrics_silver_box_office_transformer = BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer()
    for movie in movie_data:
        movie_info = box_office_metrics_silver_box_office_transformer.transform_entity(movie)
        print(movie_info)

    box_office_metrics_financials_extractor = BoxOfficeMetricsMovieFinancialsExtractor()
    financials_data = box_office_metrics_financials_extractor.get_entities()
    print(financials_data)
    print("--------------------------------")

    box_office_metrics_silver_financials_transformer = BoxOfficeMetricsBronzeToSilverFinancialsTransformer()
    for movie in financials_data:
        movie_info = box_office_metrics_silver_financials_transformer.transform_entity(movie)
        print(movie_info)
