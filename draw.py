from __future__ import annotations
import os
import re
import time
import math
from PIL import Image, ImageOps
import curses


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def copy(self):
        return Point(self.x, self.y)

    def distance(self, other: Point) -> float:
        return math.sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)


def draw_label(stdscr, pos: Point, msg: str, color_pair=0):
    _, width = stdscr.getmaxyx()

    if color_pair == 0:
        stdscr.addstr(pos.y, max(pos.x, 0), msg[abs(min(pos.x, 0)):width])
    else:
        stdscr.addstr(pos.y, max(pos.x, 0), msg[abs(min(pos.x, 0)):width], color_pair)


def draw_label_centered(stdscr, y: int, msg: str, color_pair=0):
    _, width = stdscr.getmaxyx()
    draw_label(stdscr, Point((width // 2) - (len(msg) // 2), y), msg, color_pair)
