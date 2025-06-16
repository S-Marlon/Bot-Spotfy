import html
from datetime import datetime
from drive import PASTA_ID

def escape_xml(texto):
    return html.escape(texto)

def escapar_url(url):
    return url.replace("&", "&amp;")

def gerar_rss(itens):
    rss_items = ""
    for item in itens:
        titulo = escape_xml(item['name'])
        caminho = f"http://localhost:5000/audios/{item['id']}.mp3"
        link = escapar_url(f"https://drive.google.com/uc?export=download&id={item['id']}")
        data = datetime.strptime(item['createdTime'], "%Y-%m-%dT%H:%M:%S.%fZ")
        pub_date = data.strftime("%a, %d %b %Y %H:%M:%S GMT")

        rss_items += f"""
        <item>
            <title>{titulo}</title>
            <link>{caminho}</link>
            <guid>{caminho}</guid>
            <pubDate>{pub_date}</pubDate>
            <enclosure url="{caminho}" type="audio/mpeg" length="1234567"/>
        </item>
        """

    rss_feed = f"""<?xml version="1.0" encoding="UTF-8" ?>
    <rss version="2.0">
    <channel>
        <title>Ancapsu hoje</title>
        <link>https://drive.google.com/drive/folders/{PASTA_ID}</link>
        <description>Podcast gerado automaticamente</description>
        <language>pt-br</language>
        {rss_items}
    </channel>
    </rss>"""
    
    with open("templates/rss.xml", "w", encoding="utf-8") as f:
        f.write(rss_feed)
    print("✅ RSS gerado em 'templates/rss.xml'")
    return "dados"

    # proxima ação, enviar o rss gerado para o app.py e fazer a leitura de acordo com ID no drive