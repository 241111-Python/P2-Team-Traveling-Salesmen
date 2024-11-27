import os, argparse
from JSON_reader import searchByName, searchByIngredients
from recipe import Recipe, save_recipes_to_json

continu = "yes"
recipeFileOptions = [file[:-5] for file in os.listdir("JSON_FILES")]

parser = argparse.ArgumentParser(description="Recipe Finder Program")
parser.add_argument("--data-file",type=str,help="Path to the JSON file containing recipes (e.g., 'JSON_FILES/budget.json').")
args = parser.parse_args()

print(args.data_file)


while continu.lower() != 'no':
  print("Hello Friend! \n Welcome to the RECIPE FINDER PROGRAM.")
  
  if not args.data_file or args.data_file not in recipeFileOptions:
    recipeFile = input(f"What kind of recipes would you like to view? \n(Options: {recipeFileOptions}) ")
    while recipeFile not in recipeFileOptions:
      recipeFile = input(f"Invalid Entry.\nWhat kind of recipes would you like to view?\n(Options: {recipeFileOptions}) ")
  else:
    recipeFile = args.data_file
  nameOrIngredients = input("Would you like to search by recipe name or ingredients? Enter 'name' or 'ingredients' ")
  while nameOrIngredients != "name" and nameOrIngredients != "ingredients":
    nameOrIngredients = input("Invalid Entry.\nWould you like to search by recipe name or ingredients? Enter 'name' or 'ingredients' ")
    
  if nameOrIngredients == "name": 
    name = input("Enter the dish's name: ")
    searchByName(name, recipeFile)
  else:
    ingredients = input("Enter the list of ingredients: \n Ex: Cheese, Pepperoni, Mushrooms (Case-insensitive; Comma to Separate Ingredients)")
    searchByIngredients(ingredients, recipeFile)
  
  minCalories = int(input("Enter the Minimum Amount of Calories per Serving: ") or "0")
  while minCalories < 0:
    minCalories = int(input("Try a larger value. Enter the Minimum Number of Calories per Serving: "))

  maxCalories = int(input("Enter the Maximum Amount of Calories per Serving: ") or "1000")
  while maxCalories < 0:
    maxCalories = int(input("Try a larger value. Enter the Maximum Amount of Calories per Serving: "))
  
  prepTime = int(input("Enter the Maximum Prep/Cook Time(in minutes): ") or "10000")
  while prepTime < 0:
    prepTime = int(input("Try a larger value. Enter the Maximum Prep/Cook Time: "))
  
  if nameOrIngredients == "name":
    recipes = searchByName(name, recipeFile, minCalories, maxCalories, prepTime)
  else:
    recipes = searchByIngredients(ingredients, recipeFile, minCalories, maxCalories, prepTime)
  
  print("\n\nYour Recipes: ")
  recipe_list = []
  if recipes:
    
    with open("output.txt", 'a') as file:
      
      print(f"Choose a number 1-{len(recipes)}")
      for i, recipe in enumerate(recipes):
        index = i + 1
        print(f"{index}: {recipe}")
        file.write(recipe.__str__() + '\n')
      choice = input("Enter your choice: ")
      while choice != "all" and not choice.isdigit() or (choice.isdigit() and (int(choice) < 1 or int(choice) > len(recipes))):
            choice = input("Invalid input. Enter a valid number or 'all': ")
        
      selected_recipe = recipes[int(choice) - 1]
      
      recipe_list.append(selected_recipe)
      print(recipe_list)
      save_recipes_to_json(recipe_list, "saved.json")
        
  else:
    print("No recipes found with the given criteria.")
  
  print("\n\n")
  
  continu = input("Would you like to search for another recipe? Enter 'yes' or 'no': ")


