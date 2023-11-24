import requests
from bs4 import BeautifulSoup
import re
# TODO 使用User-Agent字段实现反反扒策略
headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"}
url="http://43.139.169.182/hospital.html"
# TODO  爬取网页上的数据
requests.get(url=url,headers=headers)
response=requests.get(url=url)
soup=BeautifulSoup(response.content.decode("utf-8"),"html.parser")
result=soup.find_all(class_="message-right")+soup.find_all(class_="message-left")
with open("赛位号_hospital.txt","w",encoding="utf-8") as f:
    for i in result:
        print(i.find(class_="text").get_text())
        f.write(i.find(class_="text").get_text()+"\n")