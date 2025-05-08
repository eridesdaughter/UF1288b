import os

import requests

r = requests.get('http://192.168.1.10:5000')


datos = r.text

print(datos)
