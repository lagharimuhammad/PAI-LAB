listA = [[0 for _ in range(3)] for _ in range(3)] #pre initialisation of list
for x in range(0,3):
    for y in range(0,3):
        listA[x][y] = int(input("Enter your value in first matrix: "))

listB = [[0 for _ in range(3)]for _ in range(3)]
for m in range(0,3):
    for n in range(0,3):
        listB[m][n] = int(input("Enter your value in second matrix: "))

listSum = [[0 for _ in range(3)]for _ in range(3)]
for a in range(0,3):
    for b in range(0,3):
        listSum[a][b] = listA[a][b] + listB[a][b]
print("Sum: ")
print(listSum)

listMulti = [[0 for _ in range(3)] for _ in range(3)]

for p in range(0,3):
    for q in range(0,3):
        for r in range(0,3):
            listMulti[p][q] += listA[p][r] * listB[r][q]

print("Muultiplication: ")
print(listMulti)