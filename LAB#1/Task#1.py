password = input("Enter a password: ")
count = len(password)
while True:
    length = len(password)
    for digits in password:
        digits = digits.lower()
        if(digits >= 'a' and digits <= 'z'):
            count -= 1
        if(digits == '@' or digits == '#' or digits == '$' or digits == '%'):
            count -= 1
        if(digits >= '0' and digits <= '9'):
            count -= 1
        if(length >= 8):
            count -= 1
    
    if(count <= 0):
        print("valid")
        break
        
    else:
        print("invalid")
        break