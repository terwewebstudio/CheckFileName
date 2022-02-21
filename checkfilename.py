# uploadfilename.py
# id 77

import os
import requests

path = os.getcwd()
print(path)
filelist = str(os.listdir(path))
print(filelist)

apiurl = '192.168.1.1'
data = {"source" : "เด็กชายลุงเริง", "data" : "มากั๊บ"}
r = requests.post(url=apiurl, data=data)
print(r.text)
print(r.status_code)
