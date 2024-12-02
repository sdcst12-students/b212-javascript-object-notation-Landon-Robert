#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

a = open('task01a.txt', 'r').read().replace("[", "").replace("]", "").replace(",", "").split(' ')
A = []
for i in a:
    A.append(int(i))
    A.sort()
b = open('task01b.txt', 'r').read().replace("[", "").replace("]", "").replace(",", "").split(' ')
B = []
for i in b:
    B.append(int(i))
    B.sort()
c = open('task01c.txt', 'r').read().replace("[", "").replace("]", "").replace(",", "").split(' ')
C = []
for i in c:
    C.append(int(i))
    C.sort()
print(f"\ntask01a: {A[-1]}\ntask01b: {B[-1]}\ntask01c: {C[-1]}")
