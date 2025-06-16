import requests
import json
import os

YOUTUBE_API_KEY = 'AIzaSyBqL0SoxhnZlTACHxe8OHGDPOujock2G30'
CHANNEL_ID = 'UCLTWPE7XrHEe8m_xAmNbQ-Q'
ULTIMO_VIDEO_ARQUIVO = 'ultimo_video.json'

print(YOUTUBE_API_KEY, CHANNEL_ID, ULTIMO_VIDEO_ARQUIVO)

def obter_ultimo_video():
    url = f'https://www.googleapis.com/youtube/v3/search?key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&order=date&part=snippet&type=video&maxResults=1'
    resposta = requests.get(url)
    dados = resposta.json()
    if 'items' in dados and len(dados['items']) > 0:
        video_id = dados['items'][0]['id']['videoId']
        titulo = dados['items'][0]['snippet']['title']
        return video_id, titulo
    return None, None

def verificar_novo_video():
    video_id, titulo = obter_ultimo_video()
    if not video_id:
        return f"video já publicado"

    if os.path.exists(ULTIMO_VIDEO_ARQUIVO):
        with open(ULTIMO_VIDEO_ARQUIVO, 'r') as f:
            ultimo = json.load(f)
            print("ultimo")
            print(video_id)
            print(ultimo)
            print(ultimo['video_id'])
        if ultimo['video_id'] == video_id:
            print("video já publicado agora puco")
            return None, None

    with open(ULTIMO_VIDEO_ARQUIVO, 'w') as f:
        json.dump({'video_id': video_id}, f)
    print(video_id, titulo)
    print("video novo vou postar")
    return video_id, titulo