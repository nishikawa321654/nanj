import datetime
import urllib.request

ym = datetime.datetime.now().strftime('%Y%m')

url_1 = 'https://280blocker.net/files/280blocker_adblock_' + ym + '.txt'
url_2 = 'https://280blocker.net/files/280blocker_domain_ag_' + ym + '.txt'

# urllib.request.urlretrieve(url_1, 'LICENSE1.txt')
# urllib.request.urlretrieve(url_2, 'LICENSE2.txt')

headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}

request = urllib.request.Request(url_1, headers=headers) 
html = urllib.request.urlopen(request).read()
with open('LICENSE1.txt', mode="wb") as f:
   f.write(html)

request = urllib.request.Request(url_2, headers=headers) 
html = urllib.request.urlopen(request).read()
with open('LICENSE2.txt', mode="wb") as f:
   f.write(html)
