from bs4 import BeautifulSoup as soup
import urllib.request
import urllib
import webbrowser
songn=input("Enter song's name       ")
url="https://www.youtube.com/results?search_query="+songn.replace(" ","+")
req = urllib.request.Request(
    url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
uopen = urllib.request.urlopen(req)
page=soup(uopen.read(),"html.parser")
url2="https://320youtube.com"+page.findAll("div",{"class":"yt-lockup-content"})[0].findAll("a")[0]["href"]
req = urllib.request.Request(
    url2,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
uopen2 = urllib.request.urlopen(req)
page2=soup(uopen2.read(),"html.parser")
finallink=page2.findAll("div",{"id":"download"})[0].findAll("a")[0]["href"]
webbrowser.open(finallink)
