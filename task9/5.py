# Write a python program to detect whether a comment is spam or not.
# A comment should be treated as spam if it contains any of these keywords: 
# "make a lot of money", "buy now", "subscribe this", "click this".

comment=input("Enter your comment: ")
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
flag = False
for i in spam_keywords:
    if i in comment:
        flag = True
        break

if flag:
    print("This comment is spam.")
else:
    print("This comment is not spam.")
