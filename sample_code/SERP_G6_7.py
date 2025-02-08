import requests
from bs4 import BeautifulSoup
from urlextract import URLExtract
import re

#webscrape and data sorting class
class WebScrape:
    #initializer(SE data is obtained using webscrape)
    def __init__(self, keyword):
       self.searchlink = "https://www.google.com/search?q=" + keyword
       self.rawWebData = requests.get(self.searchlink)
       self.webData = str(self.rawWebData.text)
       self.numberOfCharacter = len(self.webData)
       self.currentCharIndex = 0
       self.my_data = []
       self.webContent = ""
       self.title = []
       self.summary = ""
       
    #This method sorts the data from html using string manipulations
    def getRelevantLinks(self):
       #extractor = URLExtract()
       #self.my_data = extractor.find_urls(self.webData)
       self.my_data = re.findall(r'(https?://[^\s]+)', self.webData)
       #print(self.my_data[0:20])
       print("\nProcessing...\n")
      # print(self.webData)
    def getSummary(self):
        for x in range(0,20):
           self.webContent = requests.get(self.my_data[x])
           soup = BeautifulSoup(self.webContent.text, 'html.parser')
           for title in soup.find_all('title'):
               #print(title.get_text())
               self.title.append(str(title.get_text()) + " ")
               if x == 2:
                   print("Still processing... Please wait \n")
               elif x == 15:
                   print("Almost done...\n")
           twiCheck = str(self.my_data[x])
           if "https://twitter.com" in twiCheck:
                self.title.append("Twitter Link")
        #print(self.title)      
        print("SERP in order of relevance: \n")
        for x in range(1,20):
            print(self.title[x])
            print(self.my_data[x])
            print("")
                   
#The main method  
def main():
    print(" Run a SERP program \n")
    keywordEntry = input("Enter keyword: ")
    #create a search object
    keywordWebscrape = WebScrape(keywordEntry)
    keywordWebscrape.getRelevantLinks()
    keywordWebscrape.getSummary()
main()
