def get_int() -> int:
  while True:
    try:
      input_str = input("Enter an integer: ")
      return int(input_str)
    except ValueError:
      print(f"'{input_str}' is not valid integer")


def even_or_odd(number: int) -> str:
  if number % 2 == 0:
    return "even"
  return "odd"


def main():
    num = get_int()
    print(even_or_odd(num))


if __name__ == "__main__": main()