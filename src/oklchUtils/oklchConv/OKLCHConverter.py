from .utils.Converters import Converters
from .utils.Math import Math

class OKLCHConverter:
    @staticmethod    
    def oklch_to_rgb(l: float, c: float, h: float) -> str:
        """
        Конвертирует цвет из OKLCH в RGB

        Args:
            l: Lightness (0-1)
            c: Chroma (0-0.4+)
            h: Hue (0-360)

        Returns:
            Tuple[int, int, int]: RGB значения в диапазоне 0-255
        """
        # Конвертируем OKLCH в OKLab
        l, a, b = Converters.oklch_to_oklab(l, c, h)

        # Конвертируем OKLab в линейный sRGB
        r_linear, g_linear, b_linear = Converters.oklab_to_linear_srgb(l, a, b)

        # Применяем гамма-коррекцию
        r, g, b = Converters.linear_srgb_to_srgb(r_linear, g_linear, b_linear)

        # Ограничиваем значения и конвертируем в 0-255
        r = Math.clamp(r, 0, 1)
        g = Math.clamp(g, 0, 1)
        b = Math.clamp(b, 0, 1)

        return f"#{Math.math_rounding(r * 255):02x}{Math.math_rounding(g * 255):02x}{Math.math_rounding(b * 255):02x}"
