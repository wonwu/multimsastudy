# 1. 딕션어리 이용해 평균 점수 구하기
# 2. 셋 이용해 1~100까지 숫자 중에 공배수 구하기 : 3과 5의 공배수, 합집합 (표현식 사용)
# 3. 리스트 데이터 : 7, 5, 3, 1, -1, -3, -5, -7 출력 : range 활용
# 4. 3번 결과를 튜플로 변경 (형변환)

# 1. 
dicScore = {
            '국어' : 95,
            '영어' : 90,
            '수학' : 80,
            '과학' : 50
            }

avg = sum(dicScore.values()) / len(dicScore)

# 2.
setData1 = set()
setData2 = set()
for i in range(1,101):
    if i % 3 == 0:
        setData1.add(i)
    if i % 5 == 0:
        setData2.add(i)

resultData1 = setData1 & setData2 # 교집합 (3과 5의 공배수)
resultData2 = setData1 | setData2 # 합집합


# 3. 리스트 데이터 : 7, 5, 3, 1, -1, -3, 5, -7 출력 : range 활용
listData1 = list(range(7, -8, -2))
print(listData1)

# 4. 위의 결과 튜플로 변경 (형변환)
tupleData1 = tuple(listData1)

# 디버깅을 위한 임시 변수
temp = 0
