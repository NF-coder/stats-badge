import jinja2
import pathlib

from renderer.section import Section, PlaneInfo, Cordinate, PiechartInfo, CaptionInfo

from typing import Self

from abc import ABCMeta, abstractmethod

class IRenderer(metaclass=ABCMeta):
    @abstractmethod
    def add_section(
        self,
        start_outer_cords: tuple[int, int],
        finish_outer_cords: tuple[int, int],
        finish_inner_cords: tuple[int, int],
        start_inner_cords: tuple[int, int],
        section_start_angle: float,
        section_finish_angle: float,
        color: str,
        name: str
    ) -> Self: pass

    @abstractmethod
    def render(
        self
    ) -> str: pass

class RenderBuilder(IRenderer):
    def __init__(
            self,
            # info about plane
            height: int,
            width: int,
            # info about piechart
            outer_radius: int,
            thickness: int,
            margin_x: int,
            margin_y: int,
            # info about font
            legend_margin_x: int,
            legend_margin_y: int,
            space_between_captions: int,
            font_color: str,
            # other
            path: str = "templates",
            template_filename: str = "template.html"
        ) -> None:
        TEMPLATE_DIR_PATH = pathlib.Path(__file__).parent / path
        self._planeInfo = PlaneInfo(height, width)
        self._piechartInfo = PiechartInfo(outer_radius-thickness, outer_radius, outer_radius+margin_x, outer_radius+margin_y)
        self._fontInfo = CaptionInfo(legend_margin_x, legend_margin_y, space_between_captions, font_color)
        self._JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR_PATH), trim_blocks=True)
        self._template_filename = template_filename
        self._sections_arr: list[Section] = []

    def add_section(
            self,
            start_outer_cords: tuple[int, int],
            finish_outer_cords: tuple[int, int],
            finish_inner_cords: tuple[int, int],
            start_inner_cords: tuple[int, int],
            section_start_angle: float,
            section_finish_angle: float,
            color: str,
            name: str
        ) -> Self:
        self._sections_arr.append(
            Section(
                start_outer_cords = Cordinate(*start_outer_cords),
                finish_outer_cords = Cordinate(*finish_outer_cords),
                finish_inner_cords = Cordinate(*finish_inner_cords),
                start_inner_cords = Cordinate(*start_inner_cords),
                color = color,
                section_start_angle = section_start_angle,
                section_finish_angle = section_finish_angle,
                name=name
            )
        )
        return self

    def render(self) -> str:
        template = self._JINJA_ENV.get_template(self._template_filename)
        return template.render(
            sections_array = self._sections_arr,
            plane_info = self._planeInfo,
            piechart_info = self._piechartInfo,
            caption_info = self._fontInfo
        )