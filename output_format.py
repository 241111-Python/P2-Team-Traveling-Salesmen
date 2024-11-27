import nutrients_analysis
from recipe import Recipe

def single_output_format(recipe):
    return f"""Recipe Name and URL: {recipe.name} {recipe.url}
Total Time To Make: {nutrients_analysis.minutes_to_hours(nutrients_analysis.total_time(recipe))}
Calories per Serving: {nutrients_analysis.calories_serving(recipe)}
kCal Daily Value: {nutrients_analysis.kcal_dv(recipe)}%
Carbs Daily Value: {nutrients_analysis.carbs_dv(recipe)}%
Fat Daily Value: {nutrients_analysis.fat_dv(recipe)}%
Sugars Daily Value: {nutrients_analysis.sugars_dv(recipe)}%
Protein Daily Value: {nutrients_analysis.protein_dv(recipe)}%
Salt Daily Value: {nutrients_analysis.salt_dv(recipe)}%
----------------------------------------------------------\n"""
