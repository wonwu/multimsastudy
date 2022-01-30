# 220126 정답

from flask import Flask
import json
import requests


# 변수 선언 - 프로그램의 이름 저장하는 변수(파일 이름 저장 변수)
# application server 개발 app 변수를 많이 사용
app = Flask(__name__) # flask 프로그램 시작 기본 값은 = app.py 파일을 생성

#함수 선언 
# 시작할 때 경로(route) 선언해야함
@app.route("/") # 웹 사이트 경로를 지정 - 앞에서 선언한 app 변수를 사용
def FlaskLab(): # 요청 - 메서드(함수) 이름 요청에서 사용하는 것
    return "Flask 데이터 응답" # 응답 -  return 에서 돌려주는 데이터가 응답

@app.route("/data1")
def FlaskData():
    keyValue = r""

    dataURL = "https://api.odcloud.kr/api/apnmOrg/v1/list?"
    dataURL += "page=" + str(1) + "&perPage=" + str(10)
    dataURL += "&cond%5BorgZipaddr%3A%3ALIKE%5D=" + "강남구" # 또는 본인 사는 지역구
    dataURL += "&serviceKey=" + keyValue

    dataResult = requests.get(dataURL)
  
    exchangeData = dataResult.text
    return json.loads(exchangeData) 
  
