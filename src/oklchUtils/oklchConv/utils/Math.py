class Math:
    @staticmethod
    def clamp(value: float, min_val: float = 0.0, max_val: float = 1.0) -> float:
        """Ограничивает значение в заданном диапазоне"""
        return max(min_val, min(max_val, value))
    
    @staticmethod
    def math_rounding(value: float) -> int:
        """Округление по правилам математики"""
        return int(value)+1 if value%1>0.5 else int(value)