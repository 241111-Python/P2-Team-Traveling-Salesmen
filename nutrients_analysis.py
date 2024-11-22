from recipe import Recipe
import json

recipeFile = 'baking'
with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
        data = json.load(file)


def kcal_dv(recipe):
    daily_value = 2000
    percentage = int(((recipe['nutrients']['kcal'] / recipe['serves']) / daily_value) * 100)
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


new_recipe = data[0]
print(new_recipe)
print(salt_dv(new_recipe))
print(calories_serving(new_recipe))
print(fibre_dv(new_recipe))
print(new_recipe['nutrients']['salt'].strip('g'))
