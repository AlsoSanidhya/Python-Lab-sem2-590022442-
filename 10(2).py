#(3×3) NumPy array operations
import numpy as np

arr = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])

print("Array:\n", arr)

rsum = np.sum(arr, axis=1)
print("Row wise sum:", rsum)

csum = np.sum(arr, axis=0)
print("Col wise sum:", csum)

secondmax = np.sort(arr.flatten())[-2]
print("Second max element:", secondmax)