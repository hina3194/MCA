####.....PALINDROME.....####

word=input("Please enter a word:")
reversed_word=word[::-1]
if word == reversed_word:
    print("Hooray! You entered a palindrome")
else:
    print(" You did not enter a palindrome number")
