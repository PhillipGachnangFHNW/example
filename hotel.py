from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from room import Room

class Hotel:
    def __init__(self, name: str, stars: int):
        self._rooms: list[Room] = []
        self._name = name
        self._stars = stars
