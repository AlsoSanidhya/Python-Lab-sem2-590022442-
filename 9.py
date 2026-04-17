n = int(input("Enter number of inputs: "))

count = [0, 0, 0, 0]   # index represents 0,1,2,3

print("Enter values (0 to 3):")

for i in range(n):
    value = int(input())

    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid value")

for i in range(4):
    print(i, "occurred", count[i], "times")