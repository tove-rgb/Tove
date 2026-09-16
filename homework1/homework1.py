# File: homework1.py

# --- Variable and Data Types ---
a = 10
print (a)
print (type(a)) # a is an integer, a whole number with no decimals
b = 1.5 
print (b)
print (type(b)) # b is a float, a number with decimals
c = 3j
print (c)
print (type(c)) # c is a complex number, a number with a real and imaginary part
d = "hello"
print (d)
print (type(d)) # d is a string, a sequence of characters
e = [1, 2, 3]
print (e)
print (type(e)) # e is a list, an ordered collection of items
g = (1, 2)
print (g)
print (type(g)) # g is a tuple, an ordered collection of items that cannot be changed
h = ["apple", "banana", "strawberry"]
print (h)
print (type(h)) # h is a list, an ordered collection of items
i = True
print (i)
print (type(i)) # i is a boolean, a value that can be either True or False
j = None 
print (j)
print (type(j)) # j is a NoneType, a special type that represents the absence of a value
k = [True, "blue", 12]
print (k)
print (type(k)) # k is a list, an ordered collection of items
l = str(14)
print (l)
print (type(l)) # l is a string, a sequence of characters
m = 1e4
print (m)
print (type(m)) # m is a float, a number with decimals
'''
1. I found 8 different data types. 
2. Integers, floats, complex numbers, strings, lists, tuples, booleans, and Nonetype.
3. b and m are floats, d and l are strings, e and h are lists.
4. L is a string because the str() function converts the integer 14 into a string. 
5. range
n = range (0, 10)
print (n)
print (type(n)) # n is a range, a sequence of numbers
'''

# --- Booleans ---
print (10 > 9) #true
print (10 == 9) #false
print (10 <= 9) #false
print (bool("abc")) #true
print (bool(["apple", "cherry", "banana"])) #true
print (bool(True)) # true 
print (bool(False)) #false
print (bool(0)) #false
print (bool("")) #false
print (bool(" ")) #true
print (bool(())) #false
print (bool([])) #false
print (bool({})) #false
print (bool(True and False)) #false
print (bool(True and True)) #true
print (bool(False and False)) #false
print (bool (True or False)) #true 
print (bool(True or True)) #true
print (bool (False or False)) #false
print (bool(not(False))) #true 
print (bool(not(True))) #False
"""
1. True statements are ones that are correct, accurate, or valid. Whereas false statements are ones that are incorrect, inaccurate, or invalid.
2. I was most suprised by False False, I figured it translated to wrong is wrong, but that was not the case. 
3. One statement that will return true is bool(3) because 3 is a non-zero number.
4. One statement that will return false is bool(not(3)). Because 3 is a non-zero number, it will return true, but the not operator will negate it and return false.
"""

# --- Operators ---
# Arthmetic Operators
print (10 + 5) #15, + performs addition
print (10 - 5) #5, - performs subtraction
print (2 * 4) #8, * performs multiplication
print (6 / 3) #2.0, / performs division
print (5 % 2) #1, % performs modulus (internet term??) the remainder of the division
print (3 ** 2) #9, ** performs raising first number to second number power (exponentiation
print (15 // 2) #7, // performs floor division (internet term??) the largest integer less than or equal to the result.
# Comparison Operators
print (5 == 2) #false, == performs equality comparison
print (10 != 10) #false, != performs inequality comparison
print (2<5) #true, < performs less than comparison
print (12>5) #true, > performs greater than comparison
print (5<=6) #true, <= performs less than or equal to comparison
print (1>= 10) #false, >= performs greater than or equal to comparison
# Assignments Operators
x = 5
x += 5
print (x) #10, += adds the right and left
x -= 4
print (x) #6, -= subtracts the right from the left
x*= 3
print (x) #18, *= multiplies the right and left
"""
1. The operator 'and' adds two boolean values together. If both values are true, the result will be true. If either value is false, the result will be false.
2. The operator 'or' returns true if at least one of the boolean values is true. If both values are false, the result will be false.
3. The operator 'not' negates the value of the boolean.
4. The difference between / and // is that / performs regular division and returns a float, while // performs floor division and returns an integer.
5. The difference between % and // is that % returns the remainder of the division, while // returns the quotient.
6. To calculate the remainder when dividing two numbers, I would use the % operator. For example, 5 % 2 would return 1.
7. Assignment operators lowk confuse me. But I think I kinda got it. Basically they equate the variable to the result of theoperation.
"""

# --- Strings ---
my_string = "hello"
print (my_string) #Prints hello
print (my_string[0]) #Prints h
print (my_string[1]) #Prints e
print (my_string[2]) #Prints 1
print (my_string[3]) #Prints 1
print (my_string[4]) #Prints o
print (my_string[-1]) #Prints o
print (my_string[1:3]) #Prints el
print (my_string[0:5:2]) #Prints hlo
print (len(my_string)) #Prints 5, the length of the string
print (my_string + "goodbye") #Prints hellogoodbye
print (my_string * 7) #Prints hellohellohellohellohellohellohello
name = "Oski"
print ("hello, my nme is", name) #Prints hello, my name is Oski
print (f"hello, my name is {name}") #Prints hello, my name is Oski
"""
1. sclicing is a way to acces a portion of a string. I sliced the string in the second example through to the 9th. 
2. It prints hello, my name is Oski. 
3. It prints the same frase
4. The f string (second one)is more efficient and easier to read. And f strings allow for variables to be inserted directly into the string. You use {} to insert the variable into the string.
"""

# --- Terminal Commands ---
"""
cd
Changes directories. Use it to move from one folder to another 
Example: cd Desktop
ls
Lists the contents of the current directory. Use it to view files/folders.
Example: ls
ls -a
Lists all contents of the current directory, including hidden files/folders. Use it to view all files/folders.
Example: ls -a
mkdir
Makes a new directory. Use it to create a new folder.
Example: mkdir name_of_folder
cat
View the contents of a file. Use it to read a file.
Example: cat name_of_file
pwd
Prints the currentworking directory. Use it to see where you are in the file system.
Example: pwd
cd ..
Moves up one directory. Use it to go back to the previous folder/parent directory.
Example: cd ..
cd .
Stays in current directory. Use it to stay in the current folder.
Example: cd.
cd~
Brings you back to home directory. Use it to go back to starting. 
Example: cd~
cp
Copies files or directories. USe it to make duplicates and have them stored in different locations/
Example: cp a.text b.text (whatever is in A is copied ito B aka duplicate)
mv
Move or rename files/directories. Use it to change the location of a file.
mv filename locationname
rm
Dangerous. Permenantly deletes files and directories. 
Example: rm filename
clear
clear terminal screen. Use it to get a new workspace without deleting any data.
Example: clear 
grep
Search for specific words/phrases/patterns in text files 
Example: grep "words/phrase/patter" filename
1. 
    rmdir
    Deletes empty directories
    Example: rmdir directoryname
    locate
    Find files using a database
    Example: locate file_name
    touch
    create empty files
    Example: touch newfilename 
2. Both list files in directory but ls -a also shows hidden files
3. A hidden file is one that exists but isn't able to be viewed without a special command.
4. 
    mikdr -title
    Makes a new directory witht the name "title"
    grep -i
    Case-sensitive search
    clear -x
    Clears visible screen but you can still scroll up to see past work
"""
