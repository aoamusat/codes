import pandas as pd


d = {
    'nomes': {'Graco': 'Babeuf', 'Glauber': 'Mateus', 'Grácio': 'Zaqueu'},
    'idades': [29, 27, 25],
    'profissao': ['Desenvolvedor', 'Advogado', 'Músico']
}
#df = pd.DataFrame(d)
serie = pd.Series(d)
print(serie[0])
print(serie['nomes']['Graco'])

#print(df)
"""for row in df:
    print(row, end=': ')
    for val in df[row]:
        print(val, end=' ')
    print()"""
