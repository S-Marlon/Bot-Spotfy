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
