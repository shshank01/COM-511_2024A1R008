# Write a python program to take a word and count the number of vowels a,e,i,o,u without use of conditional statements.
word=input("Enter a word: ")
a=word.count('a')
e=word.count('e')
i=word.count('i')
o=word.count('o')
u=word.count('u')
print("Number of vowels in the word are: ", a+e+i+o+u)