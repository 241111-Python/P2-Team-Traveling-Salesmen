from recipe import Recipe
import json

recipeFile = 'baking'
with open( 'JSON_Files/' + recipeFile + '.json', 'r') as file:
        data = json.load(file)


def kcal_dv(recipe):
    daily_value = 2000
    percentage = int(((recipe['nutrients']['kcal'] / recipe['serves']) / daily_value) * 100)
    return f'{percentage}%'

def fat_dv(recipe):
    daily_value = 70
    percentage = (float(recipe['nutrients']['fat'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{percentage}%'

def carbs_dv(recipe):
    daily_value = 310
    percentage = (float(recipe['nutrients']['carbs'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{percentage}%'

def sugars_dv(recipe):
    daily_value = 50
    percentage = (float(recipe['nutrients']['sugars'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{percentage}%'
    

def fibre_dv(recipe):
    daily_value = 28
    percentage = (float(recipe['nutrients']['fibre'].strip('g')) / recipe['serves']  / daily_value) * 100
    return f'{percentage}%'

def protein_dv(recipe):
    daily_value = 50
    percentage = (float(recipe['nutrients']['protein'].strip('g')) / recipe['serves'] / daily_value) * 100
    return f'{percentage}%'

def salt_dv(recipe):
    daily_value = 2.3
    salt = float(recipe['nutrients']['salt'].strip('g')) / recipe['serves']
    percentage = int((salt / daily_value) * 100)
    return f'{percentage}%'

def calories_serving(recipe):
    cal = recipe['nutrients']['kcal'] / recipe['serves']
    return cal


new_recipe = data[0]
print(salt_dv(new_recipe))
print(new_recipe['nutrients']['salt'].strip('g'))
