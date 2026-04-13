import requests

def buscar_repositorios(topico):
    url = "https://api.github.com/search/repositories"
    params = {
        'q': topico,
        'sort': 'stars',
        'order': 'desc'
    }
    
    try:
        resposta = requests.get(url, params=params)
        resposta.raise_for_status()
        dados = resposta.json()
        
        print(f"5 repositórios sobre {topico}")
        for repo in dados['items'][:5]:
            print(f"Nome: {repo['name']}")
            print(f"URL: {repo['html_url']}")
            print("-" * 20)
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")

buscar_repositorios("data science")