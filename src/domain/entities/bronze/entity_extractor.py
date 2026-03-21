from abc import ABC, abstractmethod

from domain.entities.bronze.bronze_entity import BronzeEntity
from typing import Generic, TypeVar
import logging

T = TypeVar('T', bound=BronzeEntity)

class EntityExtractor(ABC, Generic[T]):
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get_entities(self) -> list[T]:
        pass