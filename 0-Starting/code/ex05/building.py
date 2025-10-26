import sys


def paragraph_tally(string: str):
    """
        This function takes a single string argument and displays the sums
        of its upper-case characters, lower-case characters, punctuation
        characters, digits, and spaces.
    """
    lower_count = 0
    upper_count = 0
    punc_count = 0
    space_count = 0
    digit_count = 0
    char_count = 0

    for i in range(len(string)):
        if string[i].islower():
            lower_count += 1
        elif string[i].isupper():
            upper_count += 1
        elif string[i] == " " or string[i] == "\n":
            space_count += 1
        elif string[i].isdigit():
            digit_count += 1
        elif string[i] in "!\"#$%&'()*+,-./:;<=>?@[]\\{}|":
            punc_count += 1
        char_count += 1

    print((
        f"The text contains {char_count} characters:\n"
        f"{upper_count} upper letters\n"
        f"{lower_count} lower letters\n"
        f"{punc_count} punctuation marks\n"
        f"{space_count} spaces\n"
        f"{digit_count} digits"
    ))


def main():
    """
        Reads input text (from command line or user) and counts character types
        using paragraph_tally(). Raises AssertionError for too many arguments
        and EOFError for unexpected end-of-input.
    """
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
        line = ""
        if len(sys.argv) == 1:
            try:
                line += input("What is the text to count?\n")
                # Because input doesn't include the \n at the end, so we
                # add it manually
                line += "\n"
            # This error is triggered when you hit Ctrl + D at the start
            # of the input prompt
            except EOFError:
                pass
        else:
            line += sys.argv[1]
        paragraph_tally(line)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
