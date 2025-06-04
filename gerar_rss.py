from xml.etree.ElementTree import Element, SubElement, ElementTree
import datetime

def criar_rss(episodios, titulo_podcast, link_site, descricao, email_autor, caminho_saida='rss.xml'):
    rss = Element('rss', version='2.0')
    channel = SubElement(rss, 'channel')

    SubElement(channel, 'title').text = titulo_podcast
    SubElement(channel, 'link').text = link_site
    SubElement(channel, 'description').text = descricao
    SubElement(channel, 'language').text = 'pt-br'
    SubElement(channel, 'managingEditor').text = email_autor

    for episodio in episodios:
        item = SubElement(channel, 'item')
        SubElement(item, 'title').text = episodio['titulo']
        SubElement(item, 'description').text = episodio['descricao']
        SubElement(item, 'pubDate').text = episodio['data'].strftime('%a, %d %b %Y %H:%M:%S +0000')
        SubElement(item, 'enclosure', url=episodio['url'], type='audio/mpeg')
        SubElement(item, 'guid').text = episodio['url']

    tree = ElementTree(rss)
    tree.write(caminho_saida, encoding='utf-8', xml_declaration=True)
    print(f"RSS gerado com sucesso em {caminho_saida}")