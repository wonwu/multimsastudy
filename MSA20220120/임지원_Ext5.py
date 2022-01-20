# 2차원 리스트, 2중 for문

students =[ [95,90,80,50],
            [100,50,90,90],
            [99,60,100,40],
            [55,80,80,60] ]
sumList = []
avgList = []

for i in range(len(students)):
    sumAll = 0
    for j in range(4):
        sumAll += students[i][j]
    sumList.append(sumAll)
    avgList.append(sumAll/4)


print("홍길동1 합계 = {}, 평균 = {}" .format(sumList[0], avgList[0]))
print("홍길동2 합계 = {}, 평균 = {}" .format(sumList[1], avgList[1]))
print("홍길동3 합계 = {}, 평균 = {}" .format(sumList[2], avgList[2]))
print("홍길동4 합계 = {}, 평균 = {}" .format(sumList[3], avgList[3]))

totalSum = sum(sumList)
totalAvg = sum(avgList) / 4
print("전체4명 합계 = ", totalSum, "평균 = ", totalAvg)
