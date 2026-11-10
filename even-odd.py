def get_int() -> int:
  while True:
    try:
      input_str = input("Enter an integer: ")
      return int(input_str)
    except ValueError:
      print(f"'{input_str}' is not valid integer")


def is_even(integer: int) -> bool:
  return integer % 2 == 0


def main() -> None:
    integer: int = get_int()
    if is_even(integer):
      print("even")
    else:
      print("odd")


if __name__ == "__main__": main()