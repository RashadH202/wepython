import pandas as pd

#read CSV directly
data = pd.read_csv("nato_phonetic_alphabet.csv")

#create a dictionary using dictionary comprehension
pheonetic_dict = {row.letter: row.code for _, row in data.iterrows()}
print(pheonetic_dict)

#get users input and handle invalid characters
word = input("enter a word: ").upper()
output_list = [pheonetic_dict.get(letter, letter) for letter in word]

#output the phonetic code words
print(output_list)