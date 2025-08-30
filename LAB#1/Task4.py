arr = (13,5, -2,-10,12,7,-9,-6, 11,-17)
min = 2**31 - 1
numOne = None
numTwo = None

for x in range(len(arr)):
    for y in range(len(arr) - 1):
        if(arr[x] == arr[y]):
            continue
        if( abs(min) > abs(arr[x]+arr[y])):
            min = arr[x] + arr[y]
            numOne = arr[x]
            numTwo = arr[y]

print(f"first number: {numOne}\nsecond number {numTwo}")
print("Their sum value is: ", min)