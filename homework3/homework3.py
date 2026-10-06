
# 3 Print Functions
# --- 3.1 Say Goodbye ---
def say_goodbye (name):
	print ("Goodbye,",name) #this function says goodbye to a name
name = "Python Instructors"
say_goodbye (name)

# --- 3.2 Area of a Circle ---
def area_of_circle(radius):
	return 3.14*2*radius # this function gives the area 
radius = 3
print (area_of_circle (radius))

# 4 Return Functions
# --- 4.1 Subtract, Multiply, and Divide ---
def subtract(a,b):
	return a - b #this function subtracts numbers
a = 4
b = 3
print(subtract (a,b))
#prints 1
def multiply (a,b):
	return a*b #multiplies axb
print (multiply(a,b))
#prints 12
def divide (a,b):
	return a/b # divides a by b
print (divide(a,b))
#prints 1.33

# 5 Conditionals
# 5.1 What Should I Wear?
def what_should_I_wear (temps):
	return (min(temps),max(temps)) #returns min and max of temps as tuple
temps = [45,50,56,62,49]
print (what_should_I_wear(temps))
#prints (45,62)

# --- 5.2 Check if it's the Weekend --- 
def weekend (day):
	if day <= 5:
		return "False"
	else:
		return "True"
Monday = 1
Tuesday = 2
Wednesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7
day = Sunday
print(weekend (day))
# prints True

# --- 5.3 Fuel Efficiency Calculator ---
def efficiency (distance, fuel):
	return distance/fuel #and "miles per gallon"
distance = 20
fuel = 30
print (efficiency (distance, fuel))
# prints number, can't figure out how to get it to print with units

# --- 5.4 Secret Code ---
def secret_code (num):
	n = len(str(num))
	digit = num % 10
	num = num-digit
	num = num // 10
	num = num + digit *(10**(n-1))
	return num
print(secret_code (12345))
12345
5
1234
#used the internet to help with getting results right next to one another

# Using "Code With TJ" to explain how to do this:
def secret_code (num):
	n = len(str(num))
	last_digit = num % 10
	rest_figits = num // 10
	return last_digit*(10**(n-1)) + rest_figits
print(secret_code (12345))


# 6 Loops
# --- 6.1 Oski Stole Your Power ---
def exponential (x,y):  
	value = x
	for i in range (1,y):
		value = value * x
		return value 
	for i in range (y,-1):
		value = 1/(value*x)
		return value
print(exponential(2,-4))
# my code doesn't work for negatives 
# Doing it again with Giraffe Academy
def raise_to_power (x,y):
	result = 1
	for index in range (y):
		result =result * x #as it runs through the equation y times it continues to multipy x by x
	return result
print (raise_to_power(3,2))

# --- 6.2 Min and Max with Loops!
# 6.2.1
list1 = [3,5,2,8,9,6]
def one_way (list1):
	if not list1: # this finds the minimum, peer support from reagan
		return None
	mini = list1 [0]
	for d in list1:
		if d < mini:
			mini = d
	return mini
print (one_way(list1))

def one_way (list1):
	if not list1:
		return None
	maxi = list1 [0]
	for d in list1:
		if d > maxi:
			maxi = d
	return maxi
print (one_way(list1))


#6.2.2
def second_way (list1):
	mini = list1 [0]
	for d in list1 :
		while d >= mini:
			mini = mini 
		d = mini 
	return mini
print (second_way(list1))



#6.3 Calculate Sum
"""
def summation (number):
	f = 10 ** len(str(number))
	while 
	g = number // f
	h = number // f
	j = number // f/
	return g+h+j

number = 4356
"""

def summation (value):
    final = 0
    while value > 0:
        final = final + value % 10
        value = value // 10
    return final

print (summation (12345))
# My function prints when the other functions are commented out, but not when they are here. I do not know why. 