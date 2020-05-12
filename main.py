# School bot
# Run with Python3, require re and requests.

from school.school import school
from school.soup import soup
import json

sc = school()
so = soup()
print("[] School Bot test")

sc.setOffice(53)
raw = sc.getData()

so.parseRaw(raw)
so.processRaw()
#print(so.getData())
with open('data.json', 'w') as file:
	json.dump(so.getData(), file,indent=4)
    


