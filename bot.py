from school.school import school
from school.soup import soup
import json
from os import path
import time

sc.setOffice(53)

while (True):
	check()
	sleep(3600)

def check():
	raw = sc.getData()
	so.parseRaw(raw)
	so.processRaw()
	if path.exists("data.json") and path.getsize("data.json") > 0:
		f = open('data.json', 'r+')
		data = json.loads(f.read())
		for i in so.getData():
			if i not in data:
				data.append(i)
		json.dump(data, f, indent = 4)
	else:
		f = open('data.json', 'w')
		json.dump(so.getData(), f, indent = 4)
