import yaml
from typing import Self

from .GeneralSettings import GeneralSettings, PlaneSubsettings
from .LegendSettings import LegendSettings
from .DiagramSettings import DiagramSettings
from .coloring.OKLCHColoring import OKLCHColoring

class Settings:
    GENERAL_SETTINGS: GeneralSettings
    LEGEND_SETTINGS: LegendSettings
    DIAGRAM_SETTINGS: DiagramSettings

    @classmethod
    def from_yaml(cls, path: str) -> Self:
        with open(path, 'r') as stream:
            data = yaml.safe_load(stream)

        inst = cls()
        
        inst.GENERAL_SETTINGS = GeneralSettings(
            data["general"]["top_k"],
            PlaneSubsettings(
                data["general"]["plane"]["height"],
                data["general"]["plane"]["width"]
            ),
            OKLCHColoring(
                data["general"]["coloring"]["chroma"],
                data["general"]["coloring"]["lightness"]
            ),
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