# --- September 23 Functions, Conditions, Loops Practice Questions --- 

# def minimum ([40,80,10,30,50,20]):

list = [40,80,10,30,50,20]
def minimum (list): 
    return min (list)

list2 = [23045,34930]

def minimum(x):
    return min(list)

print (min(list))

def maximum(list):
    return max(list)
#basically this is a bad example bc min/max function already exits

def isprime (num):
    if num <= 0 or type(num) != int:
        return "Not Prime"
    else:
        if num == 1:
            return "Neither"
        elif num == 2:
            return "Is Prime"
        else: 
            if num % 2 == 0:
                return "Not Prime, composite number"
            else:
                for i in range (1, num):
                    if num % i == 0:
                        return "Not Prime, composite number"
                    else:
                        return "Prime Number"
print(isprime(34))