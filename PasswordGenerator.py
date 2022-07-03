#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bienvenido a el Generador de Contraseñas PyPassword!")
nr_letters= int(input("¿Cuántas letras le gustaría que tenga su contraseña?\n")) 
nr_symbols = int(input("¿Cuántos simbolos le gustaría que tenga?\n"))
nr_numbers = int(input(f"¿Cuántos números le gustaría que tenga?\n"))

password_len=nr_letters+nr_numbers+nr_symbols
password=""

for letter_number in range(1,nr_letters+1):
  random_number = random.randint(0,len(letters)-1)
  letter = letters[random_number] #letter = random.choice(letters)
  password = password + letter

for symbol_number in range(1,nr_symbols+1):
  random_number = random.randint(0,len(symbols)-1)
  symbol = symbols[random_number]
  password = password + symbol

for number_of_numbers in range(1,nr_numbers+1):
  random_number = random.randint(0,len(numbers)-1)
  number = numbers[random_number]
  password = password + number

random_password=random.sample(password,password_len) #crea una lista aletoria a partir de un string

contraseña=""
for position in random_password:
  contraseña+=position

print(f"Tu contraseña puede ser: {contraseña}")