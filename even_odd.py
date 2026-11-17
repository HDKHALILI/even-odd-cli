import sys

EXIT_ABORTED = 1


def get_int() -> int:
    """Prompt the user until a valid base-10 integer is entered and return it.

    Accepts optional leading/trailing whitespace, a '+' or '-' sign, Unicode
    decimal digits (including non-Latin numerals such as '٣'), and
    a single underscore between digits (e.g., '1_000', '1_000_000').

    Prompt again if the input exceeds the maximum allowed digit count.

    Raises:
        EOFError: If the input stream ends before a valid integer is read.
    """
    max_digits = sys.get_int_max_str_digits()

    while True:
        try:
            input_str = input("Enter an integer: ")
            return int(input_str)
        except ValueError:
            if len(input_str) > max_digits:
                print(
                    f"Integer is too large (max {max_digits} digits). Please enter a smaller integer."
                )
            else:
                print("Invalid integer. Please enter a valid integer.")


def is_even(integer: int) -> bool:
    """Return True if the given integer is even, False otherwise."""
    return integer % 2 == 0


def main() -> None:
    try:
        integer = get_int()
    except KeyboardInterrupt:
        print("\nProgram cancelled by user.")
        sys.exit(EXIT_ABORTED)
    except EOFError:
        if sys.stdin.isatty():
            print("\nInput cancelled by the user.")
            sys.exit(EXIT_ABORTED)
        else:
            print(
                "\nError: Reached end of input without receiving a valid integer.",
                file=sys.stderr,
            )
            sys.exit(EXIT_ABORTED)

    if is_even(integer):
        print("even")
    else:
        print("odd")


if __name__ == "__main__":
    main()
