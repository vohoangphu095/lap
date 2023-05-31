# Password Generator Project
import random, string

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?"))
nr_symbols = int(input(f"How many symbols would you like?"))
nr_numbers = int(input(f"How many numbers would you like?"))

ran1 = [random.choice(letters) for x in range(nr_letters)]
ran3 = [random.choice(numbers) for y in range(nr_numbers)]
ran2 = [random.choice(symbols) for z in range(nr_symbols)]

passw = "".join(ran1 + ran2 + ran3)
print(passw)
listt = list(passw)
random.shuffle(listt)
print(''.join(listt))

# plan 2

character = string.ascii_letters + string.digits + string.punctuation
min_size = 8
max_size = 20
password = ''.join(random.choice(character) for xx in range(random.randint(min_size, max_size)))
print(password)