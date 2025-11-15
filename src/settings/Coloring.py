from dataclasses import dataclass
from typing import Union

@dataclass
class OKLCHColoring():
    TYPE = "oklch"
    CHROMA: float
    LIGHTNESS: float
    OTHER_COLOR: str

@dataclass
class GithubColoring():
    TYPE = "github"
    OTHER_COLOR: str