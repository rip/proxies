'''fplproxies.py

python3 fplproxies.py > proxies.txt

scrapes 600 http(s) proxies to ip:port

https://free-proxy-list.net 300
https://www.us-proxy.org 200
https://www.sslproxies.org 100
'''

from requests_html import HTMLSession

def z(fpl):

	session = HTMLSession()  # session appears to be currently required for a single get request with this library?

	cells = session.get(fpl).html.find('td')  # table cells

	p = ''  # string as data stream for proxies

	for cell in cells:
		c = cell.text 
		if not c.lower().islower():  # lowercase all letters and then check if islower to determine if the cell contains letters (only ip and port cells will remain)
			if '.' in c: c = '\n' + c + ':'  # ip will have "." then add newline in front of ip to separate proxies \nip:port\nip:port 
			p += c  # string together 

	print(p)
z('https://free-proxy-list.net')
z('https://www.us-proxy.org')
z('https://www.sslproxies.org')
#z('https://www.socks-proxy.net')  # socks
