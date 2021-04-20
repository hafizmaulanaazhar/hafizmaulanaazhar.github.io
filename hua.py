# Import package 
import requests
from bs4 import BeautifulSoup
import jsons
from datetime import datetime
from datetime import date

page = requests.get("https://www.republika.co.id")

obj = BeautifulSoup(page.text, "html.parser")
now = datetime.now()
current_time = now.strftime("%d %B %Y, %H:%M:%S")
data=[]
f = open("data.json","w")
for content in obj.find("div", class_="conten_kanal").find("div", class_="wrap-latest").find_all("div", "conten1"):
    data.append({"judul":content.find("div", class_="teaser_conten1_center").find("h2").find("a").text,
                 "kategori":content.find("div", class_="teaser_conten1_center").find("h1").find("p").find("a").text,
                 "waktu_publish":content.find("div", class_="teaser_conten1_center").find("div", class_="date").text,
                 "waktu_scraping":current_time})
jdumps=jsons.dumps(data)
f.writelines(jdumps)
f.close()


            