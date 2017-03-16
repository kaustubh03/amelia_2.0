import gnp
import codecs
import json
from pprint import pprint

a = gnp.get_google_news(gnp.EDITION_ENGLISH_INDIA)

j = json.dumps(a, indent=4, ensure_ascii=False )
f = codecs.open( 'news.json', 'w', encoding='utf-8')
f.write(j.decode('utf-8'))
f.close()

with open('news.json') as data_file:
    data = json.load(data_file)

pprint(data)