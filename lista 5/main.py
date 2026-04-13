import pandas as pd
import numpy as np

def exercicio_agrupamento():
    print("\nAgrupamento e Agregação (Total por Vendedor)")
    dados = {
        'vendedor': ['Milena', 'Leonardo', 'Milena', 'Laura', 'Leonardo'],
        'valor_venda': [1200, 1500, 800, 2000, 300]
    }
    df = pd.DataFrame(dados)
    
    resultado = df.groupby('vendedor')['valor_venda'].sum().reset_index()
    print(resultado)

def exercicio_datas():
    print("\nManipulação de Datas (Extração de Mês)")
    dados = {'data_pedido': ['2026-01-15', '2026-02-20', '2026-04-12']}
    df = pd.DataFrame(dados)
    
    df['data_pedido'] = pd.to_datetime(df['data_pedido'])
    
    df['mes'] = df['data_pedido'].dt.month
    print(df)

def exercicio_limpeza():
    print("\nLimpeza de Dados (Duplicatas e Nulos)")
    dados = {
        'nome': ['Laura', 'Milena', 'Laura', 'Leonardo', 'Julia'],
        'idade': [25, 30, 25, np.nan, 40]
    }
    df = pd.DataFrame(dados)
    
    df = df.drop_duplicates()
    
    media_idade = df['idade'].mean()
    df['idade'] = df['idade'].fillna(media_idade)
    
    print(df)

if __name__ == "__main__":
    exercicio_agrupamento()
    exercicio_datas()
    exercicio_limpeza()