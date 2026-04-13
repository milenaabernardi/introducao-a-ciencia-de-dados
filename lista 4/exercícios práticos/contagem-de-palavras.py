import re
from collections import Counter

def contar_palavras(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read().lower()
            
        # remove pontuação e mantém apenas palavras
        palavras = re.findall(r'\b\w+\b', texto)
        contagem = Counter(palavras)
        
        print("As 10 palavras mais comuns")
        for palavra, freq in contagem.most_common(10):
            print(f"{palavra}: {freq}")
            
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")

contar_palavras('texto.txt')