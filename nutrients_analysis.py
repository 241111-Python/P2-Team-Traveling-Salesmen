from recipe import Recipe
import json

recipeFile = 'baking'
with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
        data = json.load(file)



def kcal_dv(recipe):
    daily_value = 2000
    percentage = int(((int(recipe['nutrients']['kcal']) / recipe['serves']) / daily_value) * 100)
    return f'{round(percentage, 2)}%'

def fat_dv(recipe):
    daily_value = 70
    percentage = (float(recipe['nutrients']['fat'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def carbs_dv(recipe):
    daily_value = 310
    percentage = (float(recipe['nutrients']['carbs'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def sugars_dv(recipe):
    daily_value = 50
    percentage = (float(recipe['nutrients']['sugars'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{round(percentage, 2)}%'
    

def fibre_dv(recipe):
    daily_value = 28
    percentage = (float(recipe['nutrients']['fibre'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{round(percentage, 2)}%'

def protein_dv(recipe):
    daily_value = 50
    percentage = (float(recipe['nutrients']['protein'].strip('g')) / recipe['serves'] / daily_value) * 100
    return f'{round(percentage, 2)}%'

def salt_dv(recipe):
    daily_value = 2.3
    salt = float(recipe['nutrients']['salt'].strip('g')) / recipe['serves']
    percentage = int((salt / daily_value) * 100)
    return f'{round(percentage, 2)}%'

def calories_serving(recipe):
    cal = int(recipe['nutrients']['kcal']) / int(recipe['serves'])
    return round(cal, 2)

def total_time(recipe):
    prep_time = int(recipe['times']['Preparation'].strip(' mins'))
    cook_time = int(recipe['times']['Cooking'].strip(' mins'))            
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


new_recipe = data[1]
print(total_time(new_recipe))
print(salt_dv(new_recipe))
print(calories_serving(new_recipe))
print(fibre_dv(new_recipe))
print(new_recipe['nutrients']['salt'].strip('g'))
print(minutes_to_hours(total_time(new_recipe)))

