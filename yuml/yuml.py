# yuml.py
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

import yaml
from yuml.finder import find_images
from yuml.models import Recipe
from yuml.reader import read_servings, read_ingredients, read_steps, read_variants


class YumlException(Exception):
    """ The only exception type allowed to be thrown to consumer code. """


def read_yuml(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def recipe_from_file(file_path: str) -> Recipe:
    try:
        data = read_yuml(file_path)
        servings = read_servings(data)
        ingredients = read_ingredients(data)
        steps = read_steps(data)
        variants = read_variants(data)
        images = find_images(file_path)
        return Recipe(servings=servings, ingredients=ingredients, steps=steps, variants=variants, images=images)
    except Exception as e:
        raise YumlException(f'Encountered error while reading {file_path}.') from e
