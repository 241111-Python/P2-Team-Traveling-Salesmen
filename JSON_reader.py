import json                               # This imports Python's built-in json module used to work with JSON data
from recipe import Recipe                 # Importing the Recipe class from recipe.py to handle the recipes

# Define the function to search recipes by name with given parameters
def searchByName(name, recipeFile, minCalories=0, maxCalories=100000, prepTime=1000):
    # Reads the JSON file which is passed as recipeFile, converts its content into a list of dictionaries, and closes the file
    with open('JSON_Files/' + recipeFile + '.json', 'r') as file:  
        data = json.load(file)  # Converts the JSON content into a Python object (list of recipes)

    recipes = []  # Initialized an empty list to store the recipes that match the search criteria
    for recipe in data:
        # Checks whether the given input 'name' is present in the recipe's name (case-insensitive search)
        if name.lower() in recipe['name'].lower():
            try:
                # Calculating calories per serving
                calories = int(recipe['nutrients']['kcal']) / recipe['serves']  # 'kcal' is in string, so we convert it to int for calculation
                prep = int(recipe["times"].get("prep", 0))
                if minCalories <= calories and calories <= maxCalories:  # Check if the calculated calories are within the user-provided range
                    # If it meets the calorie range, append the matching recipe to the recipes list
                    recipes.append(Recipe(
                        recipe['name'], 
                        recipe['url'], 
                        recipe['description'], 
                        recipe['ingredients'], 
                        recipe['steps'], 
                        recipe['nutrients'], 
                        recipe['times'], 
                        recipe['serves'], 
                        recipe['dish_type'], 
                        recipe['maincategory']
                    ))

            except KeyError:
                pass  # In case any required key is missing, we ignore that recipe

    return recipes  # Return the list of matching recipes


# Define the function to search recipes by ingredients with given parameters
def searchByIngredients(ingredients, recipeFile, minCalories=0, maxCalories=100000, prepTime=10000):
    try:
        # Read the JSON file corresponding to the recipeFile parameter
        with open(f'JSON_Files/{recipeFile}.json', 'r') as file:
            data = json.load(file)

        # Process the ingredients input by stripping spaces and converting them to lowercase
        ingredients = [ingredient.strip().lower() for ingredient in ingredients.split(",")]

        matching_recipes = []  # Initialize an empty list to store recipes that match the ingredients

        # Iterate through each recipe in the data
        for recipe in data:
            try:
                # Check if the recipe's ingredients are in a list format
                recipe_ingredients = [item.strip().lower() for item in recipe.get("ingredients", [])]

                # Ensure all input ingredients are present in the recipe's ingredients
                all_match = all(
                    any(ingredient in item for item in recipe_ingredients)  # Check if each ingredient is in the recipe's ingredient list
                    for ingredient in ingredients
                )

                if all_match:  # If all ingredients match
                    # Calculate calories per serving
                    calories = int(recipe["nutrients"]["kcal"]) / recipe["serves"] if "kcal" in recipe["nutrients"] else 0
                    prep = int(recipe["times"].get("prep", 0))  # Get the preparation time (default to 0 if not present)

                    # Check if the recipe satisfies the calorie and prep time conditions
                    if minCalories <= calories <= maxCalories and prepTime >= prep:
                        matching_recipes.append(
                            Recipe(
                                name=recipe["name"],
                                url=recipe["url"],
                                description=recipe["description"],
                                ingredients=recipe["ingredients"],
                                steps=recipe["steps"],
                                nutrients=recipe["nutrients"],
                                times=recipe["times"],
                                serves=recipe["serves"],
                                dish_type=recipe["dish_type"],
                                maincategory=recipe["maincategory"]
                            )
                        )
            except KeyError as e:
                print(f"KeyError for recipe '{recipe.get('name', 'Unknown')}': {e}")  # In case of missing keys, print the error message

        return matching_recipes  # Return the list of matching recipes

    except FileNotFoundError:
        print(f"Error: File 'JSON_Files/{recipeFile}.json' not found.")  # Handle if the file is not found
        return []  # Return an empty list in case of error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Catch any other exceptions
        return []  # Return an empty list in case of error
