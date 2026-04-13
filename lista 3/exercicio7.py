import pandas as pd
import io

conteudo = """amostra,ph,temperatura,concentracao
A01,6.8,25.2,0.15
A02,7.1,26.5,0.18
A03,6.5,24.9,0.14
A04,6.9,25.8,0.16"""

df = pd.read_csv(io.StringIO(conteudo))

print("Primeiras linhas:\n", df.head(2))
print("\nEstatísticas:\n", df.describe())