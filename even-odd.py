def get_int() -> int | None:
    """Prompt the user until a valid integer is entered, then return it or return None for EOF"""
    while True:
        try:
            input_str = input("Enter an integer: ")
            return int(input_str)
        except ValueError:
            print(f"Invalid integer. Please enter a valid integer.")
        except EOFError:
            return None

def is_even(integer: int) -> bool:
    """Return True if the given integer is even, False otherwise."""
    return integer % 2 == 0

def main() -> None:
    integer = get_int()
    
    if integer is None:
        print("\nProgram cancelled by user.")
        return
    
    if is_even(integer):
        print("even")
    else:
        print("odd")

if __name__ == "__main__":
    main()