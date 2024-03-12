import string
import random

letters = list(string.ascii_letters)
symbols = list(string.punctuation)
numbers = list(range(10))

print("Welcome to PyPassword Generator...")
required_letters = int(input("How many letters would you like? "))
required_numbers = int(input("How many numbers would you like? "))
required_symbols = int(input("How many symbols would you like? "))

number_pass = random.sample(numbers,required_numbers)
letter_pass = random.sample(letters,required_letters)
symbol_pass = random.sample(symbols,required_symbols)

password_list = number_pass+letter_pass+symbol_pass
random.shuffle(password_list)
password = ''.join(map(str,password_list))
print(f"Your Random Password is: '{password}'")
