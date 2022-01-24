from flask import Flask
import json
import requests
import pandas as pd

# 변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
# application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성

#함수 선언 
# 시작할 때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로를 지정 - 앞에서 선언한 app 변수를 사용
def FlaskLab(): # 요청 - 메서드(함수) 이름 요청에서 사용하는 것
    return "Flask 데이터 응답" # 응답 -  return 에서 돌려주는 데이터가 응답

@app.route("/data1")
def FlaskData():#startPage, pageCount, address): # 요청 받음
    keyValue = r"dcDOac8qR1Hlkma1oUeF%2BzRbGEis9zq%2BZKa0NoKAwmCORC9AIPE4FYfn3b3bNpI%2BlseM4g%2BZ%2BTUX8CT3tFZDsw%3D%3D"   

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond%5BorgZipaddr%3A%3ALIKE%5D=" + "성북구" 
    dataURL += "&serviceKey=" + str(keyValue)
  
    # dataResult = requests.get(dataURL)
    #공공데이터 요청 후 데이터 받기 : flask - request / requests 기능 사용
    
    dataResult = json.loads(requests.get(dataURL))

    resultData2 = pd.DataFrame(dataResult)

    # return json.loads(dataResult) # 공공데이터 결과 값 응답
    # return dataResult
    return resultData2
