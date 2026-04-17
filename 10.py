n = int(input("Enter number of values: "))

values = []

for i in range(n):
    num = float(input("Enter value: "))
    values.append(num)

t = tuple(values)

average = sum(t) / len(t)

print("Tuple:", t)
print("Average:", average)