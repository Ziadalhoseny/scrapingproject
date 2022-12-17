import requests
from bs4 import BeautifulSoup

# find the elements containing info we need(the names of players,kit numbers,players position)

names=[]
kit=[]
position=[]

result=requests.get("https://www.realmadrid.com/ar/football/squad")
src=result.content
soup =BeautifulSoup(src,"html.parser")

players_name=soup.find_all("a",{"itemprop":"url"})
kit_numbers=soup.find_all("strong",{"class":"m_player_info_number"})
players_position=soup.find_all("span",{"itemprop":"jobTitle"})

for i in range(len(kit_numbers)):
 names.append(players_name[i].text)
 print(players_name[i].text)

 kit.append(kit_numbers[i].text)
 print(kit_numbers[i].text)

 position.append(players_position[i].text)
 print(players_position[i].text)

