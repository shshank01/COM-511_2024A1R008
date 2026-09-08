# Write a python program to detect whether a comment is spam or not.
# A comment should be treated as spam if it contains any of these keywords: 
# "make a lot of money", "buy now", "subscribe this", "click this".

comment=input("Enter your comment: ")
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]
is_spam = False
for keyword in spam_keywords:
    if keyword in comment:
        is_spam = True
        break

if is_spam:
    print("This comment is spam.")
else:
    print("This comment is not spam.")
