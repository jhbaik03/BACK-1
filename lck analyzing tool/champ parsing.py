import requests

champion = []

# get Json File
datas = requests.get('http://ddragon.leagueoflegends.com/cdn/13.5.1/data/ko_KR/champion.json')
datas = datas.json()

# 챔피언 파싱
for data in datas["data"]:
    champion.append(data)


for champ in champion:
    save_path = "C:\\Users\\백진헌\\Desktop\\lck analyzing tool\\champ\\champ" + 'Milio' + ".png"
    image_url = "http://ddragon.leagueoflegends.com/cdn/13.6.1/img/champion/" + 'Milio' + ".png"

    download_image = requests.get(image_url)

    with open(save_path, 'wb') as file:
        file.write(download_image.content)