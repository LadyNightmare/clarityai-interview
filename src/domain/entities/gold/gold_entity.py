from dataclasses import dataclass
from abc import ABC

@dataclass
class GoldEntity(ABC):
    movie_title: str
    release_year: int