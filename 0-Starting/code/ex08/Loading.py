import os


def ft_tqdm(lst: range) -> None:
    """
        Iterate over a range while displaying a dynamic terminal progress bar.
        Shows percentage, a graphical bar, and current/total iterations.
        Automatically adjusts to terminal width. Yields each element in lst.
    """
    total = len(lst)
    size = os.get_terminal_size()
    reserved = 8 + len(str(total)) * 2 + 25  # Note 1
    bar_length = size.columns - reserved

    for i in lst:
        progress = (i + 1) / total
        filled = int(progress * bar_length)
        bar = '█' * filled + ' ' * (bar_length - filled)
        display = f"{int(progress * 100):3d}%|{bar}| {i + 1}/{total}"
        print(f"\r{display}", end='', flush=True)  # Note 2
        yield i  # Note 3

    print()


"""
    NOTES

    Note 1
        * 8 because 100% is a max of 4 chars, 2 pipes, 1 space, and the /
        * len(str(total)) * 2 because if len is 1000 for example, then bar
            would say 1000/10000 when completed
        * The plus 25 is just extra space to get it to align with the display
            of the actual tqdm function. That extra space is because tqdm
            also displays timestamps and iterations/second rate but we dont.

    Note 2
        * When the print finishes, the final cursor position is after the last
            character printed — so after the iteration counter, as in 222/222
            for example.
        * What you only ever see is the final result of the write, not the
            intermediate cursor motion. That's why the \r is put at the start
            of the string being printed. By the end of the iteration, the
            cursor is in fact at the end of the line, but the next print of
            the next iteration is the one that returns it back to the start.
            Yes, the next print will automatically be on the same line
            because we set end="", so the \r is just moving the cursor back
            to the beginning of that line.

    Note 3
        Consider something like this:
            for elem in ft_tqdm(range(333)):
                sleep(0.005)

        * The for loop inside ft_tqdm is not benefitting from yield at all.
        * That internal loop just runs to generate each item and update
            the progress bar.
        * The benefit of yield goes entirely to the outside for loop that’s
            consuming ft_tqdm.
"""
