import json

# with open("dataLab\\mydata.json", "rb") as jsonFile:
#     tempData = json.load(jsonFile)
#     #tempData = json.loads(jsonFile)#오류
#     reusltData1 = tempData["name"]
#     reusltData2 = tempData["age"]
#     reusltData3 = tempData["address"]
#     reusltData4 = tempData["email"]
#     reusltData5 = tempData["empcheck"]

try:
    jsonFile = open("dataLab\\mydata.json", "rb")
    tempData = json.load(jsonFile)
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except Exception as error:
    print("오류: " + error)
else:
    jsonFile.close()


jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

# with open("dataLab\\mydata5.json", "w", encoding="utf-8") as writeFile:
#     json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) 

try:
    writeFile = open("dataLab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile, ensure_ascii=False, indent=4) 
except Exception as error:
    print("오류: " + error)
else:
    writeFile.close()


#디버깅 변수 선언함(임시)
temp = 0
