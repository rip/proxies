from json import loads
from base64 import b64decode
from requests_html import AsyncHTMLSession

a = AsyncHTMLSession() 

url = 'https://www.proxyfish.com/proxylist/server_processing.php?type='

async def 一(): return await a.get(url + 'HTTP')  # ~1.5k

async def 二(): return await a.get(url + 'HTTPS')  # ~500

results = a.run(一, 二)

for result in results:

	req = result.json()['data']  # request json data

	data = b64decode(req)  # decode data

	d = loads(data)  # load data

	for p in d:  # only proxy ip and port
		print(p[1] + ':' + p[2])