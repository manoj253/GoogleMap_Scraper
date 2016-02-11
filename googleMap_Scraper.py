import urllib
import mechanize
from bs4 import BeautifulSoup
import re

class VCards():
    def __init__(self,phoneNumber,Name):
        self.name = Name
        self.phoneNumber = phoneNumber

vCardArray = []        

def getGoogleMapsLinks(searchTerm):
        searchTerm = searchTerm.replace(" ","+")
        url = "https://www.google.co.in/maps/search/"+searchTerm+"/@40.9581204,-73.8503535,9z/am=t"
        resultssArr = []
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.addheaders = [("User-Agent","Google Chrome")]

        htmltext = br.open(url,timeout=3.0).read()
        soup = BeautifulSoup(htmltext)
        vcards = soup.findAll('div',attrs="class":"text vcard indent block"))

        for vcard in vcards:
            soup2 = BeautifulSoup(vcard)
            phoneRes = soup.findAll('span',attrs=("class":"pp-headline-item-pp-headline-phone"))
            soupPhone = BeautifulSoup(str(phoneRes[0]))
            phoneRes = soupPhone.findAll('nobr')[0].text
            formattedPhone = "+1"+phoneRes.replace("(","").replace(")","").replace.(" ","").replace('-','')

            titleRes = soup2.findAll('span',attrs=("class":"pp-place-title"))

            vc1 = vCards(formattedPhone,titleRes[0].text)
            vCardsArray.append(vc1)
            
        for vc in vCardArray:
            print vc.name,vc.phoneNumber
    
    
    
getGoogleMapsLinks("Driveway paving")    
