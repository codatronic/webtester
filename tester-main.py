import requests
site = 'http://' + input('(put quote marks) Website URL, without http: ')
r = requests.get(site)
stat = r.status_code
if stat == 200:
 print('Code 200. OK')
else:
 print('Unknown code:')
 print(stat)