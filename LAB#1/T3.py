num = int(input("Enter number: "))

n1 = num // 1000
n2 = (num//100) % 10
n3 = (num // 10) % 10
n4 = num % 10

n1, n4 = n4, n1
n2, n3 = n3, n2

n1 = (n1 + 7) % 10
n2 = (n2 + 7) % 10
n3 = (n3 + 7) % 10
n4 = (n4 + 7) % 10

x = n1*1000 + n2*100 + n3*10 + n4
print(x)