import pandas as pd

data = pd.read_csv('Negara.csv')
print(f"Data Negara:\n{data}")

data_mean = data.groupby('Benua')[['Luas', 'Populasi']].mean()
data_std = data.groupby('Benua')[['Luas', 'Populasi']].std()

print(f"\nBerikut data Mean: \n{data_mean}")
print(f"\nBerikut data Standard Deviation : \n{data_std}")






