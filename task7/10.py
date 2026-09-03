# Take a sentence containing double spaces and unwanted spaces at the beginning or end. Clean the sentence.
sentence=input("Enter sentence: ")
sentence=sentence.strip()
sentence=sentence.replace("  "," ")
print(sentence)
