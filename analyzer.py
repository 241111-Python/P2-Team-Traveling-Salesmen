from recipe import Recipe
import json
from output_format import single_output_format

recipes = []

with open( '.json', 'r') as file:
    recipe = json.load(file)

for i in recipe:
    recipes.append(Recipe(recipe['name'], recipe['url'], recipe['description'], recipe['ingredients'], recipe['steps'], recipe['nutrients'], recipe['times'], recipe['serves'], recipe['dish_type'], recipe['maincategory']))

if recipes:
    
    with open("output.txt", 'a') as file:
      
        for recipe in recipes:
  
            file.write(single_output_format(recipe))

