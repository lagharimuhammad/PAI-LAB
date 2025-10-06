def isQuestion():
    try:
        sentence = input("Enter the sentence: ")
        if sentence.strip().endswith("?"):
            with open("question.txt", 'a') as file:
                file.write(sentence)
                file.write("\n")
        else:
            print("sentence is not a question")

    except PermissionError:
        print("Permsission denied")

    except FileNotFoundError:
        print("file not found")

    except Exception as e:
        print("unexpected error ", e)

isQuestion()
