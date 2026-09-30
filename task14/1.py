# Write a python program to input a student's marks in n consecutive tests and store them in a list.
# Find the longest consecutive sequence in which each mark is strictly greater than the previous mark.
# Display the sequence, its length, and its starting and ending test numbers as a tuple.
# If multiple sequences have the same maximum length, display the first one.
# Marks: [55,60,68,62,65,70,78,74]
# Longest improving sequence: [62, 65, 70, 78]
# Numbers of tests: 4
# Test range: (4, 7)
'''Condition:
Accept at least one test.
Equal marks break the improving sequence.
Test numbers begin at 1
Do not sort the list because the original test order matters.'''

marks = list(map(int, input("Enter marks of students: ").split()))
n = len(marks)
current = [marks[0]]
longest = [marks[0]]
for i in range(1, n):
    if marks[i] > marks[i-1]:
        current.append(marks[i])
    else:
        current = [marks[i]]
    if len(longest) < len(current):
        longest = current.copy()
start = marks.index(longest[0])+1
end = marks.index(longest[-1])+1
print("Longest improving sequence: ", longest)
print("Number of tests: ", len(longest))
print("Test range: ", (start, end))
