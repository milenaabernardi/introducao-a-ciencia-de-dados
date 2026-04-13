import pandas as pd
import io

conteudo = """id_transacao,valor,moeda
1,"1.250,00",BRL
2,"3.500,50",BRL
3,999.99,USD"""

df = pd.read_csv(io.StringIO(conteudo), thousands='.', decimal=',')

print(df)
print("\nTipo da coluna valor:", df['valor'].dtype)