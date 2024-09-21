# This exercise is about creating a program which allows the user to search for recipes based on their names, preparation times, or ingredients used. The program should read the recipes from a file submitted by the user.

# Each recipe consists of three or more lines. The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.

# Pancakes
# 15
# milk
# eggs
# flour
# sugar
# salt
# butter

# Meatballs
# 45
# mince
# eggs
# breadcrumbs

# Tofu rolls
# 30
# tofu
# rice
# water
# carrot
# cucumber
# avocado
# wasabi

# Cake pops
# 60
# milk
# bicarbonate
# eggs
# salt
# sugar
# cardamom
# butter

# Hint: it might be best to first read through all the lines in the file and pop them into a list, which is then easier to manipulate in the way described in the exercise.

# Search for recipes based on the name of the recipe
# Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose name contains the given search string. The names of these recipes are then returned in a list.

# An example of the function in action:

# found_recipes = search_by_name("recipes1.txt", "cake")

# for recipe in found_recipes:
#     print(recipe)

# Pancakes
# Cake pops

# As you can see in the example above, the case of the letters is irrelevant. The search term cake returns both Pancakes and Cake pops, even though the latter is capitalized.

# NB: If Visual Studio can't find the file and you have checked that there are no spelling errors, take a look at these instructions.

# Search for recipes based on the preparation time
# Please write a function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. The function should go through the file and select all recipes whose preparation time is at most the number given.

# The names of these recipes are again returned in a list, but the preparation time should be appended to each name. Please have a look at the example below.

# found_recipes = search_by_time("recipes1.txt", 20)

# for recipe in found_recipes:
#     print(recipe)

# Pancakes, preparation time 15 min

# Search for recipes based on the ingredients
# A word of caution: this third part of the exercise is considerably more demanding than the previous two. If you feel like you aren't making headway, it may be worth your while to move on, complete the other exercises in this part of the material, and then come back to this exercise if you have time later. Remember, you can submit and receive points for the first two parts of this exercise even if you haven't completed the third part.

# Please write a function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. The function should go through the file and select all recipes whose ingredients contain the given search string.

# The names of these recipes are returned in a list just like in the second part, with the preparation time appended. Please have a look at the example below.

# found_recipes = search_by_ingredient("recipes1.txt", "eggs")

# for recipe in found_recipes:
#     print(recipe)

# Pancakes, preparation time 15 min
# Meatballs, preparation time 45 min
# Cake pops, preparation time 60 min

def recipe_list(filename: str):
    # store the recipes first in a list
    recipes = []
    with open(filename) as new_file:
        recipe = {}
        ingredients = []
        for line in new_file:
            line = line.strip()
            if not line:
                # empty line check
                if recipe:
                    recipe["ingredients"] = ingredients
                    recipes.append(recipe)
                    # reset
                    recipe = {}
                    ingredients = []
            elif "name" not in recipe:
                recipe["name"] = line
            elif "time" not in recipe:
                recipe["time"] = int(line)
            else:
                ingredients.append(line)

    # since last item of recipes wont have new line, need to add anyways
    if recipe:
        recipe["ingredients"] = ingredients
        recipes.append(recipe)

    return recipes

def search_by_name(filename: str, word: str):
    recipes = recipe_list(filename)
    found = [recipe["name"] for recipe in recipes if word.lower() in recipe["name"].lower()]
    return found

def search_by_time(filename: str, prep_time: int):
    recipes = recipe_list(filename)
    found = [f"{recipe['name']}, preparation time {recipe['time']} min" for recipe in recipes if recipe["time"] <= prep_time]
    return found

def search_by_ingredient(filename: str, ingredient: str):
    recipes = recipe_list(filename)
    found = [f"{recipe['name']}, preparation time {recipe['time']} min" for recipe in recipes if ingredient in recipe["ingredients"]]
    return found