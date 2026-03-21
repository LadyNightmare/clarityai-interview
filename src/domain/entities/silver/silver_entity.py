from dataclasses import dataclass
from abc import ABC

@dataclass
class SilverEntity(ABC):
    # These fields are the PK for each movie. It identifies the movie the 
    # data (score, financials, box office) belongs to.
    movie_title: str
    release_year: int