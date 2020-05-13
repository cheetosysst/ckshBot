# This file is under construction

# Library
from school.school import school
from school.soup import soup
import json
from os import path
import time

# Objects and setting
sc = school()
sc.setOffice(53)
so = soup()

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
				print("**new post**", str(i))
		json.dump(data, f, indent = 4)
		print("[] Check done, time is", time.asctime( time.localtime(time.time()) ))
	else:
		print("[] else")
		f = open('data.json', 'w')
		json.dump(so.getData(), f, indent = 4)

while (True):
	check()
	time.sleep(60)
	print("[] sleep ")