# models.py
#
# Copyright 2022 Patrick Eschenbach
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Serving:
    index: int
    text: str


@dataclass
class Ingredient:
    index: int
    text: str
    quantities: Dict[int, str]


@dataclass
class Step:
    index: int
    text: str


@dataclass
class Variant:
    index: int
    text: str


@dataclass
class Recipe:
    name: str
    servings: List[Serving]
    ingredients: List[Ingredient]
    steps: List[Step]
    variants: List[Variant]
    images: List[str]
