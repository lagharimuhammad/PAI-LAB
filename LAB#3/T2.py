def stringLastLetter(sentence):
    vowels = "aeiou"

    sentence = sentence.lower()
    character = sentence[-1]

    if(character.isalpha()):
        if character in vowels:
            print("Last charcter is vowel")
        else:
            print("Last charcter is consonant")

    else:
        print("Not a alphabet")

sentence = input("Enter sentence/Word: ")
stringLastLetter(sentence)