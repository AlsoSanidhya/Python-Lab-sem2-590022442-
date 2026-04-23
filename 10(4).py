#Pandas program (powers element-wise)
import pandas as pd

data = {
    'X': [78, 85, 96, 80, 86],
    'Y': [84, 94, 89, 83, 86],
    'Z': [86, 97, 96, 72, 83]
}

df = pd.DataFrame(data)

# Element-wise power (X^Y)
df['X_power_Y'] = df['X'] ** df['Y']

print(df[['X', 'Y', 'Z']])