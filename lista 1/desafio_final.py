import json
from datetime import datetime, timedelta

class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

    def to_dict(self):
        return self.__dict__

class Usuario:
    def __init__(self, nome, cpf, livros_emprestados=None):
        self.nome = nome
        self.cpf = cpf
        self.livros_emprestados = livros_emprestados if livros_emprestados else []

    def to_dict(self):
        return self.__dict__

class Biblioteca:
    def __init__(self, arquivo='biblioteca.json'):
        self.arquivo = arquivo
        self.lista_livros = []
        self.lista_usuarios = []
        self.carregar_dados()

    def carregar_dados(self):
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                content = json.load(f)
                self.lista_livros = [Livro(**l) for l in content.get("livros", [])]
                self.lista_usuarios = [Usuario(**u) for u in content.get("usuarios", [])]
        except (FileNotFoundError, json.JSONDecodeError):
            self.lista_livros = []
            self.lista_usuarios = []

    def salvar_dados(self):
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            data = {
                "livros": [l.to_dict() for l in self.lista_livros],
                "usuarios": [u.to_dict() for u in self.lista_usuarios]
            }
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cadastrar_livro(self, t, a, i):
        self.lista_livros.append(Livro(t, a, i))
        self.salvar_dados()
        print(f"\n✅ Livro '{t}' cadastrado no acervo!")

    def cadastrar_usuario(self, nome, cpf):
        if any(u.cpf == cpf for u in self.lista_usuarios):
            print("\n❌ ERRO: Este CPF já está cadastrado!")
            return
        self.lista_usuarios.append(Usuario(nome, cpf))
        self.salvar_dados()
        print(f"\n✅ Usuário '{nome}' cadastrado no sistema!")

    def emprestar(self, cpf, titulo_busca):
        usuario = next((u for u in self.lista_usuarios if u.cpf == cpf), None)
        if not usuario:
            print("\n❌ ERRO: Usuário não encontrado!")
            return

        livro = next((l for l in self.lista_livros if l.titulo.lower() == titulo_busca.lower()), None)
        
        if livro and livro.disponivel:
            livro.disponivel = False
            prazo = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")
            
            usuario.livros_emprestados.append({
                "titulo": livro.titulo,
                "devolucao": prazo
            })
            
            self.salvar_dados()
            print(f"\n📖 SUCESSO: '{livro.titulo}' associado a {usuario.nome}.")
            print(f"📅 Prazo de devolução: {prazo}")
        else:
            print("\n❌ ERRO: Livro não encontrado ou já está emprestado.")

    def listar_tudo(self):
        print("\n📚 ACERVO DE LIVROS")
        for l in self.lista_livros:
            status = "S" if l.disponivel else "N"
            print(f"[{status}] {l.titulo} ({l.autor})")

        print("\n👥 USUÁRIOS CADASTRADOS")
        for u in self.lista_usuarios:
            print(f"• {u.nome} (CPF: {u.cpf}) - Itens: {len(u.livros_emprestados)}")

def sistema():
    bib = Biblioteca()
    while True:
        print("\n📚 BIBLIOTECA VIRTUAL")
        print("1. Novo Livro")
        print("2. Novo Usuário")
        print("3. Associar")
        print("4. Listar Relatórios")
        print("5. Sair")
        
        op = input("Opção: ")

        if op == '1':
            bib.cadastrar_livro(input("Título: "), input("Autor: "), input("ISBN: "))
        elif op == '2':
            bib.cadastrar_usuario(input("Nome: "), input("CPF: "))
        elif op == '3':
            bib.emprestar(input("CPF do Usuário: "), input("Título do Livro: "))
        elif op == '4':
            bib.listar_tudo()
        elif op == '5':
            print("Encerrando sistema...")
            break

if __name__ == "__main__":
    sistema()