n = int(input("Enter number of students: "))

scores = list(map(int, input("Enter scores: ").split()))

scores = list(set(scores))   # remove duplicates
scores.sort()

if len(scores) >= 2:
    print("Second highest:", scores[-2])
else:
    print("No second highest value")