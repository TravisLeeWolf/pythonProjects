"""
Code to convert text into morse code.
Morse code list taken from https://www.sckans.edu/~sireland/radio/code.html
"""
import pandas as pd


def csv_to_dict(csv_filename: str) -> dict:
    """Takes the file name (str) of the csv and converts it into a 
    dictionary for use in the converter."""
    morse_code = pd.read_csv(csv_filename,
                            header=None,
                            index_col=0,
                            squeeze=True).to_dict()
    return morse_code


def get_user_text() -> str:
    """Prompts the user for the text to convert and returns (str) that
    text in upper case."""
    user_text = input("Type in the text you'd like to convert:\n").upper()
    return user_text


def convert_to_morse(text: str, code: dict) -> str:
    """Takes the user text (str) and morse code (dict) and returns (str)
    the text converted into morse code."""
    converted_text = ""
    for char in text:
        try:
            _value = code.get(char)
            converted_text = converted_text + _value + " "
        except:
            if char == " ":
                converted_text = converted_text + "   "
            else:
                converted_text = converted_text + "?"
    return converted_text


def main():
    morse_code = csv_to_dict("morse_code.csv")
    user_text = get_user_text()
    converted_text = convert_to_morse(user_text, morse_code)
    print(f"The morse code converted text is:\n{converted_text}")

main()

# ⚪
# ➖