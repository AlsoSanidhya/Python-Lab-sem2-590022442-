#(3×3) NumPy array operations
import numpy as np

arr = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])

print("Array:\n", arr)

# Sum of rows
rsum = np.sum(arr, axis=1)
print("Row wise sum:", rsum)

# Sum of columns
csum = np.sum(arr, axis=0)
print("Column wise sum:", csum)

# 2nd maximum element
secondmax = np.sort(arr.flatten())[-2]
print("Second maximum element:", secondmax)