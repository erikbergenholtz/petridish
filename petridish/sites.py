import json
import requests
from bs4 import BeautifulSoup

class Site:
    def __init__(self, **kwargs):
        pass
    def crawl(self, n):
        pass
    def download(self, **kwargs):
        pass

class Malshare(Site):
    def __init__(self, **kwargs):
        print(kwargs['apikey'])
        self.api_key = kwargs['apikey']
        self.output = kwargs['output']
        self.base_url = 'https://malshare.com'

    def crawl(self, n):
        daily = '{}/api.php?api_key={}&action=getlist'
        r = requests.get(daily.format(self.base_url, self.api_key))
        r.raise_for_status()
        hashes = json.loads(r.text)
        found = 0
        for h in hashes:
            found += 1 if self.download(md5=h['md5']) else 0
            if found == n:
                break

    def download(self, **kwargs):
        try:
            md5 = kwargs['md5']
            url = '{}/api.php?api_key={}&action=details&hash={}'
            r = requests.get(url.format(self.base_url, self.api_key, md5))
            r.raise_for_status()
            details = json.loads(r.text)
            if details['F_TYPE'] != 'PE32':
                return False
            print("[MALSHARE] Downloading `{}`".format(md5))
            url = '{}/api.php?api_key={}&action=getfile&hash={}'
            r = requests.get(url.format(self.base_url, self.api_key, md5),
                             stream=True)
            r.raise_for_status()
            with open('{}/{}.exe'.format(self.output, md5), 'wb') as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)
            return True
        except KeyError:
            print('[MALSHARE] No hash provided')
            return False

class VXVault(Site):
    def __init__(self, **kwargs):
        self.base_url = 'http://vxvault.net'

    def crawl(self, n):
        found = 0
        start = 0
        while found < n:
            url = '{}/ViriList.php?s={}&m={}'.format(self.base_url, start, n)
            print(url)
            r = requests.get(url.format(start=0, amount=n))
            r.raise_for_status()
            soup = BeautifulSoup(r.text, 'html.parser')
            for tr in soup.find_all('tr'):
                try:
                    tds = tr.find_all('td')
                    a = tds[1].find_all('a')
                    if '.exe' not in a[1].string:
                        continue
                    md5 = tds[2].a.string
                    url = '{}/{}'.format(self.base_url, a[0]['href'])
                    self.download(url=url, md5=md5)
                    found += 1
                except IndexError:
                    pass
                if found >= n:
                    break
            start += n

    def download(self, **kwargs):
        print('To Be Implemented. Sorry m8.')
