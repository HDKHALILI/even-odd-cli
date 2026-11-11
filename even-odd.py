def get_int() -> int:
    """Prompt the user until a valid integer is entered, then return it."""
    while True:
        try:
            input_str = input("Enter an integer: ")
            return int(input_str)
        except ValueError:
            print(f"Invalid integer. Please enter a valid integer.")

def is_even(integer: int) -> bool:
    """Return True if the given integer is even, False otherwise."""
    return integer % 2 == 0

def main() -> None:
    integer = get_int()
    if is_even(integer):
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    main()