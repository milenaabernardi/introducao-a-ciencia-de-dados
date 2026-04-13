import pandas as pd
import io

conteudo = """item;valor_unitario;peso_kg
Maçã;2,99;0,150
Laranja;1,50;0,200
Banana;4,00;0,120"""

df = pd.read_csv(io.StringIO(conteudo), sep=';', decimal=',')

print(df.dtypes)
print("\n", df)