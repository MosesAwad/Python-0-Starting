import sys


def to_morse_code(string):
    """
        Convert a given alphanumeric string into its Morse code
        representation. Spaces are converted to '/', and characters
        are separated by single spaces.
    """
    nested_morse = {
        " ": "/",
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----."
    }

    morse_code = ""
    string = string.upper()
    for i in range(len(string)):
        morse_code += nested_morse[string[i]]
        if i < len(string) - 1:
            morse_code += " "

    return morse_code


def validate_string(string):
    """
        Check if S contains only alphanumeric characters or spaces
    """
    if not all(c.isalnum() or c.isspace() for c in string):
        raise AssertionError("The arguments are bad")
    return True


def main():
    try:
        assert len(sys.argv) == 2, "Invalid number of arguments"
        validate_string(sys.argv[1])
        print(to_morse_code(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
