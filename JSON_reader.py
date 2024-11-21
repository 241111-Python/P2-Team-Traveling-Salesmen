import json

#input file name
recipe_type = 'baking.json'

# Reads the JSON file, inputs it into a dictionary, and close the file
with open( 'JSON_Files/' + recipe_type, 'r') as file:
    data = json.load(file)

print(data[0])
