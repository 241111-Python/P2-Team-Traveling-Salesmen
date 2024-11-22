from JSON_reader import searchByName, searchByIngredients

contin = "yes"
recipeFileOptions = ['budget', 'insiration', 'baking', 'health', 'recipes']

while contin != 'no':
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
  
  minCalories = int(input("Enter the minimum number of calories per serving you'd like in your meal: "))
  while minCalories < 5:
    minCalories = input("Try a larger value. Enter the minimum number of calories per serving you'd like in your meal: ")

  maxCalories = int(input("Enter the maximum number of calories per serving you'd like in your meal: "))
  while maxCalories < 5:
    maxCalories = input("Try a larger value. Enter the maximum number of calories per serving you'd like in your meal: ")
  
  prepTime = int(input("Enter the maximum prep/cook time you'd like to take (in minutes): "))
  while prepTime < 0:
    prepTime = input("Try a larger value. Enter the maximum prep/cook time you'd like to take")
  
  if nameOrIngredients == "name":
    recipes = searchByName(name, recipeFile, minCalories, maxCalories, prepTime)
  else:
    recipes = searchByIngredients(ingredients, recipeFile, minCalories, maxCalories, prepTime)
  print("\n\nYour Recipes: ")
  for recipe in recipes:
    print(recipe)
  print("\n\n")
  contin = input("Would you like to search for another recipe? Enter 'yes' or 'no'")

