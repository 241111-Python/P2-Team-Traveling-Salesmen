from recipe import Recipe
import json
from output_format import single_output_format
import datetime

recipes = []

with open( 'Json_Files/baking.json', 'r') as file:
    recipe_data = json.load(file)

index = 0
for i in recipe_data:
    recipes.append(Recipe(recipe_data[index]['name'], recipe_data[index]['url'], recipe_data[index]['description'], recipe_data[index]['ingredients'], recipe_data[index]['steps'], 
                          recipe_data[index]['nutrients'], recipe_data[index]['times'], recipe_data[index]['serves'], recipe_data[index]['dish_type'], recipe_data[index]['maincategory']))
    index += 1 

# Used to output the nutrition facts per serving for all recipes you add to a the .json file 
if recipes:
    
    with open("recipe_analysis.txt", 'w') as file:
        file.write(f'{datetime.date} {datetime.time}')
        file.write('Selected Recipe Nutrition Facts Per Serving:')
        for recipe in recipes:
            if not recipe.nutrients:
                file.write(f'''Recipe Name: {recipe.name}: {recipe.url}
                           Nutrition Facts Unavailable!''')
            else:
                file.write(single_output_format(recipe))

