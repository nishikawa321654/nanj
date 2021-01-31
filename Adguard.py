import datetime
import urllib.request

ym = datetime.datetime.now().strftime('%Y%m')

url_1 = 'https://280blocker.net/files/280blocker_adblock_' + ym + '.txt'
url_2 = 'https://280blocker.net/files/280blocker_domain_ag_' + ym + '.txt'

urllib.request.urlretrieve(url_1, 'LICENSE1.txt')
urllib.request.urlretrieve(url_2, 'LICENSE2.txt')

