from renderer.renderer import IRenderer
from math import sin, cos, pi, degrees

class Math:
    @staticmethod
    def math_rounding(value: float) -> int:
        """Округление по правилам математики"""
        return int(value)+1 if value%1>0.5 else int(value)

class Calc:
    def __init__(
            self,
            outer_radius: int,
            thickness: int,
            percent_array: list[float],
            sections_colors_array: list[str],
            names_array: list[str],
            renderer: IRenderer,
            margin_x: int = 0,
            margin_y: int = 0,
        ) -> None:
        self._thickness = thickness
        self._outer_radius = outer_radius
        self._renderer = renderer
        self._margin_x = margin_x
        self._margin_y = margin_y
        self._percent_array = percent_array
        self._sections_colors_array = sections_colors_array
        self._inner_radius = outer_radius - thickness
        self._names_array = names_array
    
    def __call__(self) -> str:
        angle_accumulator = 0 # sum of all previous angles

        next_outer_curve_start_x = self._margin_x + self._outer_radius  # x-axis position of end of previous outer curve / start of new outer curve
        next_outer_curve_start_y = self._margin_y  # y-axis position of end of previous outer curve / start of new outer curve

        next_inner_curve_start_x = self._margin_x + self._outer_radius  # x-axis position of end of previous inner curve / start of new inner curve
        next_inner_curve_start_y = self._margin_y + self._thickness  # y-axis position of end of previous inner curve / start of new inner curve

        for percent,color,name in zip(self._percent_array, self._sections_colors_array, self._names_array):
            current_angle = 2*pi*percent + angle_accumulator

            outer_x = self._margin_x + self._outer_radius*(1+sin(current_angle))
            outer_y = self._margin_y + self._outer_radius*(1-cos(current_angle))
            inner_x = self._margin_x + self._thickness + self._inner_radius*(1+sin(current_angle))
            inner_y = self._margin_y + self._thickness + self._inner_radius*(1-cos(current_angle))

            self._renderer.add_section(
                (Math.math_rounding(next_outer_curve_start_x), Math.math_rounding(next_outer_curve_start_y)),
                (Math.math_rounding(outer_x), Math.math_rounding(outer_y)),
                (Math.math_rounding(inner_x), Math.math_rounding(inner_y)),
                (Math.math_rounding(next_inner_curve_start_x), Math.math_rounding(next_inner_curve_start_y)),
                section_start_angle=degrees(angle_accumulator),
                section_finish_angle=degrees(current_angle),
                color=color,
                name=name
            )
            
            # Updating all values
            angle_accumulator += 2*pi*percent
            next_outer_curve_start_x = outer_x
            next_outer_curve_start_y = outer_y
            next_inner_curve_start_x = inner_x
            next_inner_curve_start_y = inner_y

        return self._renderer.render()
        