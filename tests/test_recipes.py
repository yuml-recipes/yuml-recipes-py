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

    assert len(recipe.servings) == 3
    assert len(recipe.ingredients) == 6
    assert len(recipe.steps) == 6
    assert len(recipe.variants) == 3
    assert len(recipe.images) == 1

    serving0 = recipe.servings[0]
    serving1 = recipe.servings[1]
    serving2 = recipe.servings[2]
    assert serving0.text == 'Menge für einen kleinen Topf'
    assert serving1.text == 'Menge für einen mittleren Topf'
    assert serving2.text == ''

    ingredient0 = recipe.ingredients[0]
    assert ingredient0.text == 'Hackfleisch vom Rind'
    assert ingredient0.quantities[serving0.index] == '200g'
    assert ingredient0.quantities[serving1.index] == '400g'
    assert ingredient0.quantities[serving2.index] == '600g'

    ingredient1 = recipe.ingredients[1]
    assert ingredient1.text == 'Zwiebeln'
    assert ingredient1.quantities[serving0.index] == 'Eine Große'
    assert ingredient1.quantities[serving1.index] == 'Zwei Große'
    assert ingredient1.quantities[serving2.index] == 'Missing quantity!'

    ingredient2 = recipe.ingredients[2]
    assert ingredient2.text == 'Tomaten'
    assert ingredient2.quantities[serving0.index] == '3 Dosen (400g Füllmenge)'
    assert ingredient2.quantities[serving1.index] == '3 Dosen (400g Füllmenge)'
    assert ingredient2.quantities[serving2.index] == '3 Dosen (400g Füllmenge)'

    ingredient3 = recipe.ingredients[3]
    assert ingredient3.text == 'Zimtstange'
    assert ingredient3.quantities[serving0.index] == ''
    assert ingredient3.quantities[serving1.index] == ''
    assert ingredient3.quantities[serving2.index] == ''

    ingredient4 = recipe.ingredients[4]
    assert ingredient4.text == 'Salz und Pfeffer'
    assert ingredient4.quantities[serving0.index] == ''
    assert ingredient4.quantities[serving1.index] == ''
    assert ingredient4.quantities[serving2.index] == ''

    ingredient5 = recipe.ingredients[5]
    assert ingredient5.text == ''
    assert ingredient5.quantities[serving0.index] == ''
    assert ingredient5.quantities[serving1.index] == ''
    assert ingredient5.quantities[serving2.index] == ''

    assert recipe.steps[1].text == 'Zwiebeln, Knoblauch und Paprika ca. 5min im Öl anschwitzen'
    assert recipe.steps[5].text == ''

    assert recipe.variants[1].text == 'Eine Dose weiße Bohnen anstatt Kidneybohnen verwenden.'
    assert recipe.variants[2].text == ''

    assert recipe.images[0] == 'data/Chili con Carne.png'


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


def test_minimal_recipe():
    recipe = yuml.recipe_from_file('data/minimal.yuml')
    assert len(recipe.servings) == 1
    assert len(recipe.ingredients) == 1
    assert len(recipe.steps) == 0
    assert len(recipe.variants) == 0
    assert len(recipe.images) == 0
