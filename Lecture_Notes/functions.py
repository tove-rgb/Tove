name = "tove"

#print("hello", name)

def say_hello (name):
    print("hello",name)

say_hello(name = "Jerry")

def add(a,b):
    return(a+b)
    
print(add(7,8))

def check_num (num): 
    if num > 0: 
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print (check_num(42))

print(41<0)

#print(check_num(0))
#print(True and True)
#print(True and False)

def can_vote(age,is_citizen):
    if age >= 18 and is_citizen:
        print("You can vote!")
    else:
        print("You cannot vote.")
can_vote(19,True)

def is_weekend(day):
    if day== "Saturday" or day == "Sunday":
        return "It is the weekend"
    else:
        return "It is not the weekend"
print(is_weekend("Monday"))

# --- Loops ---
for i in range(10):
    print(i)

fruit_basket = ["Lychee","Mango","Nectarine"]
for fruit in fruit_basket:
    print(fruit)

def countdown (start):
    while start > 0:
        print("T-", start)
        start -=1
    print("Lift off!!!!")
countdown (10)

def temperature(temp):
    if 65< temp< 80:
        return "Its warm today!"
    elif temp >80:
        return "It's hot today!"
    else:
        return "brrr"
temperature = "80"