import os
from verificar_novos_videos import verificar_novo_video
from baixar_audio import baixar_audio
from drive import upload_arquivo
from drive import listar_arquivos
from datetime import datetime
from drive import PASTA_ID
import html


def limpar_nome_arquivo(titulo, video_id):
    nome = titulo.lower()
    nome = nome.replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')
    return f"{nome}_{video_id}.mp3"

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

    
def opa():
    arquivos = listar_arquivos()
    if arquivos:
        gerar_rss(arquivos)
    else:
        print("Nenhum arquivo de áudio encontrado na pasta.")

def gerar_rss(itens):
    rss_items = ""
    for item in itens:
        titulo = escape_xml(item['name'])
        link = escapar_url(f"https://drive.google.com/uc?export=download&id={item['id']}")
        data = datetime.strptime(item['createdTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        pub_date = data.strftime("%a, %d %b %Y %H:%M:%S GMT")

        rss_items += f"""
        <item>
            <title>{titulo}</title>
            <link>{link}</link>
            <guid>{link}</guid>
            <pubDate>{pub_date}</pubDate>
            <enclosure url="{link}" type="audio/mpeg"/>
        </item>
        """

    rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
        <title>Podcast do Bot</title>
        <link>https://drive.google.com/drive/folders/{PASTA_ID}</link>
        <description>Podcast gerado automaticamente</description>
        <language>pt-br</language>
        {rss_items}
    </channel>
    </rss>"""
    
    with open("rss.xml", "w", encoding="utf-8") as f:
        f.write(rss_feed)
    print("✅ RSS gerado em 'rss.xml'")

def escape_xml(texto):
    return html.escape(texto)

def escapar_url(url):
    return url.replace("&", "&amp;")

if __name__ == "__main__":
    opa()
