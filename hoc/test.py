import pandas as pd

data = {
    'state': ['ohio', 'ohio2', 'ohi03', 'opp'],
    'year': [2000, 2000, 2002, 2003],
    'pop': [2, 1.1, 3, 4]
}
new1 = pd.DataFrame(data)
print(new1)
