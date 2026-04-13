from collections import Counter

frase = "python é legal python é versátil legal ser python"
palavras = frase.split()
contagem = Counter(palavras)
print(f"3 mais frequentes: {contagem.most_common(3)}")