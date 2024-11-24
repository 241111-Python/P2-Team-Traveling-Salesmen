class Recipe():

    def __init__(self, id, url, image, name, description, author, rattings, ingredients, steps, nutrients, times, serves, difficult, vote_count, subcategory, dish_type, maincategory ):
        self.id = id
        self.url = url
        self.image = image 
        self.name = name
        self.description = description 
        self.author = author
        self.rattings = rattings
        self.ingredients = ingredients
        self.steps = steps 
        self.nutrients = nutrients
        self.times = times
        self.serves = serves
        self.difficult = difficult
        self.vote_count = vote_count
        self.subcategory = subcategory
        self.dish_type = dish_type
        self.maincategory = maincategory

    def __str__(self):
        return f'{self.name} : {self.url}'