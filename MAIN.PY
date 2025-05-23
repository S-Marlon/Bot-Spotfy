import os
import datetime
from verificar_novos_videos import verificar_novo_video
from baixar_audio import baixar_audio
from gerar_rss import gerar_feed

# Dados fixos
TITULO_PODCAST = 'Podcast Automático do YouTube'
DESCRICAO_PODCAST = 'Episódios convertidos automaticamente do canal do YouTube'
AUTOR = 'Seu Nome'
URL_BASE_AUDIO = 'https://seudominio.com/audios/'  # altere conforme sua hospedagem
PASTA_AUDIOS = 'audios'

# Armazena os episódios já gerados
EPISODIOS_REGISTRADOS = 'episodios.txt'

# Lê os episódios anteriores
def carregar_episodios_salvos():
    if not os.path.exists(EPISODIOS_REGISTRADOS):
        return []
    with open(EPISODIOS_REGISTRADOS, 'r') as f:
        return [linha.strip() for linha in f.readlines()]

# Salva novo episódio
def salvar_episodio(video_id):
    with open(EPISODIOS_REGISTRADOS, 'a') as f:
        f.write(video_id + '\n')

# Main
def main():
    novo = verificar_novo_video()
    if not novo:
        print("Nenhum novo vídeo encontrado.")
        return

    video_id, titulo = novo
    print(f"Novo vídeo detectado: {titulo}")

    audio_file = baixar_audio(video_id, titulo)

    url_audio = URL_BASE_AUDIO + audio_file
    data = datetime.datetime.utcnow()

    episodio = {
        'id': video_id,
        'titulo': titulo,
        'descricao': f'Conversão automática do vídeo {titulo} do YouTube.',
        'url_audio': url_audio,
        'data': data
    }

    episodios_salvos = carregar_episodios_salvos()
    episodios_lista = []

    if os.path.exists('rss.xml'):
        # Opcional: você pode carregar o XML e reconstruir os episódios antigos, se quiser manter histórico
        # Para simplificação aqui, vamos criar um novo com o episódio atual + os IDs salvos.
        pass

    episodios_lista.append(episodio)
    salvar_episodio(video_id)

    gerar_feed(TITULO_PODCAST, DESCRICAO_PODCAST, AUTOR, episodios_lista)
    print("RSS atualizado com novo episódio!")

if __name__ == "__main__":
    main()
