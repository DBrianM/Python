import json
import difflib

# Step 1: Download the JSON data from the provided link and save it as 'dictionary.json'.

# Step 2: Load the JSON data into a Python dictionary.
def load_dictionary():
    with open('dictionary.json', 'r') as file:
        return json.load(file)

dictionary = load_dictionary()

# Step 3: Create a function to get the definition of a word.
def get_definition(word):
    word = word.lower()  # Convert the word to lowercase for case-insensitive matching
    if word in dictionary:
        return dictionary[word]
    else:
        suggested_word = difflib.get_close_matches(word, dictionary.keys(), n=1)
        if suggested_word:
            suggestion = suggested_word[0]
            return f"Word not found. Did you mean '{suggestion}'? Definition: {dictionary[suggestion]}"
        else:
            return "Word not found in dictionary."

# Step 4: Handle cases where the entered word is not in the dictionary.
# Step 5: Handle different cases of input words (upper case, lower case, or mixed case).
def process_input():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        else:
            definition = get_definition(user_input)
            print(definition)

# Step 6: Implement a feature to suggest words if the input word is misspelled.

# Test the program
process_input()
