from domain.entities.bronze.bronze_entity import BronzeEntity
from domain.entities.bronze.entity_extractor import EntityExtractor

class ExtractBronzeEntitiesUseCase:
    def __init__(self, bronze_entity_extractor: EntityExtractor):
        self.__bronze_entity_extractor = bronze_entity_extractor

    def handle(self) -> list[BronzeEntity]:
        return self.__bronze_entity_extractor.get_entities()