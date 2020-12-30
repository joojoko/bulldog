import requests
from bs4 import BeautifulSoup
import pandas as pd
import xmltodict
import json

key = "IZWMa17q6c%2F7c9GxuIsta09lbD%2B2zj7e0Eblc%2BUKMeBoWo8qaHiPAFVrdohhKIOn9Q2d7f7hCbyUU%2FNdjn4r0w%3D%3D"
url = "http://openapi.nature.go.kr/openapi/service/rest/FungiService/fngsIlstrSearch?serviceKey=IZWMa17q6c%2F7c9GxuIsta09lbD%2B2zj7e0Eblc%2BUKMeBoWo8qaHiPAFVrdohhKIOn9Q2d7f7hCbyUU%2FNdjn4r0w%3D%3D&pageNo=&numOfRows=1000&st=&sw=&dateGbn=&dateFrom=&dateTo=&".format(key)
# content = requests.get(url).content
# print(content)

content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict['response']['body'], ensure_ascii=False)
jsonObj = json.loads(jsonString)
# print(jsonObj)


# df = pd.DataFrame(jsonObj)
# print(df.count)
for item in jsonObj['items']['item']:
    print(item)

file = open("./nonPayment.json", "w+")
file.write(json.dumps(jsonObj['items']['item']))