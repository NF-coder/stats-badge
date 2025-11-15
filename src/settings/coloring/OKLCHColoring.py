from dataclasses import dataclass

@dataclass
class OKLCHColoring():
    CHROMA: float
    LIGHTNESS: float
    TYPE = "oklvh"