import os
from JSON_reader import searchByName, searchByIngredients

continu = "yes"
recipeFileOptions = [file[:-5] for file in os.listdir("JSON_FILES")]

while continu.lower() != 'no':
  print("Hello friend! \n Welcome to the recipe finder program.")
  
  recipeFile = input("What kind of recipes would you like to view? \n(options are 'budget', 'inspiration', 'baking', 'health' or 'recipes') ")
  while recipeFile not in recipeFileOptions:
    recipeFile = input("Let's try that again\nWhat kind of recipes would you like to view?\n(options are 'budget', 'inspiration', 'baking', 'health' or 'recipes') ")
  
  nameOrIngredients = input("Would you like to search by recipe name or ingredients? Enter 'name' or 'ingredients' ")
  while nameOrIngredients != "name" and nameOrIngredients != "ingredients":
    nameOrIngredients = input("Let's try that again\nWould you like to search by recipe name or ingredients? Enter 'name' or 'ingredients' ")
  if nameOrIngredients == "name": 
    name = input("Enter the dish's name: ")
    searchByName(name, recipeFile)
  else:
    ingredients = input("Enter the list of ingredients: \n ex: cheese, Pepperoni, mushrooms (caps don't matter and use commas to separate ingredients)")
    searchByIngredients(ingredients, recipeFile)
  
  minCalories = int(input("Enter the minimum number of calories per serving you'd like in your meal: ") or "0")
  while minCalories < 0:
    minCalories = int(input("Try a larger value. Enter the minimum number of calories per serving you'd like in your meal: "))

  maxCalories = int(input("Enter the maximum number of calories per serving you'd like in your meal: ") or "1000")
  while maxCalories < 0:
    maxCalories = int(input("Try a larger value. Enter the maximum number of calories per serving you'd like in your meal: "))
  
  prepTime = int(input("Enter the maximum prep/cook time you'd like to take (in minutes): ") or "10000")
  while prepTime < 0:
    prepTime = int(input("Try a larger value. Enter the maximum prep/cook time you'd like to take"))
  
  if nameOrIngredients == "name":
    recipes = searchByName(name, recipeFile, minCalories, maxCalories, prepTime)
  else:
    recipes = searchByIngredients(ingredients, recipeFile, minCalories, maxCalories, prepTime)
  
  print("\n\nYour Recipes: ")
  with open("output.txt", 'a') as file:

    for recipe in recipes:
      file.write(recipe.__str__() + '\n')
      print(recipe)
  
  print("\n\n")
  
  continu = input("Would you like to search for another recipe? Enter 'yes' or 'no' ")

