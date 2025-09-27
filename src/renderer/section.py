from dataclasses import dataclass

@dataclass
class Cordinate:
    x: int
    y: int

@dataclass
class Section:
    start_outer_cords: Cordinate
    finish_outer_cords: Cordinate
    finish_inner_cords: Cordinate
    start_inner_cords: Cordinate
    
    section_start_angle: float
    section_finish_angle: float

    color: str

    name: str

@dataclass
class PiechartInfo:
    inner_radius: int
    outer_radius: int

    center_x: int
    center_y: int

@dataclass
class CaptionInfo:
    margin_x: int
    margin_y: int
    space_between_captions: int
    font_color: str

@dataclass
class PlaneInfo:
    height: int
    width: int