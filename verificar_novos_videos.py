import requests
import json
import os

YOUTUBE_API_KEY = 'SUA_API_KEY'
CHANNEL_ID = 'ID_DO_CANAL'
ULTIMO_VIDEO_ARQUIVO = 'ultimo_video.json'

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
        return None

    if os.path.exists(ULTIMO_VIDEO_ARQUIVO):
        with open(ULTIMO_VIDEO_ARQUIVO, 'r') as f:
            ultimo = json.load(f)
        if ultimo['video_id'] == video_id:
            return None

    with open(ULTIMO_VIDEO_ARQUIVO, 'w') as f:
        json.dump({'video_id': video_id}, f)

    return video_id, titulo