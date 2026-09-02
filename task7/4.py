# Write a python program to take a word and print it in reverse order using slicing. Also check whether it is same forward or backward.
word=input("Enter a word: ")
reverse=word[::-1]
print(reverse)
print(word==reverse)