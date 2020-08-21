import requests
import bs4
import lxml.etree 
import re

class s:
    def getc(self):
        URL = "https://www.worldometers.info/coronavirus/country/india/"
        requests.get(URL)
        web_page = bs4.BeautifulSoup(requests.get(URL, {}).text, "lxml")
        detail = [e.text.strip("\n ") for e in 
                        web_page.find_all(name="div", 
                        attrs={"class": re.compile("maincounter-number")})]
        detail.append([e.text.strip("\n ") for e in 
                        web_page.find_all(name="div", 
                        attrs={"class": re.compile("number-table-main")})])
        d = {
            'total' : detail[0],
            'deaths' : detail[1],
            'recovered' : detail[2],
            'cases':detail[3]
        }
        return d
    def news(self):
        URL = "https://indianexpress.com/about/coronavirus-outbreak/"
        requests.get(URL)
        web_page = bs4.BeautifulSoup(requests.get(URL, {}).text, "lxml")
        detail = [ e.text.strip("\n ") for e in  
                        web_page.find_all(name="div", 
                        attrs={"class": re.compile("details")})]
        return detail[0:8]


