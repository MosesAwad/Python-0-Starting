
def ft_filter(function, iterable):
    """
    Filter items in `iterable` using `function` as the predicate.
    """
    result_arr = [i for i in iterable if function(i) is True]
    return result_arr


def main():
    """
    Demonstration of ft_filter function.
    """
    ages = [5, 12, 17, 18, 24, 32]

    def myFunc(x):
        if x < 18:
            return False
        else:
            return True

    adults = ft_filter(myFunc, ages)

    for x in adults:
        print(x)


if __name__ == "__main__":
    main()
