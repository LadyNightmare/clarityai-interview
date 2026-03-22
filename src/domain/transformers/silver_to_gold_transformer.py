from abc import ABC, abstractmethod
from domain.entities.silver.silver_entity import SilverEntity
from domain.entities.gold.gold_entity import GoldEntity
from typing import Generic, TypeVar

T = TypeVar('T', bound=SilverEntity)
U = TypeVar('U', bound=GoldEntity)

class SilverToGoldTransformer(ABC, Generic[T, U]):
    @abstractmethod
    def transform_entities(self, silver_entities: list[T]) -> list[U]:
        pass