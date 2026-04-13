agenda = {
    "Ana": "99123-4567",
    "Bruno": "99888-1122",
    "Carla": "98765-4321"
}
nome_busca = "Ana"
print(f"Telefone de {nome_busca}: {agenda.get(nome_busca, 'Não encontrado')}")