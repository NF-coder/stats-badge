import yaml
from typing import Self

from .GeneralSettings import GeneralSettings, PlaneSubsettings
from .LegendSettings import LegendSettings
from .DiagramSettings import DiagramSettings
from .Coloring import *

class Settings:
    GENERAL_SETTINGS: GeneralSettings
    LEGEND_SETTINGS: LegendSettings
    DIAGRAM_SETTINGS: DiagramSettings

    @classmethod
    def from_yaml(cls, path: str) -> Self:
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)

        inst = cls()
        
        coloring = select_coloring(data["general"]["coloring"])

        inst.GENERAL_SETTINGS = GeneralSettings(
            data["general"]["top_k"],
            PlaneSubsettings(
                data["general"]["plane"]["height"],
                data["general"]["plane"]["width"]
            ),
            coloring,
            data["general"]["excluded_languages"]
        )

        inst.LEGEND_SETTINGS = LegendSettings(
            data["legend"]["margin_x"],
            data["legend"]["margin_y"],
            data["legend"]["space_between_captions"],
            data["legend"]["font_color"]
        )

        inst.DIAGRAM_SETTINGS = DiagramSettings(
            data["diagram"]["outer_radius"],
            data["diagram"]["thickness"],
            data["diagram"]["margin_x"],
            data["diagram"]["margin_y"]
        )

        return inst

def select_coloring(data: dict) -> OKLCHColoring | GithubColoring:
    t = data.get("type")
    if t == "oklch":
        return OKLCHColoring(data["chroma"], data["lightness"], data["other_color"])
    elif t == "github":
        return GithubColoring(data["other_color"])
    
    raise ValueError(f"Unknown coloring type: {t!r}")