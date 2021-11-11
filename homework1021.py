# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:31:03 2021

@author: CJCU-CC
"""

import requests
URL = "https://api.kcg.gov.tw/api/service/get/94434e0c-4a53-4e04-985d-91997e7dd716"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

req = requests.get(URL,headers = headers)
list_data = req.json()["data"]

ans = open('C:\\Users\\CJCU-CC\\Desktop\\新增資料夾\\homework.csv', "w")

data = ""
for i in range(0,len(list_data)):
    data = [j for j in list_data[i].keys()]
    
for l in data:
    string = str(l) + ","
    ans.write(string)
ans.write("\n")

for i in range(0,len(list_data)):
    for l in data:
        ans.write(str(list_data[i][l]) +",")
    ans.write("\n")

ans.close()
print("done")
