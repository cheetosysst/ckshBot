# School bot
# Run with Python3, require re and requests.

from school.school import school
from school.soup import soup
# import json
from os import path

sc = school()
so = soup()
print("[] School Bot test")

sc.setOffice(53)
raw = sc.getData()

so.parseRaw(raw)
so.processRaw()

if path.exists("data.bt") and path.getsize("data.bt") > 0:
	f = open('data.bt', 'w+')
	subjectList = []
	for line in f.readlines():
		rawList = line.split(";")
		subjectList.append(str(rawList[6]))
		print(f)
	for article in so.getData():
		if article["subject"] not in subjectList:
			for content in article:
				f.write(str(article[content])+";")
			f.write("\n")
		else:
			print("[] NO!!! You can't just say no new article and output nothing noooo!!! haha error goes brrrrrrr")



else:
	f = open('data.bt', 'w')
	for article in so.getData():
		for content in article:
			f.write(str(article[content])+";")
		f.write("\n")
	f.close()
