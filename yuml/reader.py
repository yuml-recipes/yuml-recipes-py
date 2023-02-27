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

from typing import Any, List, Dict
from yuml.models import Serving, Ingredient, Step, Variant


def __read(data: dict, key: str, default: Any = None) -> Any:
    value = data.get(key, default)
    if value is not None:
        return value
    raise Exception(f"Missing or empty property for key '{key}' ...")


def __ensure_str(input: str) -> str:
    return str(input) if input else ''


def read_servings(data: dict) -> List[Serving]:
    servings_data = __read(data, 'servings', [])
    if len(servings_data) > 0:
        return [Serving(index=index, text=__ensure_str(text)) for index, text in enumerate(servings_data)]
    else:
        return [Serving(index=0, text='')]


def __determine_ingredient_text(entry: Any) -> str:
    if isinstance(entry, dict):
        for text, _ in entry.items():
            return __ensure_str(text)
    else:
        return __ensure_str(entry)


def __determine_ingredient_quantity(entry: Any, index: int) -> str:
    if isinstance(entry, dict):
        for _, quantity in entry.items():
            if isinstance(quantity, list):
                return quantity[index] if index < len(quantity) else 'Missing quantity!'
            else:
                return __ensure_str(quantity)
    else:
        return ''


def read_ingredients(data: dict, servings: List[Serving]) -> List[Ingredient]:
    ingredients_data = __read(data, 'ingredients')
    ingredients = []
    for index, entry in enumerate(ingredients_data):
        text = __determine_ingredient_text(entry)
        quantities: Dict[Serving, str] = dict()
        for serving in servings:
            quantities[serving.index] = __determine_ingredient_quantity(entry, serving.index)
        ingredients.append(Ingredient(index=index, text=text, quantities=quantities))
    return ingredients


def read_steps(data: dict) -> List[Step]:
    steps_data = __read(data, 'steps', [])
    return [Step(index=index, text=__ensure_str(text)) for index, text in enumerate(steps_data)]


def read_variants(data: dict) -> List[Variant]:
    variants_data = __read(data, 'variants', [])
    return [Variant(index=index, text=__ensure_str(text)) for index, text in enumerate(variants_data)]
