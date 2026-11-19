import sys

EXIT_SUCCESS = 0
EXIT_ABORTED = 1
DEFAULT_MAX_STR_DIGITS = 4300


def get_int() -> int:
    """Prompt until a valid base-10 integer is entered and return it.

    Accepts optional leading/trailing whitespace, a '+' or '-' sign,
    Unicode decimal digits (including non-Latin numerals such as '٣'),
    and a single underscore between digits (e.g., '1_000').

    Prompt again if the input exceeds the maximum allowed digit count.

    Raises:
        EOFError: If the input ends before a valid integer is read.
    """
    max_digits = getattr(
        sys, "get_int_max_str_digits", lambda: DEFAULT_MAX_STR_DIGITS
    )()

    while True:
        try:
            input_str = input("Enter an integer: ")
            return int(input_str)
        except ValueError:
            cleaned_input = input_str.strip().lstrip("+-")
            if cleaned_input.isdigit() and len(cleaned_input) > max_digits:
                print(
                    f"Integer is too large (max {max_digits} digits). Please enter a smaller integer."
                )
            else:
                print("Invalid integer. Please enter a valid integer.")


def is_even(integer: int) -> bool:
    """Return True if the given integer is even, False otherwise."""
    return integer % 2 == 0


def main() -> None:
    """Get an integer and print whether it is 'even' or 'odd'.

    Returns 0 on success, or 1 after printing a message to stderr if
    input is interrupted or reaches EOF before a valid integer is read.
    """
    try:
        integer = get_int()
    except KeyboardInterrupt:
        print("\nProgram cancelled by user.", file=sys.stderr)
        return EXIT_ABORTED
    except EOFError:
        if sys.stdin.isatty():
            print("\nInput cancelled by the user.", file=sys.stderr)
        else:
            print(
                "\nError: Reached end of input without receiving a valid integer.",
                file=sys.stderr,
            )
        return EXIT_ABORTED

    if is_even(integer):
        print("even")
    else:
        print("odd")

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
