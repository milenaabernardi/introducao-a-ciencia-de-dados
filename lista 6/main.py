import firebase_admin
from firebase_admin import credentials, auth, firestore, storage, messaging, exceptions
import os

NOME_ARQUIVO_JSON = 'serviceAccountKey.json' 
BUCKET_STORAGE = 'seu-projeto-id.firebasestorage.app' 

def executar_lista_6():
    # 1. CONFIGURAÇÃO E INICIALIZAÇÃO
    print("--- Exercício 1: Inicialização ---")
    try:
        if not firebase_admin._apps:
            cred = credentials.Certificate(NOME_ARQUIVO_JSON)
            app = firebase_admin.initialize_app(cred, {
                'storageBucket': BUCKET_STORAGE
            })
            print(f"✅ Firebase inicializado: {app.name}")
        
        db = firestore.client()
    except Exception as e:
        print(f"❌ Erro crítico na inicialização: {e}")
        return

    # 2. GERENCIAMENTO DE USUÁRIOS (AUTH)
    print("\n--- Exercício 2: Auth ---")
    try:
        email_teste = "aluno.unicentro@teste.com"
        user = auth.create_user(email=email_teste, password="senhaForte123")
        print(f"✅ Usuário criado: {user.uid}")
    except exceptions.AlreadyExistsError:
        print(f"ℹ️ O usuário {email_teste} já existe no sistema.")
    except Exception as e:
        print(f"❌ Erro no Auth: {e}")

    # 3. OPERAÇÕES DE FIRESTORE (UPDATE)
    print("\n--- Exercício 3: Update Firestore ---")
    try:
        id_prod = "prod_101"
        db.collection('produtos_mysql').document(id_prod).set({
            'nome': 'Teclado Mecânico',
            'preco': 150.0
        })
        
        doc_ref = db.collection('produtos_mysql').document(id_prod)
        doc_ref.update({'preco': 199.90})
        print(f"✅ Preço do produto {id_prod} atualizado.")
    except Exception as e:
        print(f"❌ Erro no Update: {e}")

    # 4. CONSULTAS AVANÇADAS NO FIRESTORE
    print("\n--- Exercício 4: Consultas ---")
    try:
        print("Buscando produtos com preço > R$ 15,00:")
        docs = db.collection('produtos_mysql').where('preco', '>', 15.0).stream()
        for doc in docs:
            p = doc.to_dict()
            print(f"- {p.get('nome')}: R$ {p.get('preco')}")
    except Exception as e:
        print(f"❌ Erro na consulta: {e}")

    # 5. UPLOAD PARA CLOUD STORAGE
    print("\n--- Exercício 5: Storage ---")
    print("ℹ️ Exercício pulado: Necessário upgrade de plano no console do Firebase.")
    # try:
    #     bucket = storage.bucket()
    #     blob = bucket.blob("exercicios/meu_arquivo.txt")
    #     blob.upload_from_string("Olá, Firebase Storage!", content_type='text/plain')
    #     print("✅ Arquivo enviado para a nuvem com sucesso.")
    # except Exception as e:
    #     print(f"❌ Erro no Storage: {e}")

    # 6. ENVIO DE NOTIFICAÇÃO (MESSAGING)
    print("\n--- Exercício 6: Messaging ---")
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title='Notificação Acadêmica',
                body='Lista 6 finalizada!',
            ),
            topic='avisos',
        )
        response = messaging.send(message)
        print(f"✅ Notificação enviada. ID: {response}")
    except Exception as e:
        print(f"❌ Erro no Messaging: {e}")

if __name__ == "__main__":
    executar_lista_6()