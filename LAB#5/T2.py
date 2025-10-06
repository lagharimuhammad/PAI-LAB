def replacementFile(fileName, searchWord, replaceWord):
    try:
        with open(fileName, 'r') as file:
            text = file.read()

        if searchWord in text:
            text = text.replace(searchWord, replaceWord)
            with open(fileName, 'w') as file:
                file.write(text)

    except FileNotFoundError:
        print("file not found")

    except PermissionError:
        print("permission denied")

    except Exception as e:
        print("Error unexpected: ", e)

fileName = input("Enter file name: ")
searchWord = input("Enter the word you want to replace: ")
replaceWord = input("Enter the word you want to replace with: ")

replacementFile(fileName, searchWord, replaceWord)