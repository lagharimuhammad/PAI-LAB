list1 = []
for x in range(0,5):
    country = input("Enter name of country: ")
    list1.append(country)


list2 = []
for x in range(0,5):
    capital = input("Enter their capital cities: ")
    list2.append(capital)

dictionary = {}
for i in range(len(list1)):
    dictionary[list1[i]] = list2[i]

with open("myfile.txt", "w") as file:
    file.write(str(dictionary))