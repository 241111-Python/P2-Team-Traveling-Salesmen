import json
from recipe import Recipe

def searchByName(name, recipeFile, minCalories=0, maxCalories=100000, prepTime=1000):

    # Reads the JSON file, inputs it into a list of dictionary, and closes the file
    with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
        data = json.load(file)

    recipes = []
    for recipe in data:
        if name.lower() in recipe['name'].lower():
            try:
                calories = int(recipe['nutrients']['kcal']) / recipe['serves']
                if minCalories <= calories and calories <= maxCalories:
                    recipes.append(Recipe(recipe['name'], recipe['url'], recipe['description'], recipe['ingredients'], recipe['steps'], recipe['nutrients'], recipe['times'], recipe['serves'], recipe['dish_type'], recipe['maincategory']))
            except KeyError:
                pass

    return recipes
     

def searchByIngredients(ingredients, recipeFile, minCalories=0, maxCalories=100000, prepTime=10000):
    try:
        # Read the JSON file.
        with open(f'JSON_Files/{recipeFile}.json', 'r') as file:
            data = json.load(file)

        # Process the ingredients input.
        ingredients = [ingredient.strip().lower() for ingredient in ingredients.split(",")]

        matching_recipes = []

        # Iterate through each recipe in the data.
        for recipe in data:
            try:
                # Check if the recipe's ingredients are in a list format.
                recipe_ingredients = [item.strip().lower() for item in recipe.get("ingredients", [])]

                # Ensure all input ingredients are present in the recipe's ingredients.
                all_match = all(
                    any(ingredient in item for item in recipe_ingredients)
                    for ingredient in ingredients
                )

                if all_match:  # If all ingredients match:
                    # Check calorie and prep time constraints.
                    calories = int(recipe["nutrients"]["kcal"]) / recipe["serves"] if "kcal" in recipe["nutrients"] else 0
                    prep = int(recipe["times"].get("prep", 0))

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
                print(f"KeyError for recipe '{recipe.get('name', 'Unknown')}': {e}")

        return matching_recipes

    except FileNotFoundError:
        print(f"Error: File 'JSON_Files/{recipeFile}.json' not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []
