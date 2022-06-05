import pandas as pd

diccionario = {
        'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}
df1 = pd.DataFrame(diccionario)

print(df1)
df1.to_csv('ejemploCsv.csv', sep='|', header=None)
df2 = pd.read_csv('Libro1.csv')
print(df2)
df3 = pd.read_csv('ejemploCsv.csv', sep=',')
print(df3)
