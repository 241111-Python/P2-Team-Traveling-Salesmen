import nutrients_analysis
from recipe import Recipes

def output_format(recipe):
    return f"""Recipe Name: {recipe.name} 
    Total Time To Make: 
    Calories per Serving: {nutrients_analysis.calories_serving(recipe)} 
    kCal Daily Value: {nutrients_analysis.kcal_dv}
    Carbs Daily Value: {nutrients_analysis.carbs_dv}
    Fat Daily Value: {nutrients_analysis.fat_dv}
    Sugars Daily Value: {nutrients_analysis.sugars_dv}
    Protein Daily Value: {nutrients_analysis.protein_dv}
    Salt Daily Value: {nutrients_analysis.salt_dv}
    """