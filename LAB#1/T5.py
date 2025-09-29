import random

name = input("Enter your name: ")
year = input("Enter your birth year: ")

firstThree = ""
for ch in name[:3]:
    if random.choice([True, False]):
        firstThree += ch.upper()
    else:
        firstThree += ch.lower()

lastTwo = year[-2:]

symbols = "@#%&*"
index = ord(name[0]) % 5
special = symbols[index]

password = firstThree + lastTwo + special
print("Generated password:", password)