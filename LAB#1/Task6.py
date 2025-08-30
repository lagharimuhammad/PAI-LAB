countries = {'Indonesia': 279134000,'Pakistan': 241493000,'Russia': 146447000,'United States': 341814000,'China': 1412000000,'India': 1430000000,'Mexico': 129732000,'Bangladesh': 174701000,'Nigeria': 229152000,'Brazil': 204653000
}

c = list(countries.items())
swap = 0

for x in range(len(c)):
    for y in range(len(c) - 1):
        if(c[y][1] < c[y+1][1]):
            swap = c[y]
            c[y] = c[y+1]
            c[y+1] = swap

countries.clear()
for keys, values in c:
    countries[keys] = values

count = 0
for keys, values in countries.items():
    if(count < 3):
        print(f" {count}. {keys} ~ {values}")
        count+=1
    else:
        break