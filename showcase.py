"""
Part 1
"""

# Komentář

"""
Docstring
"""

str = "   Ahoj Světe!   "

print(str.lower())  #   ahoj světe!
print(str.upper())  #   AHOJ SVĚTE!
print(str.strip())  #Ahoj světe!
print(str.strip().split(' '))  # ['Ahoj', 'Světe!']
print(str.replace("Ahoj", "Čus"))  #   Čus světe!

list = ['b', 'i', 'c', 'e', 'd', 'f', 'h', 'g', 'a', 'j']
print(list)  # ['b', 'i', 'c', 'e', 'd', 'f', 'h', 'g', 'a', 'j']
print(list[0])  # b
print(list[3:9:2])  # ['e', 'f', 'g']
print(list.pop())  # j
list.sort()
print(list)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
list.append('z')
print(list)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'z']
list.insert(4, 'x')
print(list)  # ['a', 'b', 'c', 'd', 'x', 'e', 'f', 'g', 'h', 'i', 'z']
list.remove('d')
print(list)  # ['a', 'b', 'c', 'x', 'e', 'f', 'g', 'h', 'i', 'z']
print(len(list))  # 10

tuple = ('x', 'y', 'z')
print(tuple)  # ('x', 'y', 'z')
# tuple[0] = 'z'    # Crash


x = 1
if x > 5:
    pass
elif x == 5:
    pass
else:
    pass

for i in range(5):
    print(i)  # 0 1 2 3 4

while x < 5:
    print(x)  # 1 2 3 4
    x += 1


def fce(a, b):
    return a + b


print(fce(1, 2))  # 3

# print(a)      # Crash

from typing import List as Ls


l: Ls = [1, 2, 3]

"""
Part 2
"""

try:
    raise ValueError("Chyba!")
except Exception as e:
    print(e)
else:
    print("To je divné.")
finally:
    print("Já se vypíši vždy.")

with open("LICENSE", "r") as f:
    print(f.read())
