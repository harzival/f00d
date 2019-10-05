class Ingredient ( object ):
    
    def __init__ (self, name, quantity ):

        self.name = name
        self.quantity = quantity

    class Quantity ( object ):

        def __init__ ( self, metric, value ):
            self.metric = metric
            self.value = value

        def kg ( self, value ):
            value = value * 1000
            return self._ ( "grams", value )

        def g ( self, value ):
            return Quantity ( "grams", value )

        def l ( self, value ):
            value = value * 1000
            return Quantity ( "millilitre", value )

        def ml ( self, value ):
            return Quantity ( "millilitre", value )

class Product ( object ):

    def __init__ ( 
        self, 
        productName         = None, 
        productBrandName    = None, 
        vendorList          = None,
        cost                = None,
        quantity            = None,
        preservationInfo    = None,
        nutritionInfo       = None,
        preperaionInfo      = None,
        ingredientInstances = None ):
        
        self.productName            = productName
        self.productBrandName       = productBrandName
        self.vendorList             = vendorList
        self.cost                   = cost
        self.preservation           = preservationInfo
        self.nutrition              = nutritionInfo
        self.ingredientInstances    = ingredientInstances

    class PreservationInfo ( object ):
       
        def __init__ ( self, 
            dates, 
            washed              = None, 
            keepRefrigerated    = None, 
            suitableForFreezing = None, 
            sealBroken          = None, 
            nonPerishable       = None, 
            precooked           = None, 
            hasBeenFrozen       = None, 
            isFrozen            = None ):

            self.washed                 = washed
            self.keepRefrigerated       = keepRefrigerated
            self.suitableForFreezing    = suitableForFreezing
            self.sealBroken             = sealBroken
            self.nonPerishable          = nonPerishable
            self.precooked              = precooked
            self.hasBeenFrozen          = hasBeenFrozen
            self.isFrozen               = isFrozen
            self.dates                  = dates

    class NutritionInfo ( object ):
        
        def __init__ ( self, 
            fat                         = None, 
            fatOfWhichSatures           = None, 
            energy                      = None, 
            carbohydrates               = None, 
            carbohydratesOfWhichSugars  = None, 
            salt                        = None, 
            protien                     = None, 
            artificialFlavours          = None, 
            artificialColours           = None, 
            noAddedSugar                = None, 
            unsweetened                 = None, 
            glutened                    = None,
            statedIngredients           = None ):

            self.fat                        = fat
            self.fatOfWhichSatures          = fatOfWhichSatures
            self.energy                     = energy
            self.carbohydrates              = carbohydrates
            self.carbohydratesOfWhichSugars = carbohydratesOfWhichSugars
            self.salt                       = salt
            self.protien                    = protien
            self.artificialFlavours         = artificialFlavours
            self.artificialColours          = artificialColours
            self.noAddedSugar               = noAddedSugar
            self.unsweetened                = unsweetened
            self.statedIngredients          = statedIngredients