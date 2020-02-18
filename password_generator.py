import random

while True:
    try:
        """Taking input from user"""
        first_name = str(input("Enter first name:"))
        last_name = str(input("Enter last name:"))
        if len(first_name) == 0 or len(last_name) == 0:
            raise ValueError
    except ValueError:
        print("Invalid Input!")
        continue
    else:
        break

password_length = int(input("Enter password length:"))
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['+', '-', '*', '@', '$', '#']


def first_convert():
    return list(first_name)


def second_convert():
    return list(last_name)


a = first_convert()
b = second_convert()
Name = first_name + " " + last_name
j = 0
if password_length >=8:
    while j < len(Name):
        if len(last_name) == 1:
            combined = a + digits + symbols
            rand_first_name = random.choice(a)
            rand_digits = random.choice(digits)
            rand_symbols = random.choice(symbols)
            temp_pass = rand_first_name + rand_digits + rand_symbols
            for x in range(password_length - 3):
                temp_pass = temp_pass + random.choice(combined)
        else:
            combined = a + b + digits + symbols
            rand_first_name = random.choice(a)
            rand_last_name = random.choice(b)
            rand_digits = random.choice(digits)
            rand_symbols = random.choice(symbols)
            temp_pass = rand_first_name + rand_last_name + rand_digits + rand_symbols
            for x in range(password_length - 4):
                temp_pass = temp_pass + random.choice(combined)
        j += 1
        print(temp_pass)
else:
    print("Invalid Length")
