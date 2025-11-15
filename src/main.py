import os

from renderer.renderer import RenderBuilder
from oklchUtils.OKLCHUtils import OKLCHUtils
from calc import Calc
from settings import Settings
from fetcher.fetcher import FetchLangStats

# Fetch info
USERNAME = os.environ['USERNAME']
TOKEN = os.environ['GITHUB_TOKEN']
OUTPUT_FILE: str = "./out.svg"
SETTINGS_FILE: str = "./settings.yaml"

SETTINGS = Settings.from_yaml(SETTINGS_FILE)

def get_langs_data(
        token: str,
        username: str,
        exclude_langs: list[str] = SETTINGS.GENERAL_SETTINGS.EXCLUDED_LANGUAGES
    ) -> dict[str, float]:
    info = {}
    total_size = 0

    for elem in FetchLangStats(token).fetch_user(username):
        if elem.name in exclude_langs: continue

        total_size += elem.size
        if elem.name not in info: info[elem.name] = elem.size
        else: info[elem.name] += elem.size

    return {k: info[k]/total_size for k in info} 

def truncate(langs_arr: list[tuple[float, str]], k: int):
    if len(langs_arr) <= k: return langs_arr
    return langs_arr[:k-1] + [(sum(map(lambda x: x[0], langs_arr[k-1:])), "Other")]

def main():
    languages_stats = get_langs_data(TOKEN, USERNAME)

    sorted_percents = sorted(
        [(percent, name) for percent,name in zip(languages_stats.values(), languages_stats.keys())],
        key=lambda x: x[0],
        reverse=True
    )

    sorted_percents = truncate(sorted_percents, SETTINGS.GENERAL_SETTINGS.TOP_K)

    _ = Calc(
        outer_radius=SETTINGS.DIAGRAM_SETTINGS.OUTER_RADIUS,
        thickness=SETTINGS.DIAGRAM_SETTINGS.THICKNESS,
        percent_array=[elem[0] for elem in sorted_percents],
        sections_colors_array=OKLCHUtils.create_colors_array(
            length=len(sorted_percents),
            chroma=SETTINGS.GENERAL_SETTINGS.COLORING.CHROMA,
            lightness=SETTINGS.GENERAL_SETTINGS.COLORING.LIGHTNESS
        ),
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
        names_array=[elem[1] for elem in sorted_percents]
    )

    with open(OUTPUT_FILE, "w+", encoding="utf-8-sig") as f:
        f.write(_())

if __name__ == '__main__':
    main()