def get_int() -> int:
  user_input = input("Enter an integer: ")
  valid_input = False

  while not valid_input:
    try:
      user_input = int(user_input)
      valid_input = True
    except:
      print(f"'{user_input}' is not valid integer")
      user_input = input()

  return user_input

def even_or_odd(number: int) -> str:
  if number % 2 == 0:
    return "even"
  return "odd"

num = get_int()
print(even_or_odd(num))