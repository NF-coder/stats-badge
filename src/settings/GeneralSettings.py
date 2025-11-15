from dataclasses import dataclass
from .Coloring import *

@dataclass
class GeneralSettings:
    TOP_K: int
    PLANE: "PlaneSubsettings"
    COLORING: OKLCHColoring | GithubColoring
    EXCLUDED_LANGUAGES: list[str]

@dataclass
class PlaneSubsettings:
    HEIGHT: int
    WIDTH: int