import requests
from bs4 import BeautifulSoup
from pprint import pprint

#webscrape and data sorting class
class WebScrape:
    #initializer(SE data is obtained using webscrape)
    def __init__(self, keyword):
       self.searchlink = "https://www.google.com/search?q=" + keyword
       self.rawWebData = requests.get(self.searchlink)
       self.webData = str(self.rawWebData.text)
       self.numberOfCharacter = len(self.webData)
       self.currentCharIndex = 0
       
    #This method sorts the data from html using string manipulations
    def sortWebData(self):
       #print(self.webData)
       while self.currentCharIndex < self.numberOfCharacter-1000:
           tempLinkHolder = ""
           currentPosition = 0
           for x in range(0,21):
               tempLinkHolder = tempLinkHolder + self.webData[self.currentCharIndex+x] 
               currentPosition = self.currentCharIndex+x
           if tempLinkHolder == '<a href="/url?q=https:':
               while self.webData[currentPosition] != ">":
                   tempLinkHolder = tempLinkHolder + self.webData[currentPosition] 
               pprint(tempLinkHolder)
           self.currentCharIndex += 1
                   
#The main method  
def main():
    keywordEntry = input("Enter keyword: ")
    keywordWebscrape = WebScrape(keywordEntry)
    print("SERP in order of relevace: \n")
    keywordWebscrape.sortWebData()
main()
