Records = (("Ali", 87), ("Ahmed", 79), ("Zohaib", 93),("Amjad", 82), ("Riaz", 77))
swap = ( )
temp = list(Records)
for x in range(len(temp)):
    for y in range(len(temp) - 1):
        if(temp[y][1] < temp[y+1][1]):
            swap = temp[y]
            temp[y] = temp[y+1]
            temp[y+1] = swap

Records = tuple(temp)

print(Records)