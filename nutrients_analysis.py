from recipe import Recipe
import json
import re

recipeFile = 'baking'
with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
    data = json.load(file)



def kcal_dv(recipe):
    daily_value = 2000
    percentage = int(((int(recipe.nutrients['kcal']) / recipe.serves) / daily_value) * 100)
    return f'{round(percentage, 2)}%'

def fat_dv(recipe):
    daily_value = 70
    percentage = (float(recipe.nutrients['fat'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def carbs_dv(recipe):
    daily_value = 310
    percentage = (float(recipe.nutrients['carbs'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def sugars_dv(recipe):
    daily_value = 50
    percentage = (float(recipe.nutrients['sugars'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}%'
    

def fibre_dv(recipe):
    daily_value = 28
    percentage = (float(recipe.nutrients['fibre'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def protein_dv(recipe):
    daily_value = 50
    percentage = (float(recipe.nutrients['protein'].strip('g')) / recipe.serves / daily_value) * 100
    return f'{round(percentage, 2)}%'

def salt_dv(recipe):
    daily_value = 2.3
    salt = float(recipe.nutrients['salt'].strip('g')) / recipe.serves
    percentage = int((salt / daily_value) * 100)
    return f'{round(percentage, 2)}%'

def calories_serving(recipe):
    cal = int(recipe.nutrients['kcal']) / int(recipe.serves)
    return round(cal, 2)

def hours_minutes(time_str):
    hours = 0
    minutes = 0
    hours_minutes = re.findall(r'\d+', time_str) 

    if ('hr'in time_str or 'hrs' in time_str) and 'mins' in time_str: 
        hours = int(hours_minutes[0])
        minutes = int(hours_minutes[1])
    elif 'hr' or 'hrs' in time_str: 
        hours = int(hours_minutes[0]) 
    else: 
        minutes = int(hours_minutes[0])
    return hours


def total_time(recipe):
    
    prep_time = hours_minutes(recipe.times['Preparation'])
    cook_time = hours_minutes(recipe.times['Cooking'])            
    total_time = prep_time + cook_time
    return total_time

def minutes_to_hours(minutes):
    hours = minutes // 60
    minutes_left_over = minutes % 60
    if hours > 0:
        hours_label = 'hour' if hours == 1 else 'hours'
        minutes_label = 'minute' if minutes == 1 else 'minutes' 
        return f'{hours} {hours_label} and {minutes} {minutes_label}'
    else:
        return f'{minutes} minutes'


new_recipe = Recipe(data[3]['name'], data[3]['url'], data[3]['description'], data[3]['ingredients'], data[3]['steps'], data[3]['nutrients'], data[3]['times'], data[3]['serves'], data[3]['dish_type'], data[3]['maincategory'])
print(new_recipe.nutrients['kcal'])
print(new_recipe.serves)
print(kcal_dv(new_recipe))
print(hours_minutes(new_recipe.times['Cooking']))
print(total_time(new_recipe))
# print(salt_dv(new_recipe))
# print(calories_serving(new_recipe))
# print(fibre_dv(new_recipe))
# print(new_recipe['nutrients']['salt'].strip('g'))
print(minutes_to_hours(total_time(new_recipe)))

