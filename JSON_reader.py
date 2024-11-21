import json

class Recipe:
    def __init__(self, id, url, image, name):
        self.id = id
        self.url = url
        self.image = image
        self.name = name

    def __str__(self):
        return f'{self.name}:'


#input file name
recipe_type = 'baking.json'

# Reads the JSON file, inputs it into a list of dictionary, and closes the file
with open( 'JSON_Files/' + recipe_type, 'r') as file:
    data = json.load(file)

#print(data[0]) 
#for i in data:
#    print(i)

recipeobjs = []
for x in data:
    entry = Recipe(x['id'], x['url'], x['image'], x['name'])
    recipeobjs.append(entry)
    print(entry)
    
#for i in recipeobjs:
#   print(i)