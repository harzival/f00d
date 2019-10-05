#!/usr/bin/python

class Dish:
    
    def __init__ ( self, name, quantity ):
        self.name = name
        self.quantity = quantity

class Recipe:

    def __init__ ( self, dish, ingredientList=[] ):
        self.dishProduced = dish
        self.ingredientsRequired = ingredientList

    def addIngredient ( self, ingredient, quantity ):
        self.ingredientsRequired.append ( ingredient )
        ingredient.quantity = quantity

class Ingredient:

    def __init__ ( self, name, quantity=None ):
        self.name = name
        self.quantity = quantity

class Quantity:

    def __init__ ( self, value, metric ):
        self.value = value
        self.metric = metric

class Product:

    def __init__ ( self, name, ingredientList, cost = None, vendor = None, advice = None ):
        self.ingredientsAttributed = ingredientList
        self.cost = cost
        self.advice = advice
    
    def addIngredient ( self, ingredient, quantity ):
        self.ingredientsRequired.append ( ingredient )
        ingredient.quantity = quantity
    
    def addIngredient ( self, ingredient, quantity ):
        pass

class Advice:

    def __init__ ( self, nutition = None, preservation = None, preperation = None,  ):
        self.nutrition = nutition
        self.preservation = preservation
        self.preperation = preperation

class Nutrition:
    pass

class Preservation:
    pass

class Preperation:
    pass




# >>> class Email:
# ...     def __init__(self):
# ...         self.is_sent = False
# ...     def send_email(self):
# ...         self.is_sent = True
# ...
# >>> my_email = Email()
# >>> my_email.is_sent
# False
# >>> my_email.send_email()
# >>> my_email.is_sent
# True

# class Outer(object):
#     def some_method(self):
#         # do something

#     class _Inner(object):
#         def __init__(self, outer):
#             outer.some_method()

#     def Inner(self):
#         return Inner(self)
