from requests import Session, get

def getSession(login, password):
	global ctoken
	s = Session()
	try:
		ctoken = s.get('https://iphub.info/login').text.split('token" content="')[1].split('"')[0]
		r = s.post('https://iphub.info/login', data={'_token': ctoken, 'email': login, 'password': password, 'remember': 'on'})
		r.text.split('Logout')[1]
		return s
	except:
		raise Exception('Login failed!')

def getKeys(session):
	keys = []
	r = session.get('https://iphub.info/account')
	dem = r.text.split('/apiKey/')
	for line in dem:
		try:
			if dem.index(line) != 0:
				keys.append(line.split('"')[0])
		except:
			raise Exception('Keys not found!')
	return keys

def getKey(session, id):
	try:
		return 'MT' + session.get(f'https://iphub.info/apiKey/{id}').text.split('"MT')[1].split('"')[0]
	except:
		return None

def regenerateKey(session, id):
	try:
		session.post(f'https://iphub.info/apiKey/regenerateApiKey/{id}', data={'_token': ctoken})
		return getKey(session, id)
	except:
		return None

def generateKey(session):
	try:
		session.post('https://iphub.info/apiKey/newFree', data={'_token': ctoken})
		return getKey(session, getKeys(session)[0])
	except:
		return None

def checkIP(session, ip):
	r = get(url=f'http://v2.api.iphub.info/ip/{ip}', headers={'X-Key': apiKey}).json()
	if 'error' in r:
		if '86400' in r['error']:
			setKey(regenerateKey(session, getKeys(session)[0]))
			return checkIP(ip)
		else:
			return r
	else:
		return r

def setKey(key):
	global apiKey
	apiKey = key