# Password generator project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '&', '*']

print("Welcome to the Python Password Generator!")
# nr_letters = int(input("How many letters would you like to use in your password? : "))
# nr_numbers = int(input("How many numbers would you like to use in your password? : "))
# nr_symbols = int(input("How many symbols would you like to use in your password? : "))

nr_letters = random.randint(1,10)
nr_numbers = random.randint(1,10)
nr_symbols = random.randint(1,10)

# easy level 
# password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
    
# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
    
# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
    
# print(f"Password:  {password}")


# hard level 
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))
    
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
    
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
print(f"Password:  {password.capitalize()}")
