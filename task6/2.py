'''Write a python program to fill the given letter tempelate with name and date'''
'''name=input("Enter name: ")
date=input("Enter date: ")
# print(f"Dear {name},\nYou are selected!\n{date}")
print(f"""Dear {name},
You are selected!
{date}""")'''
# or
letter = '''Dear <Name>,
You are selected!
<Date>'''
name = input("Enter name: ")
date = input("Enter date: ")
letter = letter.replace("<Name>", name)
letter = letter.replace("<Date>", date)
print(letter)
