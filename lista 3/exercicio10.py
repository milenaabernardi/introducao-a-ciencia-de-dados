import pandas as pd
import io

vendas_rep = "produto,quantidade,preco\n" + "Monitor,10,799.90\n"*100
arquivo = io.StringIO(vendas_rep)

for i, bloco in enumerate(pd.read_csv(arquivo, chunksize=20)):
    print(f"Lendo bloco {i+1} - Quantidade de linhas: {len(bloco)}")
    print(bloco.head(3))