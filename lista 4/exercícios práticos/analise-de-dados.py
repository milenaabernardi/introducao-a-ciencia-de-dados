import csv

def analisar_csv(caminho_csv, categoria_alvo):
    precos = []
    
    try:
        with open(caminho_csv, mode='r', encoding='utf-8') as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                if linha['categoria'].lower() == categoria_alvo.lower():
                    precos.append(float(linha['preco']))
        
        if precos:
            media = sum(precos) / len(precos)
            print(f"Preço médio de {categoria_alvo}: R$ {media:.2f}")
        else:
            print(f"Nenhum produto encontrado na categoria {categoria_alvo}.")
            
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")

analisar_csv('produtos.csv', 'Eletrônicos')