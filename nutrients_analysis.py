from recipe import Recipe
import json
import re

recipeFile = 'baking'
with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
    data = json.load(file)

def kcal_dv(recipe):
    daily_value = 2000
    percentage = int(((int(recipe.nutrients['kcal']) / recipe.serves) / daily_value) * 100)
    return f'{round(percentage, 2)}'

def fat_dv(recipe):
    daily_value = 70
    percentage = (float(recipe.nutrients['fat'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}'

def carbs_dv(recipe):
    daily_value = 310
    percentage = (float(recipe.nutrients['carbs'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}'

def sugars_dv(recipe):
    daily_value = 50
    percentage = (float(recipe.nutrients['sugars'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}'
    

def fibre_dv(recipe):
    daily_value = 28
    percentage = (float(recipe.nutrients['fibre'].strip('g')) / recipe.serves  / daily_value) * 100
    return f'{round(percentage, 2)}'

def protein_dv(recipe):
    daily_value = 50
    percentage = (float(recipe.nutrients['protein'].strip('g')) / recipe.serves / daily_value) * 100
    return f'{round(percentage, 2)}'

def salt_dv(recipe):
    daily_value = 2.3
    salt = float(recipe.nutrients['salt'].strip('g')) / recipe.serves
    percentage = int((salt / daily_value) * 100)
    return f'{round(percentage, 2)}'

def calories_serving(recipe):
    cal = int(recipe.nutrients['kcal']) / int(recipe.serves)
    return round(cal, 2)

def hours_minutes(time_str):
    hours_pattern = re.compile(r'(\d+)\s*hr')
    minutes_pattern = re.compile(r'(\d+)\s*mins?')

    hours_match = hours_pattern.search(time_str)
    minutes_match = minutes_pattern.search(time_str)

    hours = int(hours_match.group(1)) if hours_match else 0
    minutes = int(minutes_match.group(1)) if minutes_match else 0

    return (hours * 60) + minutes


def total_time(recipe):
    if 'Cooking' in recipe.times:
        prep_time = hours_minutes(recipe.times['Preparation'])
        cook_time = hours_minutes(recipe.times['Cooking'])
    else:
        prep_time = hours_minutes(recipe.times['Preparation'])
        cook_time = 0        
    total_time = prep_time + cook_time
    return total_time

def minutes_to_hours(minutes):
    hours = minutes // 60
    minutes_left_over = minutes % 60
    if hours > 0:
        hours_label = 'hour' if hours == 1 else 'hours'
        minutes_label = 'minute' if minutes == 1 else 'minutes' 
        return f'{hours} {hours_label} and {minutes_left_over} {minutes_label}'
    else:
        return f'{minutes} minutes'


# new_recipe = Recipe(data[5]['name'], data[5]['url'], data[5]['description'], data[5]['ingredients'], data[5]['steps'], data[5]['nutrients'], data[5]['times'], data[5]['serves'], data[5]['dish_type'], data[5]['maincategory'])
# print(new_recipe.name)
# print(total_time(new_recipe))


