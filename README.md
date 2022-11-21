# Yuml Recipes Python Library

This is the Python library for Yuml Recipes. It reads *.yuml files and collects all recipe information. Images that are located in the same directory and use the same base name are associated with the respective *.yuml recipe.

## Example

```yaml
servings:
    - Enough for everyone
ingredients:
    - Mix of vegetables: 800g
    - Salt and pepper:
steps:
    - Cut everything in pieces
    - Fry everything in a pan for 10 minutes
    - Season with salt and pepper
variants:
    - Add strips of chicken breast to the mix
```

## Usage

```python
import yuml
from typing import List

recipe: yuml.Recipe = yuml.recipe_from_file('my_recipe.yuml')
servings: List[yuml.Serving] = recipe.servings
ingredients: List[yuml.Ingredient] = recipe.ingredients
steps: List[yuml.Step] = recipe.steps
variants: List[yuml.Variant] = recipe.variants
images: List[str] = recipe.images
```

## Setup

1. Initialize the Python virtual environment
   * Run './venv.sh' to initialize the virtual environment
   * Run 'source venv.bat' to activate the virtual environment in a shell
   * Use an IDE that can activate the existing virtual environment for you
1. Run 'pytest' from a shell with the virtual environment activated
1. Run './build.sh' to lint, test and create a package

## License

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

GPL-3.0

Copyright (c) 2022 Patrick Eschenbach
