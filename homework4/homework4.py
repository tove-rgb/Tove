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
"""
def upper_case(fav_foods):
    for foods in fav_foods:
            foods.upper()
    print (upper_case) 
print(upper_case(fav_foods))
"""
for foods in fav_foods:
     print(foods.upper())

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

# --- 3.2 Slicing and Striding ---
#numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers = list(range(1,21,1)) # First I did this, I needed the list()Listnumbers = range(1,21,1)
print (numbers)
def get_first_15(numbers):
    list1 = numbers [0:15:1]
    return list1
list1 = get_first_15(numbers)
print (list1) #for these two I needed to set an output equal to statement so I could put it into the new function

def get_every_5th(list1):
    list2 = list1[::5]
    return list2
list2 = get_every_5th(list1)
print(list2)

def reverse_and_stride(list2):
    list2.reverse
    list3 = list2[::3]
    return list3
list3 = reverse_and_stride(list2)
print(reverse_and_stride(list2))
# this lowk took a while to figure out. Basically once I perform list2.reverse I don't need to set that equal to a new variable because the functions runs top to bottom

# --- 3.3 Nested Lists ---
nestednumbers = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print (nestednumbers[2]) #error out of range :print (nestednumbers[3])
print (nestednumbers[1][1]) # [] print (nestednumbers[1:1]
nestednumbers.append([10,11,12])

def sum_nested(nestednumbers):
    row = 0
    sum = 0
    while row <= 3:
        sum = sum + nestednumbers[row][0]+nestednumbers[row][1]+nestednumbers[row][2]
        row = row+1
    return sum
print(sum_nested(nestednumbers))
print(1+2+3+4+5+6+7+8+9+10+11+12)

# --- 3.4 Create a 5x5 List ---
by5=[]
def create_5by5():
    row = 0
    for row in by5:
        by5.append("1,2,3,4,5,")
#Rework aka doesn't work

# 4 Dictionaries
# --- 4.1 Dictionary Operations ---
ages = {
    "Katie": 30,
    "Mariam": 42,
    "Safia": 25, 
    "Mira": 48
}
print(ages)

print(ages["Katie"])
ages["Mira"] = 100
ages["Milana"] = 52
del ages["Mariam"]

#ages.items
#for keys, values in ages
#for keys in ages:

for key, value in ages.items():
    print(f"{key}: {value}")
    #got help with, don't super get f-strings

#Favorite

def sum_nested(nestednumbers):
    row = 0
    sum = 0
    while row <= 3:
        sum = sum + nestednumbers[row][0]+nestednumbers[row][1]+nestednumbers[row][2]
        row = row+1
    return sum
print(sum_nested(nestednumbers))


# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.


# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?

