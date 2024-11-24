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
                    recipes.append(Recipe(recipe['name'], recipe['url'], recipe['description'], recipe['ingredients'], recipe['steps'], recipe['nutrients'], recipe['serves'], recipe['times'], recipe['dish_type'], recipe['maincategory']))
            except KeyError:
                pass

    return recipes
    

def searchByIngredients(ingredients, recipeFile, minCalories=0, maxCalories=100000, prepTime=1000): 
    pass