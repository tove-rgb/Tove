"""
1. Git vs  Git hub: version control software vs the platform that hosts it
2. Terminal vs command line: terminal is the whole place where you run code whereas the command line is where you type new lines
3. Local vs Remote repository: local repository is on computer, remote is one you can access via internet
4. Version Control: tracking changes to files
5. Staging area: purgatory for files being committed 
6. git add: makes git aware of your files
7. git commit: saves added snapshot to local history
8. git push: uploads files to remote repository
9. git status: where tf your files are in the process
10. git pull: almost oppisite of push, takes remote stuff into local
11. pwd: print working directory
12. ls: lists files/repositories in current directory
13. cd: change directory
14. nano: opens and edits a file in terminal
15. touch: updates file to most recent, make file
16. mv: move can also rename
17. rm: remove aka delete
18. cat: read file contents, prints output onto screen


--- 2.2 Directory Tree ---

pwd will tell you what your current working directory is. 

ls will list all files in current working directory.

cd .. /briana_repo # or cd.. then cd briana_repo
git pull 

mv homework.py../judy_decal/ (idk I forgot how to do this, gotta go back then back down)

cd ../judy_decal

cat homework.py

git add
git commit -m "saving homework"
git push

git status, Judy probably did not add and/or commit the files before pushing them. if you don't add then the files cannot be pushed

cd Recent/

--- Draw Your Directory Tree ---
did it

--- Homework 3 Review --- 
"""
#3.1 Data Types
def checkDataType (input):
    return type(input)
print(checkDataType(10))

#3.2 Conditionals
def evenOrodd(input):
    if input % 2 == 0:
        return "Even"
    else:
        return "odd"
print(evenOrodd(3))

# --- Loops ---
numbers = [0,2,4,5,10,70,95]
def sumWithLoops (numbers):
    summation = 0
    for digit in numbers:
        summation = digit + summation
    return summation
print(sumWithLoops(numbers))
print(sum(numbers))

# --- Homework 4 Review 
#5.1 Lists 
abcs = ['a','b','c']

print(abcs * 2)
"""
def duplicateList(abcs):
    result = []
    for index in abcs:
        for x in (index, index):
            result.append(x)
            return result

print(duplicateList(abcs))

IDKKK
"""
def duplicate_list(abcs):
    return [x for item in abcs for x in (item, item)]
print (duplicate_list(abcs))
# IDKKK HOW THIS ONE WORKS BUT IT DOES, Got help but still confused 

# 5.2 Debugging 
"""
def square(num)
    return num * num

This function is missing a colon
"""
def square(num):
    return num * num
print (square(3))