import pandas as pd
df1 = pd.DataFrame(
    {
        'Nombre': ['Laura','Laura','Laura','Laura','Juan','Juan','Juan','Juan'],
        'Fecha':['03/05/2022','04/05/2022','05/05/2022','05/05/2022','03/05/2022','04/05/2022','05/05/2022','05/05/2022'],
        'Cantidad': [8,2,5,6,8,7,1,2]
    }
)
pt = pd.pivot_table(df1, index='Nombre', columns = 'Fecha', aggfunc=['sum', 'count'])
print(pt)