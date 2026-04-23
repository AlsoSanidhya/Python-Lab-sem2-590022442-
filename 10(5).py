#First 3 rows of DataFrame
import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily',
             'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 20, 14.5, np.nan, 8, 19, 15],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'yes',
                'yes', 'no', 'no', 'yes', 'yes']
}

labels = list('abcdefghij')

df = pd.DataFrame(exam_data, index=labels)

print("First 3 rows:\n")
print(df.head(3))