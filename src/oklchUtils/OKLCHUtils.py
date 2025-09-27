from .oklchConv.OKLCHConverter import OKLCHConverter

class OKLCHUtils:
    @staticmethod
    def create_colors_array(length: int, chroma: float, lightness: float):
        return [
            OKLCHConverter.oklch_to_rgb(lightness, chroma, hue)
            for hue in range(0, 360, 360//length)
        ]