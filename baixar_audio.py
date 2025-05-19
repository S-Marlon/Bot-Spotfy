import subprocess
import os

def baixar_audio(video_id, titulo):
    url = f'https://www.youtube.com/watch?v={video_id}'
    nome_arquivo = f'audio_{video_id}.mp3'
    comando = [
        'yt-dlp',
        '-x', '--audio-format', 'mp3',
        '-o', nome_arquivo,
        url
    ]
    subprocess.run(comando)
    return nome_arquivo
