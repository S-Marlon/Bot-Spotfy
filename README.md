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
Bot-Spotfy/
├── app/
│   ├── __init__.py         # Inicializa o app Flask
│   ├── routes.py           # Todas as rotas Flask
│   ├── logic/              # Funções de lógica separadas
│   │   ├── main.py         # Função principal que você quer rodar
│   │   ├── drive.py        # Lógica de upload e autenticação Google Drive
│   │   └── rss_generator.py# Geração do RSS Feed
│   ├── static/
│   │   └── ...             # Arquivos públicos (css, js, imagens)
│   └── templates/
│       └── index.html      # Página com botão para iniciar processo
├── audios/                 # Pasta onde os áudios serão armazenados
├── requirements.txt        # Dependências do projeto
├── run.py                  # Script principal que roda o app
└── README.md
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
