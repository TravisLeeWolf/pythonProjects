"""
Morse code list taken from https://www.sckans.edu/~sireland/radio/code.html
"""
import pandas as pd


# Make dictionary from morse code csv
morse_code = pd.read_csv('morse_code.csv',
                        header=None,
                        index_col=0,
                        squeeze=True).to_dict()

user_text = input("Type in the text you'd like to convert:\n").upper()

converted_text = ""
for char in user_text:
    try:
        _value = morse_code.get(char)
        converted_text = converted_text + _value + " "
    except:
        if char == " ":
            converted_text = converted_text + "   "
        else:
            converted_text = converted_text + "?"
print(f"The morse code converted text is:\n{converted_text}")