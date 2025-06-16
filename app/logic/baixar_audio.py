import subprocess
import os
from slugify import slugify  # pip install python-slugify (opcional, mas recomendado)


def baixar_audio(video_id, titulo):
    url = f'https://www.youtube.com/watch?v={video_id}'
    
    # Nome seguro e com pasta
    nome_seguro = f"{video_id}_{titulo.lower().replace(' ', '-').replace(':', '').replace(',', '').replace('.', '')}.mp3"
    caminho_final = os.path.join('audio', nome_seguro)

    comando = [
        'yt-dlp',
        '-x',                       # Extrai o áudio
        '--audio-format', 'mp3',   # Converte para mp3
        '--audio-quality', '0',    # Qualidade máxima
        '--ffmpeg-location', 'C:\\Users\\marlo\\Downloads\\ffmpeg-7.1.1-essentials_build\\ffmpeg-7.1.1-essentials_build\\bin',
        '-o', caminho_final,
        url
    ]

    print("Baixando áudio...")
    result = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        print("Erro ao baixar:", result.stderr.decode())
        raise Exception("Erro no download")

    # Espera até o arquivo estar disponível no disco
    tentativas = 0
    while not os.path.exists(caminho_final) and tentativas < 10:
        import time
        time.sleep(1)
        tentativas += 1

    if not os.path.exists(caminho_final):
        raise FileNotFoundError("O arquivo não foi encontrado após o download.")

    return caminho_final
