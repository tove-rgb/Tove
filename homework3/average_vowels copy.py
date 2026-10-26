# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.
def counting_vowels_and_consonants (word):
    vowels = "aeiouAEIOU"
    num_vowel = 0
    num_consonants = 0
    for letter in word:
        if letter.isalpha():
            if letter in vowels:
                num_vowel +=1
        else:
            num_consonants += 1
    return (num_vowel, num_consonants)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    passage = paragraph.splitlines() #seperates the lines
    sentences = len(passage) #notes the length of each sentence 
    sentence_vowels = 0
    sentence_consonants = 0
    for sentence in passage:
        vowels, consonants = counting_vowels_and_consonants (sentence) #using old function
        sentence_vowels += vowels # adds vowels to the output
        sentence_consonants += consonants #adds the consonants to output
    average_vowels = sentence_vowels / sentences
    average_consonants = sentence_consonants / sentences
    return (sentences, average_vowels, average_consonants)
# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)
sentences, average_vowels, average_consonants = average_vowels_and_consonants (paragraph)
# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
print(f"The number of sentences in this paragraph is {sentences}. The average vowels per sentence is {average_vowels}. The average consonants per sentence is {average_consonants}.")

#my code doesn't work brooo