def isPalindrome(word):
    word = word.lower()
    left = 0
    right = len(word) - 1;

    while left < right:
        if(word[left] != word[right]):
            return False
        
        right -=1
        left += 1

    return True

word = input ("Enter the word: ")
if(isPalindrome(word)):
    print("Palindrome")
else:
    print("Not Palindrome")