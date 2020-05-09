import requests as req

class school():
    def school(self):

        self.project    = "ckshBot"
        self.version    = "0.0.1"
        self.devState   = "alpha"
        self.officeCode = 0

    def setOffice(self, officeCode):
        self.officeCode = officeCode

    def getData(self):
        r = req.get("https://www2.cksh.tp.edu.tw/category/news/?officeID="+str(self.officeCode))
        if r.status_code == 200:
            data = r.text
        else:
            data = 1
        return data

