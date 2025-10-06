def function(fileNAME):
    try:
        num = int(input("Enter number of elements in lists: "))
        list1 = []
        for i in range(num):
            list1.append(input("enter element for list 1: "))

        list2 = []
        for i in range(num):
            list2.append(input("enter element for list 2: "))

        if(len(list1) != len(list2)):
            print("error, both list are of different size")
            return
        
        dict = {}
        for i in range(num):
            dict[list1[i]] = list2[i]

        with open(fileNAME, 'w') as file:
            for key, value in dict.items():
                file.write(f'{key} = {value} \n')

    except FileNotFoundError:
        print("file not found")

    except PermissionError:
        print("permission denied")

    except Exception as e:
        print("Error unexpected: ", e)

fileNAME = "dictionary.txt"
function(fileNAME)