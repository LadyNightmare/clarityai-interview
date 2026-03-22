from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.gold.gold_entity import GoldEntity
from domain.transformers.silver_to_gold_transformer import SilverToGoldTransformer


class TransformSilverToGoldUseCase:
    def __init__(self, silver_to_gold_transformer: SilverToGoldTransformer):
        self.__silver_to_gold_transformer = silver_to_gold_transformer

    def handle(self, silver_entities: list[SilverEntity]) -> list[GoldEntity]:
        return self.__silver_to_gold_transformer.transform_entities(silver_entities)