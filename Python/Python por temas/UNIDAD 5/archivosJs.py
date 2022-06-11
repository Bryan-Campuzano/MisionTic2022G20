import json
import pandas as pd
df1 = pd.read_json('data.json')
print(df1.to_string())

diccionario ={
    "nombre":"Juan",
    "edad": 25,
    "profesion": "contador",
    "hijos": ['Ana', 'Julián'],
    "mascotas": None,
    "divorciado": False    
}
archivo = json.dumps(diccionario, indent=4, ensure_ascii=False)
print(archivo)
print(type(archivo))

