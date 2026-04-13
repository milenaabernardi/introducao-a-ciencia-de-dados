import pandas as pd
import io

conteudo = "id,coluna_a,coluna_b,coluna_c,timestamp\n" + \
           "1,val1,10.5,True,2024-01-01 10:00:00\n"*10

df = pd.read_csv(io.StringIO(conteudo))

df.info()