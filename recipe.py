import json
import os

class Recipe():

    def __init__( self, name, url, description, ingredients, steps, nutrients, times, serves, dish_type, maincategory ):
        self.url = url
        self.name = name
        self.description = description 
        self.ingredients = ingredients
        self.steps = steps 
        self.nutrients = nutrients
        self.times = times
        self.serves = serves
        self.dish_type = dish_type
        self.maincategory = maincategory

    def __str__(self):
        return f'{self.name}: {self.url}'

    def get_prep_time(self):
        return int(self['times']['Preparation'].strip(" mins"))
    
    def get_cook_time(self):
        return int(self['times']['Cooking'].strip(" mins"))
    
    def to_dict(self):
        return {
            "name": self.name,
            "url": self.url,
            "description": self.description,
            "ingredients": self.ingredients,
            "steps": self.steps,
            "nutrients": self.nutrients,
            "times": self.times,
            "serves": self.serves,
            "dish_type": self.dish_type,
            "maincategory": self.maincategory
        }
def save_recipes_to_json(recipes, file_path):
    with open(file_path, 'a') as file:
            json.dump([recipe.to_dict() for recipe in recipes], file, indent=4)
