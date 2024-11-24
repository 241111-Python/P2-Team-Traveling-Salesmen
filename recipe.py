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