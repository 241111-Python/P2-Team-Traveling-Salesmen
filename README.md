# Recipe Finder Program

## Overview

The Recipe Finder program allows users to search through a collection of recipes stored in JSON files. Users can search by recipe name or by ingredients and filter the results based on calorie range and preparation time.

---

## Features

- **Recipe Categories:** Choose from `budget`, `inspiration`, `baking`, `health`, or `recipes`.
- **Search by Name:** Find recipes by their name.
- **Search by Ingredients:** Search for recipes containing specific ingredients.
- **Filter Options:** Set minimum and maximum calories per serving and preparation time.
- **Results Output:** Display recipes on the console and save them to `output.txt`.

---

## Prerequisites

- Python 3.x installed on your machine.
- JSON files for each recipe category in the `JSON_Files/` directory.
- `recipe.py` module to define the `Recipe` class.

---

## Usage

1. Clone the repository or download the program files.
2. Ensure that the JSON files for recipe categories (`budget.json`, `inspiration.json`, etc.) are in the `JSON_Files/` directory.
3. Run the program using:

   ```bash
   python recipe_finder.py


## Cronjob
To run the analyzer script as a cron job do:
* * * * * cd /mnt/c/Users/dalla/rev/week2/p2/P2-Team-Traveling-Salesmen && /bin/bash -c 'source /mnt/c/Users/dalla/week2/p2/P2-Team-Traveling-Salesmen/venv/Scripts/activate && /usr/bin/python3 /mnt/c/Users/dalla/rev/week2/p2/P2-Team-Traveling-Salesmen/analyzer.py
with correct absolute paths.
