import pandas as pd
import io

conteudo = """produto;quantidade;preco_unitario
Monitor;10;799.90
Teclado;25;120.50
Mouse;40;50.00
Webcam;15;250.00"""

df = pd.read_csv(io.StringIO(conteudo), sep=';')

print(df)