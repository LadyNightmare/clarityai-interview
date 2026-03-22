from infrastructure.extractors.critic_agg_movie_extractor import CriticAggMovieExtractor

from infrastructure.extractors.audience_pulse_movie_extractor import AudiencePulseMovieExtractor
from infrastructure.extractors.box_office_metrics_movie_extractor import BoxOfficeMetricsMovieExtractor
from infrastructure.extractors.box_office_metrics_financials_extractor import (
    BoxOfficeMetricsMovieFinancialsExtractor,
)

from infrastructure.transformers.bronze.critic_agg_bronze_to_silver import CriticAggBronzeToSilverTransformer
from infrastructure.transformers.bronze.box_office_metrics_bronze_to_silver_financials import BoxOfficeMetricsBronzeToSilverFinancialsTransformer

from application.use_cases.extract_bronze_entities_use_case import ExtractBronzeEntitiesUseCase
from application.use_cases.transform_bronze_to_silver_use_case import TransformBronzeToSilverUseCase
from application.use_cases.transform_silver_to_gold_use_case import TransformSilverToGoldUseCase
from infrastructure.transformers.silver.critic_agg_silver_to_gold import CriticAggSilverToGoldTransformer
from infrastructure.transformers.silver.audience_pulse_silver_to_gold import AudiencePulseSilverToGoldTransformer
from infrastructure.transformers.silver.box_office_metrics_silver_to_gold import BoxOfficeMetricsSilverToGoldTransformer

from infrastructure.transformers.bronze.box_office_metrics_bronze_to_silver_box_office import BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer
from infrastructure.transformers.bronze.audience_pulse_bronze_to_silver_box_office import AudiencePulseBronzeToSilverBoxOfficeTransformer
from infrastructure.transformers.bronze.audience_pulse_bronze_to_silver_score import AudiencePulseBronzeToSilverScoreTransformer

if __name__ == "__main__":
    print("Critic Agg bronze entities\n")

    critic_agg_bronze_entities= ExtractBronzeEntitiesUseCase(CriticAggMovieExtractor()).handle()
    print(critic_agg_bronze_entities)
    print("\n")

    print("Critic Agg silver entities\n")
    critic_agg_silver_score = []
    for movie in critic_agg_bronze_entities:
        critic_agg_silver_score.append(TransformBronzeToSilverUseCase(CriticAggBronzeToSilverTransformer()).handle(movie))
    print(critic_agg_silver_score)
    print("\n")

    print("Critic Agg gold entities\n")
    critic_agg_gold_entities = TransformSilverToGoldUseCase(CriticAggSilverToGoldTransformer()).handle(critic_agg_silver_score)
    print(critic_agg_gold_entities)

    print("--------------------------------\n")

    print("Audience Pulse bronze entities\n")
    audience_pulse_bronze_entities = ExtractBronzeEntitiesUseCase(AudiencePulseMovieExtractor()).handle()
    print(audience_pulse_bronze_entities)
    print("\n")


    print("Audience Pulse silver entities\n")
    audience_pulse_silver_box_office = []
    for movie in audience_pulse_bronze_entities:
        audience_pulse_silver_box_office.append(TransformBronzeToSilverUseCase(AudiencePulseBronzeToSilverBoxOfficeTransformer()).handle(movie))
    print(audience_pulse_silver_box_office)
    print("\n")

    audience_pulse_silver_score = []
    for movie in audience_pulse_bronze_entities:
        audience_pulse_silver_score.append(TransformBronzeToSilverUseCase(AudiencePulseBronzeToSilverScoreTransformer()).handle(movie))
    print(audience_pulse_silver_score)
    print("\n")

    print("Audience Pulse gold entities\n")
    audience_pulse_gold_entities = TransformSilverToGoldUseCase(AudiencePulseSilverToGoldTransformer()).handle(audience_pulse_silver_score + audience_pulse_silver_box_office)
    print(audience_pulse_gold_entities)
    print("--------------------------------\n")

    print("Box Office Metrics bronze entities\n")
    box_office_metrics_bronze_box_office_entities = ExtractBronzeEntitiesUseCase(BoxOfficeMetricsMovieExtractor()).handle()
    print(box_office_metrics_bronze_box_office_entities)
    box_office_metrics_bronze_financials_entities = ExtractBronzeEntitiesUseCase(BoxOfficeMetricsMovieFinancialsExtractor()).handle()
    print(box_office_metrics_bronze_financials_entities)
    print("\n")

    print("Box Office Metrics silver entities\n")
    box_office_metrics_silver_box_office = []
    for movie in box_office_metrics_bronze_box_office_entities:
        box_office_metrics_silver_box_office.append(TransformBronzeToSilverUseCase(BoxOfficeMetricsBronzeToSilverBoxOfficeTransformer()).handle(movie))
    print(box_office_metrics_silver_box_office)
    print("\n")

    box_office_metrics_silver_financials = []
    for movie in box_office_metrics_bronze_financials_entities:
        box_office_metrics_silver_financials.append(TransformBronzeToSilverUseCase(BoxOfficeMetricsBronzeToSilverFinancialsTransformer()).handle(movie))
    print(box_office_metrics_silver_financials)
    print("\n")

    print("Box Office Metrics gold entities\n")
    box_office_metrics_gold_entities = TransformSilverToGoldUseCase(BoxOfficeMetricsSilverToGoldTransformer()).handle(box_office_metrics_silver_box_office + box_office_metrics_silver_financials)
    print(box_office_metrics_gold_entities)