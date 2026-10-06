# Lists 
#3.1 List Operations 
fav_foods = ["Cheese", "Coffee", "Pasta", "Seafood","Dumplings"]
print (fav_foods[1])
print (fav_foods [-1])
fav_foods.append("Strawberries")
fav_foods.insert(0,"Apples")
fav_foods.remove("Pasta") #Apples, cheese, coffee, seafood dumplings, strawberries
print (fav_foods)
print(len(fav_foods))

def upper_case(fav_foods):
    for foods in fav_foods:
        foods.upper()
    return (fav_foods)
print(upper_case(fav_foods))
# error message "attribute error: list object has no attribute upper"
# Isn't doing the function

print(fav_foods[0:6:5])
def potato(fav_foods):
    for foods in fav_foods:
        if foods == "Potato":
            return "A potato!"
    else:
        return "No potato!"
print (potato(fav_foods))
# IDK HOW TO get things from lists broooo
