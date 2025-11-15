from dataclasses import dataclass
from .coloring.OKLCHColoring import OKLCHColoring

@dataclass
class GeneralSettings:
    TOP_K: int
    PLANE: "PlaneSubsettings"
    COLORING: OKLCHColoring
    EXCLUDED_LANGUAGES: list[str]

@dataclass
class PlaneSubsettings:
    HEIGHT: int
    WIDTH: int