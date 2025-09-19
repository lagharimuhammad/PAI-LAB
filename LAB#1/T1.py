var = int(input("Enter a number: "))

varComplex = complex(var)
varFloat = float(var)
varString = str(var)

print("In Complex: ", varComplex)
print("In Float: ",varFloat)
print("In String: ", varString)

div = (varFloat // 2) * 2 == varFloat
print("Divisible by 2: ", div)