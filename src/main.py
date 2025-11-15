import os
from dataclasses import dataclass

from renderer.renderer import RenderBuilder
from oklchUtils.OKLCHUtils import OKLCHUtils
from calc import Calc
from settings import Settings
from fetcher.fetcher import FetchLangStats

# Some settinga
USERNAME = os.environ['USERNAME']
TOKEN = os.environ['GITHUB_TOKEN']
OUTPUT_FILE: str = "./out.svg"
SETTINGS_FILE: str = "./settings.yaml"

SETTINGS = Settings.from_yaml(SETTINGS_FILE)


@dataclass
class LangData:
    name: str
    size: float
    github_color: str

def get_langs_data(
        token: str,
        username: str,
        exclude_langs: list[str] = SETTINGS.GENERAL_SETTINGS.EXCLUDED_LANGUAGES
    ) -> list[LangData]:
    info: dict[str, LangData] = {}
    total_size: float = 0

    for elem in FetchLangStats(token).fetch_user(username):
        if elem.name in exclude_langs: continue

        total_size += elem.size
        if elem.name not in info: info[elem.name] = LangData(elem.name, elem.size, elem.github_color)
        else: info[elem.name].size += elem.size

    return [LangData(
        info[k].name,
        info[k].size/total_size,
        info[k].github_color
    ) for k in info]

def truncate(langs_arr: list[LangData], k: int):
    if len(langs_arr) <= k: return langs_arr
    return langs_arr[:k-1] + [LangData("Other", sum(map(lambda x: x.size, langs_arr[k-1:])), SETTINGS.GENERAL_SETTINGS.COLORING.OTHER_COLOR)]

def coloring(sorted_percents: list[LangData]) -> list[str]:
    coloring_cfg = SETTINGS.GENERAL_SETTINGS.COLORING
    
    if coloring_cfg.TYPE == "oklch":
        if hasattr(coloring_cfg, "CHROMA") and hasattr(coloring_cfg, "LIGHTNESS"):
            return OKLCHUtils.create_colors_array(
                length=len(sorted_percents),
                chroma=getattr(coloring_cfg, "CHROMA"),
                lightness=getattr(coloring_cfg, "LIGHTNESS")
            )
        raise ValueError("Invalid oklch coloring config")
    elif coloring_cfg.TYPE == "github":
        return [elem.github_color for elem in sorted_percents]
    
    raise ValueError("No such coloring config")

def main():
    sorted_langs = sorted(
        get_langs_data(TOKEN, USERNAME),
        key=lambda x: x.size,
        reverse=True
    )

    sorted_percents = truncate(sorted_langs, SETTINGS.GENERAL_SETTINGS.TOP_K)

    _ = Calc(
        outer_radius=SETTINGS.DIAGRAM_SETTINGS.OUTER_RADIUS,
        thickness=SETTINGS.DIAGRAM_SETTINGS.THICKNESS,
        percent_array=[elem.size for elem in sorted_percents],
        sections_colors_array=coloring(sorted_percents),
        renderer=RenderBuilder(
            height=SETTINGS.GENERAL_SETTINGS.PLANE.HEIGHT,
            width=SETTINGS.GENERAL_SETTINGS.PLANE.WIDTH, 
            outer_radius=SETTINGS.DIAGRAM_SETTINGS.OUTER_RADIUS, 
            thickness=SETTINGS.DIAGRAM_SETTINGS.THICKNESS,
            margin_x=SETTINGS.DIAGRAM_SETTINGS.MARGIN_X,
            margin_y=SETTINGS.DIAGRAM_SETTINGS.MARGIN_Y, 
            legend_margin_x=SETTINGS.LEGEND_SETTINGS.MARGIN_X,
            legend_margin_y=SETTINGS.LEGEND_SETTINGS.MARGIN_Y, 
            space_between_captions=SETTINGS.LEGEND_SETTINGS.SPACE_BETWEEN_CAPTIONS,
            font_color=SETTINGS.LEGEND_SETTINGS.FONT_COLOR
        ),
        margin_x=SETTINGS.DIAGRAM_SETTINGS.MARGIN_X,
        margin_y=SETTINGS.DIAGRAM_SETTINGS.MARGIN_Y,
        names_array=[elem.name for elem in sorted_percents]
    )

    with open(OUTPUT_FILE, "w+", encoding="utf-8-sig") as f:
        f.write(_())

if __name__ == '__main__':
    main()