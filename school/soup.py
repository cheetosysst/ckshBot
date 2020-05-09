from bs4 import BeautifulSoup

class soup():
    def soup(self):
        self.html = ""
        self.soup = ""
    
    def parseRaw(self, html):
        self.html = html

    def getRaw(self):
        return self.html

    def processRaw(self):
        self.soup = BeautifulSoup(self.html, 'html.parser')

    def getPrettify(self):
        return self.soup.prettify()

    def getData(self):
        # resAll = self.soup.find_all("td")
        resDate = self.soup.findAll("td", {"class": "nt_date"})
        resSubject = self.soup.findAll("a", {"title": "查看公告內容"})
        resCategory = self.soup.findAll("td", {"class": "nt_category"})
        resUnit = self.soup.findAll("td", {"class": "nt_unit"})
        resView = self.soup.findAll("td", {"class": "nt_view"})
        resUrl = []
        for a in self.soup.findAll("a", {"title": "查看公告內容"}):
            resUrl.append(a["href"])
        data = []
        for i in range(15):
            data.append({
                "date": resDate[i].text,
                "category": resCategory[i].text,
                "unit": resUnit[i].text,
                "view": resView[i].text,
                "urgent": True if "急件" in resSubject[i].text else False,
                "important": True if "重要" in resSubject[i].text else False,
                "subject": resSubject[i].text,
                "url": resUrl[i]
                })
        return data


