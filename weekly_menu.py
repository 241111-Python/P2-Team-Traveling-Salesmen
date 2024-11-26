import nutrients_analysis
from recipe import Recipe


monday_menu = []
tuesday_menu = []
wednesday_menu = []
thursday_menu = []
friday_menu = []
saturday_menu = []
sunday_menu = []

# Put full recipe object in each day
# Calculate daily nutrients for single serving
# Total prep time per day
# Total time per day
# Total time per week

daily_time = 0
weekly_time = 0

def total_time_per_day(menu):
    for i in menu:
        daily_time = daily_time + nutrients_analysis.total_time(i)

def total_time_per_week():
    pass

# Nutrients daily value for each day that you inputed recipes for
def daily_nutrients(menu):
    total_kcal = 0
    total_carbs = 0
    total_fibre = 0
    total_fat = 0
    total_sugars = 0
    total_salt = 0
    total_protein = 0
    total_nutrients_list = []

    for i in menu:
        total_kcal = total_kcal + int(i.nutrients['kcal'] / i.serves)
        total_carbs = total_carbs + int(i.nutrients['carbs'].strip('g')) / i.serves
        total_fibre = total_fibre + int(i.nutrients['fibre'].strip('g')) / i.serves
        total_fat = total_fat + int(i.nutrients['fat'].strip('g')) / i.serves
        total_sugars = total_sugars + int(i.nutrients['salt'].strip('g')) / i.serves
        total_salt = total_salt + int(i.nutrients['salt'].strip('g')) / i.serves
        total_protein = total_protein + int(i.nutrients['protein'].strip('g')) / i.serves
    
    total_nutrients_list = [total_kcal, total_carbs, total_fibre, total_fat, total_sugars, total_protein, total_salt]

    return total_nutrients_list
    

        


