# Import package 
import requests
from bs4 import BeautifulSoup
import jsons
from datetime import datetime

page = requests.get("https://www.republika.co.id")

obj = BeautifulSoup(page.text, "html.parser")
now = datetime.now()
currenttime = now.strftime("%d %B %Y, %H:%M:%S")
data=[]
f = open("data.json","w")
for content in obj.find_all("div", class_="contenkanal").find("div", class_="wrap-latest").findall("div", "conten1"):
    data.append({"judul":content.find("div", class_="teaser_conten1center").find("h2").find("a").text,
                 "kategori":content.find("div", class_="teaser_conten1_center").find("h1").find("p").find("a").text,
                 "waktupublish":content.find("div", class_="teaser_conten1center").find("div", class_="date").text,
                 "waktu_scraping":current_time})
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()