import nutrients_analysis
from recipe import Recipe

def single_output_format(recipe):
    return f"""Recipe Name: {recipe.name}: {recipe.url}
Total Time To Make: {nutrients_analysis.minutes_to_hours(nutrients_analysis.total_time(recipe))}
Calories per Serving: {nutrients_analysis.calories_serving(recipe)}
kCal Daily Value: {nutrients_analysis.kcal_dv(recipe)}%
Carbs Daily Value: {nutrients_analysis.carbs_dv(recipe)}%
Fat Daily Value: {nutrients_analysis.fat_dv(recipe)}%
Sugars Daily Value: {nutrients_analysis.sugars_dv(recipe)}%
Protein Daily Value: {nutrients_analysis.protein_dv(recipe)}%
Salt Daily Value: {nutrients_analysis.salt_dv(recipe)}%
    """

def daily_nutrients_format(total_nutrients):
    return f"""kCal Daily Value: {total_nutrients[0]/2000}%
Carbs Daily Value: {total_nutrients[1]/310}%
Fibre Daily Value: {total_nutrients[2]/28}%
Fat Daily Value: {total_nutrients[3]/70}%
Sugars Daily Value: {total_nutrients[4]/50}%
Protein Daily Value: {total_nutrients[5]/50}%
Salt Daily Value: {total_nutrients[6]/2.3}%
    """

def daily_menu_output(menu):
    menu_str = ''
    for i in menu:
        menu_str = menu_str + i.__str__() + '\n'
    return menu_str



# print(output_format(nutrients_analysis.new_recipe))