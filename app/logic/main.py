import os
from app.logic.gerar_rss import gerar_rss
from app.logic.verificar_novos_videos import verificar_novo_video
from app.logic.baixar_audio import baixar_audio
from app.logic.drive import upload_arquivo
from app.logic.drive import listar_arquivos

# def limpar_nome_arquivo(titulo, video_id):
#     nome = titulo.lower()
#     nome = nome.replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
#     return f"{nome}_{video_id}.mp3"

def main():
    # Garante que a pasta "audio" exista
    os.makedirs("audio", exist_ok=True)

    # Verifica o vídeo mais recente
    video = verificar_novo_video()
    print(f"viedeo é {video}")
    if not video:
        print("Nenhum novo vídeo encontrado.")
        return

    video_id = video[0]
    titulo = video[1]

    print(f"Novo vídeo encontrado: {titulo} (ID: {video_id})")

    # Baixa o áudio
    #nome_arquivo = limpar_nome_arquivo(titulo, video_id) 
    caminho_audio = baixar_audio(video_id, titulo) # titulo por nome do arquivo  

    print(f"Áudio baixado em: {caminho_audio}")

    nomeDrive = f"{video_id}_{titulo}"

    # Envia para o Google Drive
    drive_id = upload_arquivo(caminho_audio, nomeDrive)
    print(f"Arquivo enviado para o Google Drive. ID: {drive_id}")

    # arquivos = listar_arquivos()
    # if arquivos:
    #     gerar_rss(arquivos)
    # else:
    #     print("Nenhum arquivo de áudio encontrado na pasta.")

    arquivos = listar_arquivos()
    if not arquivos:
        print("Nenhum arquivo de áudio encontrado na pasta.")
        return
    
    gerar_rss(arquivos) 
    
    return  #gerar_rss(arquivos) 


def opa():
    arquivos = listar_arquivos()
    # if not arquivos:
    #     print("Nenhum arquivo de áudio encontrado na pasta.")
    #     return
    
    return arquivos #gerar_rss(arquivos) 


if __name__ == "__main__":
    main()
