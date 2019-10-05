#!/usr/bin/python

class Recipe ( object ):
    def __init__ ( self, dishList ):
        self.name
        self.dishesCreated = dishList

class Dish ( object ):
    def __init__ ( self, name,  ):
        self.name = name

class Ingredient ( object ):
    def __init__ ( self, name ):
        self.name = name
        self.quantity = self.Quantity

    class Quantity ( object ):
        def __init__ ( self, value, metric ):
            self.value = value
            self.metric = metric

class Product ( object ):
    def __init__ ( self, name, cost, vendor, ingredientList=[] ):
        self.name = name
        self.cost = self.Cost
        self.vendor = self.Vendor
        self.ingredientsGranted = ingredientList
    class Cost ( object ):
        def __init__ ( self, value, currency ):
            self.value = value
            self.currency = currency
    class Vendor ( object ):
        def __init__ ( self, productBrandName=None, retailerName=None, barcode=None, productUrl=None ):


# class Dish ( object ):
#     def __init__ ( self, name,  ):
#         self.name = name

# class Ingredient ( object ):
#     def __init__ ( self, name ):
#         self.name = name
#     class Quantity ( object ):
#         def __init__ ( self ):

# class Product ( object ):
#     def __init__ ( self ):
#         self.advice = self.Advice()
#     class Advice ( object ):
#         def __init__ ( self ):
#         class Preservation:
#             def __init__ ( self ):
#         class Nutrition:
#             def __init__ ( self ):
#         class Alergen:
#             def __init__ ( self ):
#         class Preperation:
#             def __init__ ( self ):
        

