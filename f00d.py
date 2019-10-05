#!/usr/bin/python

class Meal ( object ):
    def __init__ (self, name ):
        self.name = name
        self.serves
        self.recipe
        self.ingredientList
        self.prepTime
        self.cookTime
        self.canBeFrozenAndDefrosted
        self.cuisine
        self.type.snack
        self.type.dinner
        self.type.lunch
        self.type.breakfast
    def snack (self): pass
        
        
class Quantity ( object ):
    def __init__ ( self, metric, value ):
        self.metric = metric
        self.value = value
    def kg ( self, value ):
        value = value * 1000
        return Quantity ( "grams", value )
    def g ( self, value ):
        return Quantity ( "grams", value )
    def l ( self, value ):
        value = value * 1000
        return Quantity ( "millilitre", value )
    def ml ( self, value ):
        return Quantity ( "millilitre", value )

class Dates ( object ):
    def __init__ ( self, date, label ):
        self.date = date
        self.label = label
        self.bestBefore
        self.useBy
        self.displayUntil
        self.sellBy = self.displayUntil
        self.useByOnceSealBroken

class PreservationInfo ( object ):
    def __init__ ( self, dates ):
        self.washed
        self.keepRefrigerated
        self.suitableForFreezing
        self.sealBroken
        self.nonPerishable
        self.precooked
        self.hasBeenFrozen
        self.isFrozen
        self.dates = dates

class NutritionInfo ( object ):
    def __init__ ( self, fat, energy, artificialFlavours, artificialColours, noAddedSugar ):
        self.fat
        self.fatOfWhichSatures
        self.energy
        self.carbohydrates
        self.carbohydratesOfWhichAreSugars
        self.salt
        self.protien
        self.artificialFlavours
        self.artificialColours
        self.noAddedSugar
        self.unsweetened

class Ingredient ( object ):
    def __init__ (self, name, quantity ):
        self.name = name
        self.quantity = quantity

class IngredientList ( list ):
    def __init__ (self, listOfIngredients ):
        self = listOfIngredients

class PurchasedIngredient ( Ingredient ):
    def __init__ ( self, ingredientName, specificItemName, brandName, quantity, cost, preservationInfo, nutritionInfo, ingredientList ):
        Ingredient.__init__( self, ingredientName, quantity )
        self.ingredientName     = self.name
        self.specificItemName   = specificItemName
        self.brandName          = brandName 
        self.quantity           = quantity
        self.cost               = cost
        self.preservation       = preservationInfo
        self.dates              = self.preservation.dates
        self.nutrition          = nutritionInfo
        self.ingredients        = ingredientList









duck = Meal ("duck")
print ( isinstance (duck, Meal ) )
