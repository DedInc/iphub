from requests import Session, get

class IPHub:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.session = self._get_session()
        self.ctoken = None
        self.api_key = self.get_key(self.get_keys()[0])

    def _get_session(self):
        s = Session()
        try:
            self.ctoken = s.get('https://iphub.info/login').text.split('token" content="')[1].split('"')[0]
            r = s.post('https://iphub.info/login', data={'_token': self.ctoken, 'email': self.login, 'password': self.password, 'remember': 'on'})
            r.text.split('Logout')[1]
            return s
        except:
            raise Exception('Login failed!')

    def get_keys(self):
        keys = []
        r = self.session.get('https://iphub.info/account')
        self.ctoken = r.text.split('token" content="')[1].split('"')[0]
        dem = r.text.split('/apiKey/')
        for line in dem:
            try:
                if dem.index(line) != 0:
                    keys.append(line.split('"')[0])                
            except:
                pass
        if len(keys) == 0:
            self.generate_key()
            return self.get_keys()
        return keys 

    def get_key(self, id):
        return self.session.get(f'https://iphub.info/apiKey/{id}').text.split('readonly value="')[1].split('"')[0]

    def regenerate_key(self, id):
        r = self.session.post(f'https://iphub.info/apiKey/regenerateApiKey/{id}', data={'_token': self.ctoken})            
        self.ctoken = r.text.split('token" content="')[1].split('"')[0]
        return self.get_key(id)

    def generate_key(self):
        r = self.session.post('https://iphub.info/apiKey/newFree', data={'_token': self.ctoken})
        self.ctoken = r.text.split('token" content="')[1].split('"')[0]
        return self.get_key(self.get_keys()[0])

    def check_ip(self, ip):
        r = get(url=f'http://v2.api.iphub.info/ip/{ip}', headers={'X-Key': self.api_key}).json()
        if 'error' in r:
            if '86400' in r['error']:
                self.set_key(self.regenerate_key(self.get_keys()[0]))
                return self.check_ip(ip)
            else:
                return r
        else:
            return r

    def set_key(self, key):
        self.api_key = key