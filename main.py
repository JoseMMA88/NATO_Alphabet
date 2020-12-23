import pandas


data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in data_frame.iterrows()}
print(nato_dict)

asking = True
while asking == True:
    try:
        word = input("Enter a word: ")
        nato_list = [nato_dict[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(nato_list)
        asking = False
