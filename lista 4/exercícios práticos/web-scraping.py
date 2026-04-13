import requests
from bs4 import BeautifulSoup

def extrair_titulos(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resposta = requests.get(url, headers=headers)
        resposta.raise_for_status() 
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        titulos = soup.find_all('h2')
        
        if not titulos:
            print("Nenhum título H2 encontrado nesta página.")
            return

        print(f"Títulos encontrados em: {url}")
        for i, h2 in enumerate(titulos, 1):
            texto = h2.get_text(strip=True)
            print(f"{i}. {texto}")
            
    except Exception as e:
        print(f"Erro ao acessar a página: {e}")

url = "https://pt.wikipedia.org/wiki/Portal:Eventos_atuais" 
extrair_titulos(url)