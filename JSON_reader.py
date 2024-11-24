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
     

def searchByIngredients(ingredients, recipeFile, minCalories=0, maxCalories=100000, prepTime=1000):

    with open('JSON_Files/' + recipeFile + '.json', 'r') as file:
        data = json.load(file)

    recipes = []

    #input ingredients to make them case-insensitive and strip extra spaces
    ingredients = [ingredient.lower().strip() for ingredient in ingredients.split(",")]

    for recipe in data:
        try:
            # Check if the recipe's ingredients are in a list format
            if isinstance(recipe['ingredients'], list):
                # Process each ingredient in the recipe, making it case-insensitive and stripping extra spaces
                recipe_ingredients = [ingredient.strip().lower() for ingredient in recipe['ingredients']]
            else:
                # If ingredients are not in a list format, use an empty list
                recipe_ingredients = []

            # Check if any of the user's ingredients match the recipe ingredients
            matching_ingredients = [ingredient for ingredient in ingredients if any(ingredient in item for item in recipe_ingredients)]

            # If there are matching ingredients, proceed with further checks
            if matching_ingredients:
                calories = int(recipe['nutrients']['kcal']) / recipe['serves'] if 'kcal' in recipe['nutrients'] else 0

                prep = recipe['times'].get('prep', 0)

                if minCalories <= calories <= maxCalories and prepTime >= int(prep):
                    recipes.append(Recipe(recipe['name'], recipe['url'], recipe['description'], recipe['ingredients'], recipe['steps'], recipe['nutrients'], recipe['times'], recipe['serves'], recipe['dish_type'], recipe['maincategory']))

        except KeyError as e:
            print(f"KeyError: {e} - skipping recipe {recipe['name']}")

    return recipes
