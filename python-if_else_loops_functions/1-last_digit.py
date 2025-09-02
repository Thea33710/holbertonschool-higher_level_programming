#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Récupérer la valeur absolue du dernier chiffre de number
last_digit = abs(number) % 10

# On vérifie la valeur du dernier chiffre et on affiche le message adapté
if last_digit == 0:
    # Si le dernier chiffre est 0
    print(f"Last digit of {number} is {last_digit} and is 0")
elif last_digit > 5:
    # Si le dernier chiffre est supérieur à 5
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    # Si le dernier chiffre est inférieur à 6 et différent de 0
    print(
        f"Last digit of {number} is {last_digit} and is less than 6 and not 0"
        )
