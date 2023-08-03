import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

myEmail="rawadkady@gmail.com"
myPass="rawad.182002"
toEmail="rawad182002@gmail.com"
URL="https://www.amazon.com/Rich-Dad-Poor-Teach-Middle/dp/1612680194/ref=sr_1_1?crid=3HLLMXAZUKUWL&keywords=rich+dad+poor+dad&qid=1652444734&sprefix=rich+dad%2Caps%2C434&sr=8-1"

response=requests.get(url=URL,
                      headers={
                          "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                          "Accept-Language":"en-US,en;q=0.9"
                      })
web_page=response.text
soup=BeautifulSoup(web_page,"lxml")
price=soup.find(name="span",id="price",class_="a-size-medium a-color-price header-price a-text-normal")
price_float=float(price.getText().replace("$",""))
print(price_float)
content=f"Greetings Dear Rawad,\nInstant Rich Dad Poor Dad Book is now {price}\n{URL}\nPress the above link to buy NOW!"
if price_float<8:
    with smtplib.SMTP('smtp.gmail.com') as connections:
        connections.starttls()
        connections.login(user=myEmail,password=myPass)
        connections.sendmail(from_addr=myEmail,to_addrs=toEmail,msg=content)

