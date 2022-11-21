# reader.py
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

from typing import Any, List
from yuml.models import Serving, Ingredient, Step, Variant


def read(data: dict, key: str) -> Any:
    if key in data:
        value = data.get(key)
        if value:
            return value
    raise Exception(f"Missing or empty property for key '{key}' ...")


def read_servings(data: dict) -> List[Serving]:
    servings_data = read(data, 'servings')
    return [Serving(text=text) for text in servings_data]


def read_ingredients(data: dict) -> List[Ingredient]:
    ingredients_data = read(data, 'ingredients')
    ingredients = []
    for entry in ingredients_data:
        ingredients.extend([Ingredient(text=text, quantity=quantity) for text, quantity in entry.items()])
    return ingredients


def read_steps(data: dict) -> List[Step]:
    steps_data = read(data, 'steps')
    return [Step(text=text) for text in steps_data]


def read_variants(data: dict) -> List[Variant]:
    variants_data = read(data, 'variants')
    return [Variant(text=text) for text in variants_data]
