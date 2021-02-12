import urllib
import requests

# HTTP eskaerak 4 atal ditu: metodoa, uria, goiburuak eta edukia
#Las comillas simples y las dobles son lo mismo en python

metodoa = 'POST'

uria = "https://www.ehu.eus//bilatu/buscar/sbilatu.php?lang=es1"


goiburuak = {'Host': 'www.ehu.eus',
             'Content-Type': 'application/x-www-form-urlencoded'}

edukia = {'abi_ize': 'casquero','ize':'oscar'}


edukia_encoded = urllib.parse.urlencode(edukia)
goiburuak['Content-Length'] = str(len(edukia_encoded))

erantzuna = requests.request(metodoa, uria, data=edukia, headers=goiburuak, allow_redirects=False)
kodea = erantzuna.status_code
deskribapena = erantzuna.reason
print(str(kodea) + " " + deskribapena)

edukia = erantzuna.content
print(edukia)
