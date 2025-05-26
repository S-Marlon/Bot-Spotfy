# 🎙️ YouTube-to-Spotify Podcast Bot

Este projeto é um bot em Python que monitora automaticamente novos vídeos em um canal do YouTube, extrai o áudio e publica como episódios de podcast via um feed RSS compatível com Spotify for Podcasters (Anchor).

---

## 🔧 Funcionalidades

✅ Detecta novos vídeos no YouTube  
✅ Baixa o áudio usando `yt-dlp`  
✅ Converte e nomeia o áudio como episódio  
✅ Gera um feed RSS com os episódios  
✅ Integra com o Spotify via URL do feed

---

## 📦 Requisitos

- Python 3.8+
- Conta no [Spotify for Podcasters](https://podcasters.spotify.com/)
- Chave da YouTube Data API v3
- Hospedagem com suporte a arquivos estáticos (para `rss.xml` e arquivos de áudio)
- Conta no Drive para usar a Api

---

## 🛠️ Instalação

1. Clone o repositório:

```bash
git clone https://github.com/S-Marlon/youtube-podcast-bot.git
cd youtube-podcast-bot


pip install -r requirements.txt
```

requirements.txt
    | yt-dlp
    | feedgen
    | requests
    
```bash

YOUTUBE_API_KEY=YOUR_YOUTUBE_API_KEY
CHANNEL_ID=UCxxxxxxxxxxxxxxxx

python main.py
```
```bash
youtube-podcast-bot/
├── main.py                  # Script principal que une todos os passos
├── verificar_novos_videos.py
├── baixar_audio.py
├── gerar_rss.py
├── auth_podbean
├── ultimo_video.json        # Armazena ID do último vídeo processado
├── audios/                  # Pasta onde ficam os MP3 extraídos
├── rss.xml                  # Feed gerado automaticamente
├── requirements.txt
└── .env
```
---

🚀 Publicação no Spotify
Após rodar o script, envie os arquivos .mp3 e rss.xml para sua hospedagem.

Pegue a URL do feed, por exemplo:
https://seudominio.com/rss.xml

Vá em https://podcasters.spotify.com/

Adicione um novo podcast via RSS Feed

O Spotify fará a leitura e publicará os episódios automaticamente.

---

💡 Sugestões de melhorias
Suporte a múltiplos canais

Geração automática de capas

Integração com plataformas como Amazon S3 ou Firebase Storage

Envio automatizado por FTP ou API para hospedagem

---

⚠️ Aviso Legal
Este projeto deve ser usado apenas com permissão do criador do conteúdo. Baixar e republicar conteúdo sem autorização pode violar direitos autorais.

---

📩 Contato
Desenvolvido por Marlon Santos
📧 Marlon.vcsantos@icloud.com
