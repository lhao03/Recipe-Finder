import os
import requests

# function for searching for recipes
# search criteria includes: includeingredients,cuisine,diet,excludeingridients,maxreadytime,type


class Spoonacular:
    API_URL = "https://api.spoonacular.com/recipes/complexSearch?number=1&instructionsRequired=true&fillIngredients=true&"
    API_KEY = "apiKey=40770178730f426c894749c027909c7a"
    API_URL_IMAGES = "https://api.spoonacular.com/recipes/"
    IMAGE_CONT = "/ingredientWidget"

    def user_interface(self):
        print("Hi! Recipe Nest helps you use ingridients that you have lying around. Just input your ingridients and I'll find you a recipe!")
        print("You can filter by cuisine, diet, maximum preperation time and type of meal. If there are ingridients you do not want in your recipes simply put no infront of the ingrident!")
        print("Ingridients here:")
        foods = input()
        print("Cuisine here:")
        cuisine = input()
        print("Diet here:")
        diet = input()
        print("Max time here:")
        max_time = input()
        print("Meal type here:")
        meal_type = input()
        self.search_recipes(ingredients=foods, cuisine=cuisine,
                            diet=diet, time=max_time, mealtype=meal_type)

    def search_recipes(self, ingredients, diet, mealtype, time, cuisine):
        i = 1
        while i > 0:
            # for the ingridients to include - list
            user_ingredients = ingredients
            final_ingre = self.check_inputs(user_ingredients)
            if final_ingre == None:
                pass
            else:
                response = "includeIngredients=" + final_ingre + "&"

            # for the cuisines to include - list
            user_cuisine = cuisine
            final_cuisine = self.check_inputs(user_cuisine)
            if final_cuisine == None:
                pass
            else:
                response = response + "cuisine=" + final_cuisine + "&"

            # for the diet - string
            if diet.strip() == "none":
                pass
            else:
                response = response + "diet=" + diet.strip() + "&"

            # for time - dict/string
            final_time = self.check_time(time)
            if final_time == None:
                pass
            else:
                response = response + "maxReadyTime=" + str(final_time) + "&"

            # for meal type - string
            i = i - 1
            if mealtype.strip() == "none":
                pass
            else:
                response = response + "type=" + mealtype.strip() + "&"
        query = Spoonacular.API_URL + response + Spoonacular.API_KEY
        # response = requests.get(query)
        # return response.json()
        print(query)
        return query

    def join_inputs(self, user_inputs):
        if len(user_inputs) == 1:
            return user_inputs[0]
        else:
            X_get = [("+" + x.strip()) for x in user_inputs]
            X_joined = user_inputs[0] + "," + ",".join(X_get)
            return X_joined

    def check_inputs(self, the_input):
        if the_input[0].strip() == "none":
            return None
        else:
            return self.join_inputs(the_input)

    def check_time(self, usertime):
        if usertime == "none" or usertime == "":
            return None
        elif usertime["unit"] == "min":
            return usertime["amount"]
        elif usertime["unit"] == "h":
            return (usertime["amount"] * 60)

    # def show_ingredients(self):


# response = requests.get("https://api.spoonacular.com/recipes/complexSearch?includeIngredients=apple,+cheese&type=main&apiKey=40770178730f426c894749c027909c7a")
