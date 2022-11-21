# test_recipes.py
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

import pytest
import yuml
from yaml.parser import ParserError


def test_reference_recipe():
    recipe = yuml.recipe_from_file('data/Chili con Carne.yuml')

    assert recipe.name == 'Chili con Carne'

    assert len(recipe.servings) == 1
    assert len(recipe.ingredients) == 11
    assert len(recipe.steps) == 11
    assert len(recipe.variants) == 2
    assert len(recipe.images) == 1

    assert recipe.ingredients[1].text == 'Rote Chilischoten'
    assert recipe.ingredients[1].quantity == '2 große'

    assert recipe.ingredients[5].text == 'Tomaten'
    assert recipe.ingredients[5].quantity == '3 Dosen (400g Füllmenge)'

    assert recipe.ingredients[10].text == 'Salz und Pfeffer'
    assert recipe.ingredients[10].quantity is None


def test_syntax_exception_recipe():
    with pytest.raises(yuml.YumlException) as exc_info:
        _ = yuml.recipe_from_file('data/parser_error.yuml')
    exception_raised = exc_info.value
    assert type(exception_raised.__cause__) == ParserError


def test_missing_section_recipe():
    with pytest.raises(yuml.YumlException) as exc_info:
        _ = yuml.recipe_from_file('data/missing_ingredients.yuml')
    exception_raised = exc_info.value
    assert str(exception_raised.__cause__) == "Missing or empty property for key 'ingredients' ..."
