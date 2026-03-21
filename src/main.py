from infrastructure.extractors.critic_agg_movie_extractor import CriticAggMovieExtractor

from infrastructure.extractors.audience_pulse_movie_extractor import AudiencePulseMovieExtractor
from infrastructure.extractors.box_office_metrics_movie_extractor import BoxOfficeMetricsMovieExtractor


if __name__ == "__main__":
    critic_agg_extractor = CriticAggMovieExtractor()
    movie_data = critic_agg_extractor.get_entities()
    print(movie_data)
    print("--------------------------------")

    audience_pulse_extractor = AudiencePulseMovieExtractor()
    movie_data = audience_pulse_extractor.get_entities()
    print(movie_data)
    print("--------------------------------")

    box_office_metrics_extractor = BoxOfficeMetricsMovieExtractor()
    movie_data = box_office_metrics_extractor.get_entities()
    print(movie_data)