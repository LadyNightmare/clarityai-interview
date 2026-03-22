from domain.entities.bronze.bronze_entity import BronzeEntity
from domain.entities.silver.silver_entity import SilverEntity
from domain.transformers.bronze_to_silver_transformer import BronzeToSilverTransformer

class TransformBronzeToSilverUseCase:
    def __init__(self, bronze_to_silver_transformer: BronzeToSilverTransformer):
        self.__bronze_to_silver_transformer = bronze_to_silver_transformer

    def handle(self, bronze_entity: BronzeEntity) -> SilverEntity:
        return self.__bronze_to_silver_transformer.transform_entity(bronze_entity)