def fileReading(fileName):
    try:
        with open(fileName, 'r') as file:
            text = file.read()

            characterCount = len(text)
            words = text.split()
            wordsCount = len(words)
            

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("permission denied")

    except Exception as e:
        print("unexpected error ", e)

    else:
        print("Character counts: ", characterCount)
        print("Word Count: ", wordsCount)

fileName = input("enter file name: ")
fileReading(fileName)