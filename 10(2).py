#(3×3) NumPy array operations
import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print("Array:\n", arr)

# Sum of rows
row_sum = np.sum(arr, axis=1)
print("Row-wise sum:", row_sum)

# Sum of columns
col_sum = np.sum(arr, axis=0)
print("Column-wise sum:", col_sum)

# 2nd maximum element
second_max = np.sort(arr.flatten())[-2]
print("Second maximum element:", second_max)