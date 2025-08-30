password = input("Enter your password: ")
lengthCondition = False
alphabetCondition = False
numberCondition = False
charCondition= False
length = len(password)
for alphabet in password:
    if(length>=8):
        lengthCondition=True
    if(alphabet>='a' and alphabet<='z'):
        alphabetCondition=True
    if(alphabet>='0' and alphabet<='9'):
        numberCondition=True
    if(alphabet=='@' or alphabet=='#' or alphabet=='$' or alphabet=='%'):
        charCondition=True

if(lengthCondition and alphabetCondition and numberCondition and charCondition):
    print("valid password")
else:
    print("Invalid Password")