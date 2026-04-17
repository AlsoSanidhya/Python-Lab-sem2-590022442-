n = int(input("Enter number of fruits: "))

s1 = set()
for i in range(n):
    s1.add(input("Fruits in s1: "))

s2 = set()
for i in range(n):
    s2.add(input("Fruits in s2: "))

both = s1 & s2          # common fruits
only_s1 = s1 - s2       # fruits only in s1
count = s1 | s2         # all fruits (union)

print("Fruits which are in both:", both)
print("Fruits which are in s1 only:", only_s1)
print("All Fruits:", count)