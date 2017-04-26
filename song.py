from bs4 import BeautifulSoup as soup
import urllib.request
import urllib
import os
songn=input("Enter song's name       ")
url="http://www.instamp3.net/download/"+songn.replace(" ","-")+".html"
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
g = urllib.request.urlopen(req)
pageh=g.read()
pagehtml=soup(pageh,"html.parser")
tabl=pagehtml.findAll("ul",{"class":"list-group"})
table=tabl[0]
metatags=table.findAll("div",{"class":"meta"})
firstmeta=metatags[0]
atag=firstmeta.findAll("a",{"class":"downnow"})
ataga=atag[0]
str=ataga["onclick"].split("'")
url=str[1]
req = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )
f = urllib.request.urlopen(req)
downpage=f.read()
pagen=soup(downpage,"html.parser")
downbutt=pagen.findAll("a",{"class":"btn btn-danger"})
cmd='cd C:\Program Files (x86)\Internet Download Manager\ && IDMan.exe /n /d '+'"'+downbutt[0]["href"]+'"'

os.system(cmd)