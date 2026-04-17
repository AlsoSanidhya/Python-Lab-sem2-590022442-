s1 = {"Red", "Yellow", "Orange", "Blue"}
s2 = {"Violet", "Blue", "Purple"}

a = s1 | s2      # Union
b = s1 & s2      # Intersection
c = s1 - s2      # Difference

print("Union =", a)
print("Intersection =", b)
print("Difference =", c)