"Write a program that inputs a text file. The program should print all of the unique words in the file in alphabetical order."
f = open("MyFile1.txt", "r")

words = f.read().split()
unique_words = sorted(set(words))

print("Unique words in alphabetical order:")
for word in unique_words:
    print(word, end = ", ")

f.close()