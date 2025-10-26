import sys
from ft_filter import ft_filter


def filterstring(string, n):
    """
        Returns a list of words in `S` with length greater than `N`.
    """
    tokens = string.split()
    result_arr = ft_filter(lambda token: len(token) > n, tokens)
    return result_arr


def validate_string(S):
    """
        Check if S contains only alphanumeric characters or spaces
    """
    if not all(c.isalnum() or c.isspace() for c in S):
        raise AssertionError("The arguments are bad")
    return True


def main():
    """
        Main function to validate arguments and print filtered results.
    """
    try:
        assert len(sys.argv) == 3, "Must use strictly 2 args!"

        try:
            arg1 = sys.argv[1]
            validate_string(arg1)

            arg2 = int(sys.argv[2])
            if not isinstance(arg2, int):
                raise AssertionError
        except ValueError:
            raise AssertionError("Argument types must be [string, int]")
        print(filterstring(arg1, arg2))
    except AssertionError as e:
        print(f"Assertion Error: {e}")


if __name__ == "__main__":
    main()
