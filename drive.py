from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# ID da pasta 'bot-spotfy' no Google Drive
PASTA_ID = '1HyUXJMzvlziH8ylb57Fta2zE8BHeDHD3'

# Escopos de permissão (acesso apenas a arquivos criados pelo app)
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def autenticar_drive():
    creds = None

    # Usa token salvo anteriormente
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # Se não for válido, inicia nova autenticação
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva o novo token
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)


def upload_arquivo(caminho_local, nome_no_drive):
    if not os.path.exists(caminho_local):
        raise FileNotFoundError(f"❌ Arquivo não encontrado: {caminho_local}")

    service = autenticar_drive()

    file_metadata = {
        'name': nome_no_drive,
        'parents': [PASTA_ID]  # envia para a pasta correta
    }

    media = MediaFileUpload(caminho_local, mimetype='audio/mpeg')

    file = service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"✅ Arquivo enviado para a pasta 'bot-spotfy'. ID: {file.get('id')}")
    return file.get('id')


# def listar_audios_da_pasta():
#     creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     service = autenticar_drive()

#     query = f"'{PASTA_ID}' in parents and mimeType='audio/mpeg'"
#     resultados = service.files().list(q=query, fields="files(id, name, createdTime)").execute()
#     arquivos = resultados.get('files', [])

#     episodios = []
#     for arquivo in arquivos:
#         episodios.append({
#             'titulo': os.path.splitext(arquivo['name'])[0],
#             'descricao': f"Episódio gerado automaticamente: {arquivo['name']}",
#             'data': arquivo['createdTime'],
#             'url': f"https://drive.google.com/uc?export=download&id={arquivo['id']}"
#         })

       
#         return episodios


def listar_arquivos():
    
    service = autenticar_drive()

    results = service.files().list(
        q=f"'{PASTA_ID}' in parents and mimeType contains 'audio/' and trashed = false",
        fields="files(id, name, createdTime)",
        orderBy="createdTime desc"
    ).execute()
    return results.get('files', [])



