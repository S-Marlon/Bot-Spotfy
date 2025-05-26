from feedgen.feed import FeedGenerator
import os
import datetime


def gerar_feed(titulo_podcast, descricao_podcast, autor, lista_episodios):
    fg = FeedGenerator()
    fg.load_extension('podcast')

    fg.title(titulo_podcast)
    fg.description(descricao_podcast)
    fg.link(href='https://seudominio.com/podcast', rel='alternate')
    fg.language('pt-br')
    fg.podcast.itunes_author(autor)
    fg.podcast.itunes_category('Technology', 'Podcasting')

    for ep in lista_episodios:
        fe = fg.add_entry()
        fe.id(ep['id'])
        fe.title(ep['titulo'])
        fe.description(ep['descricao'])
        fe.enclosure(ep['url_audio'], 0, 'audio/mpeg')
        fe.pubDate(ep['data'])

    fg.rss_file('rss.xml')


def gerar_item(titulo, descricao, url_audio, guid):
    pubDate = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    return f"""
    <item>
      <title>{titulo}</title>
      <description>{descricao}</description>
      <pubDate>{pubDate}</pubDate>
      <enclosure url="{url_audio}" length="12345678" type="audio/mpeg" />
      <guid>{guid}</guid>
    </item>
    """

# Adicione esse item no arquivo XML base e envie para a hospedagem

