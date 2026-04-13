import pandas as pd
import io

sensor_rep = "sensor_id,temperatura\n" + "S1,23.5\nS2,NA\nS3,24.1\nS4,-\n"*13
arquivo = io.StringIO(sensor_rep)

for i, bloco in enumerate(pd.read_csv(arquivo, chunksize=10, na_values=['NA', '-'])):
    media_temp = bloco['temperatura'].mean()
    ausentes = bloco['temperatura'].isna().sum()
    print(f"Bloco {i+1}: Média Temp = {media_temp:.2f} | Valores Ausentes = {ausentes}")