def division():
    try: 
        a = int(input("Enter a number: ").strip())
        b = int(input("Enter second number: ").strip())
        result = a / b
        
    except ZeroDivisionError:
        print("Error, divide by zero results in infinite")

    except ValueError:
        print("Error, enter integers only")

    except Exception as e:
        print("Unexpected error ", e)

    else:
        print("result: ", result)

division()
