spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_foods_list = [food["name"]  for food in spicy_foods]
    return spicy_foods_list

def get_spiciest_foods(spicy_foods):
    spicy_foods_list=[food for food in spicy_foods if food["heat_level"]>3]
    return spicy_foods_list
    
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"]>5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"]*"🌶" }')


def get_average_heat_level(spicy_foods):
    heat_levels =[]
    for food in spicy_foods:
        heat_levels.append(food["heat_level"])
        
    return sum(heat_levels)/ len(heat_levels)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods


# print(get_names(spicy_foods))
# print(get_spiciest_foods(spicy_foods))
# print(print_spicy_foods(spicy_foods))
# print(get_spicy_food_by_cuisine(spicy_foods, "American"))
# print(print_spiciest_foods(spicy_foods))
# print(get_average_heat_level(spicy_foods))
'''print(create_spicy_food(
    spicy_foods,
    {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
))'''