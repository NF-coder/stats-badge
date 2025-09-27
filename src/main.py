import os

from renderer.renderer import RenderBuilder
from oklchUtils.OKLCHUtils import OKLCHUtils
from calc import Calc

from fetcher.fetcher import FetchLangStats

# Fetch info
USERNAME = os.environ['USERNAME']
TOKEN = os.environ['GITHUB_TOKEN']

# Plane settings
HEIGHT: int = 140
WIDTH: int = 250

# Captions settings
LEGEND_MARGIN_X: int = 140
LEGEND_MARGIN_Y: int = 30
SPACE_BETWEEN_CAPTIONS: int = 22
FONT_COLOR: str = "#c1c1c1"

# Color settings
OKLCH_CHROMA: float = 0.099
OKLCH_LIGHTNESS: float = 0.636
OTHER_COLOR_CHROMA: float = 0.000

# Round sizes settings
OUTER_RADIUS: int = 55
THICKNESS: int = 12

# Margins settings
MARGIN_X: int = 20
MARGIN_Y: int = 15

# Arrays settings
TOP_K: int = 4

# Output filepath
OUTPUT_FILE: str = "./out.svg"

def get_langs_data(token: str):
    info = {}
    
    total_size = 0

    for elem in FetchLangStats(token).fetch_user(USERNAME):
        total_size += elem.size
        if elem.name not in info: info[elem.name] = elem.size
        else: info[elem.name] += elem.size

    return info.keys(), map(lambda x: x/total_size, info.values())

def truncate(langs_arr: list[tuple[float, str]], k: int):
    if len(langs_arr) <= k: return langs_arr
    return langs_arr[:k-1] + [(sum(map(lambda x: x[0], langs_arr[k-1:])), "Other")]

def main():
    NAMES_ARR, PERCENT_ARR = get_langs_data(TOKEN)

    sorted_percents = sorted([(percent, name) for percent,name in zip(PERCENT_ARR, NAMES_ARR)], key=lambda x: x[0], reverse=True)

    sorted_percents = truncate(sorted_percents, TOP_K)

    _ = Calc(
        outer_radius=OUTER_RADIUS,
        thickness=THICKNESS,
        percent_array=[elem[0] for elem in sorted_percents],
        sections_colors_array=OKLCHUtils.create_colors_array(
            length=len(sorted_percents),
            chroma=OKLCH_CHROMA,
            lightness=OKLCH_LIGHTNESS
        ),
        renderer=RenderBuilder(
            height=HEIGHT,
            width=WIDTH, 
            outer_radius=OUTER_RADIUS, 
            thickness=THICKNESS,
            margin_x=MARGIN_X,
            margin_y=MARGIN_Y, 
            legend_margin_x=LEGEND_MARGIN_X,
            legend_margin_y=LEGEND_MARGIN_Y, 
            space_between_captions=SPACE_BETWEEN_CAPTIONS,
            font_color=FONT_COLOR
        ),
        margin_x=MARGIN_X,
        margin_y=MARGIN_Y,
        names_array=[elem[1] for elem in sorted_percents]
    )

    with open(OUTPUT_FILE, "w+", encoding="utf-8-sig") as f:
        f.write(_())

if __name__ == '__main__':
    main()