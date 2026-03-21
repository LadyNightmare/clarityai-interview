from abc import ABC, abstractmethod

from domain.entities.bronze.bronze_entity import BronzeEntity

from typing import Generic, TypeVar

from domain.entities.silver.silver_entity import SilverEntity

T = TypeVar('T', bound=BronzeEntity)
U = TypeVar('U', bound=SilverEntity)

class BronzeToSilverTransformer(ABC, Generic[T, U]):
    @abstractmethod
    def transform_entity(self, entity: T) -> U:
        pass
