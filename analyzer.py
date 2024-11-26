from recipe import Recipe
import json
from output_format import single_output_format
import datetime
import nutrients_analysis

recipes = []

with open( 'saved.json', 'r') as file:
    recipe_data = json.load(file)

index = 0
for i in recipe_data:
    recipes.append(Recipe(recipe_data[index]['name'] , recipe_data[index]['url'], recipe_data[index]['description'], recipe_data[index]['ingredients'], recipe_data[index]['steps'], 
                          recipe_data[index]['nutrients'], recipe_data[index]['times'], recipe_data[index]['serves'], recipe_data[index]['dish_type'], recipe_data[index]['maincategory']))
    index += 1 

# Used to output the nutrition facts per serving for all recipes you add to a the .json file 
if recipes:
    index = 0
    with open("recipe_analysis.txt", 'w') as file:
        file.write(f'{datetime.datetime.today()} \n')
        file.write(f'''Selected Recipe Nutrition Facts Per Serving(Total Recipes: {len(recipes)}):
------------------------------------------------ \n''')
        for recipe in recipes:
            if not recipe.nutrients:
                file.write(f'''Recipe Name and URL: {recipe.name} {recipe.url}
Total Cook Time: {nutrients_analysis.minutes_to_hours(nutrients_analysis.total_time(recipe))}
Nutrition Facts Unavailable! 
-------------------------------------------------\n''')
            else:
                file.write(single_output_format(recipes[index]))
            index += 1
            

