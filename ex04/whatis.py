import sys

try:
    assert len(sys.argv) < 3, "more than one argument is provided"

    if len(sys.argv) == 1:
        sys.exit(0)

    try:
        int_version = int(sys.argv[1])
    except ValueError:
        raise AssertionError("argument is not an integer")

    if int_version % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")
