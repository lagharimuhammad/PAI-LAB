def fixFile(filefile):
    try:
        with open(filefile, 'r') as file:
            text = file.read()

        if 'Thas' in text:
            text = text.replace('Thas', 'This', 1)

        with open(filefile, 'w') as file:
            file.write(text)

        return text

    except FileNotFoundError:
        print('error, file not found.')
    except PermissionError:
        print("error, permission denied")
    except Exception as e:
        print("unexpected error: ", e)

result = fixFile('filefile.txt')
print(result)