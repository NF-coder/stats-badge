from math import cos,sin,radians

class Converters: 
    @staticmethod
    def oklch_to_oklab(l: float, c: float, h: float) -> tuple[float, float, float]:
        """
            Конвертирует OKLCH в OKLab
            
            Args:
                l (float): lightness from OKLCH color (0-1)
                c (float): chroma from OKLCH color (0-0.3)
                h (float): hue from OKLCH color (0-360)
            
            Returns:
                out: tuple of 3 floats: lightness (0-1), A-number (-0.4 - 0.4) and B-number (-0.4 - 0.4)
        """
        h_rad = radians(h)
        a = c * cos(h_rad)
        b = c * sin(h_rad)
        return l, a, b

    @staticmethod
    def oklab_to_linear_srgb(l: float, a: float, b: float) -> tuple[float, float, float]:
        """
            Конвертирует OKLab в linear-sRGB

            Args:
                l (float): lightness from OKLAB color (0-1)
                a (float): A-number from OKLAB color (-0.4 - 0.4)
                b (float): B-number from OKLAB color (-0.4 - 0.4)

            Returns:
                out: tuple of 3 floats: red (0-1), green (0-1) and blue(0-1)
        """
        # Матрица преобразования из OKLab в линейный LMS
        l_ = l + 0.3963377774 * a + 0.2158037573 * b
        m_ = l - 0.1055613458 * a - 0.0638541728 * b
        s_ = l - 0.0894841775 * a - 1.2914855480 * b

        # Обратное нелинейное преобразование LMS
        l = l_ * l_ * l_
        m = m_ * m_ * m_
        s = s_ * s_ * s_

        # Матрица преобразования из LMS в линейный RGB
        r = +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
        g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
        b = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

        return r, g, b

    @staticmethod
    def linear_srgb_to_srgb(r: float, g: float, b: float) -> tuple[float, float, float]:
        """
            Конвертирует linear-sRGB в sRGB

            Args:
                r (float): red component from linear-sRGB color (0-1)
                g (float): green component  from linear-sRGB color (0-1)
                b (float): blue component  from linear-sRGB color (0-1)

            Returns:
                out: tuple of 3 floats: red (0-1), green (0-1) and blue (0-1)
        """
        def gamma_correction(x: float) -> float:
            return 1.055 * (x ** (1/2.4)) - 0.055 if x >= 0.0031308 else 12.92 * x

        r = gamma_correction(r)
        g = gamma_correction(g)
        b = gamma_correction(b)

        return r, g, b