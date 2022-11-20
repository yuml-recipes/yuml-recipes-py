# finder.py
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

import os
from typing import List

valid_file_endings = ['.jpg', '.jpeg', '.png']


def is_file(dir_path: str, child_name: str) -> bool:
    return os.path.isfile(os.path.join(dir_path, child_name))


def has_matching_name(recipe_name: str, filename: str) -> bool:
    name, extension = os.path.splitext(filename)
    return extension.lower() in valid_file_endings and name.startswith(recipe_name)


def find_images(file_path: str) -> List[str]:
    recipe_name, _ = os.path.splitext(os.path.basename(file_path))
    dir_path = os.path.dirname(file_path)
    children = os.listdir(dir_path)
    return [child for child in children if is_file(dir_path, child) and has_matching_name(recipe_name, child)]
