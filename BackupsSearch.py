import httplib
import sys
import os

def cut_url(url):
	return url[:url.index('/')], url[url.index('/'):]

BACKUPS_EXT = [
	'.bak',
	'.old',
	'~',
]

BACKUPS_FOLDERS = [
	'/backups',
	'/old',
	'/save',
]

url = sys.argv[-1]
host, path = cut_url(url)

for ext in BACKUPS_EXT:

	back_path = path + ext

	http = httplib.HTTPConnection(host, 80)
	http.request('GET', back_path)

	if http.getresponse().status == 200: print('Backup file finded : {bf}'.format(bf=host+back_path))

	http.close()

for fld in BACKUPS_FOLDERS:

	back_path = os.path.dirname(path)

	http = httplib.HTTPConnection(host, 80)
	http.request('GET', back_path)

	if http.getresponse().status == 200: print('Backup folder finded : {bf}'.format(bf=host+back_path))

	http.close()
