def find_max_min(numbers):
    maximum = numbers[0]
    minimum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num

    return maximum, minimum


nums = [10, 4, 7, 25, 2, 18]

max_val, min_val = find_max_min(nums)

print("Maximum:", max_val)
print("Minimum:", min_val)