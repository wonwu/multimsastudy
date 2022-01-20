# sum 함수, dictionary.values()

홍길동1 = { '국어' : 95, '영어' : 90, '수학' : 80, '과학' : 50 }
홍길동2 = { '국어' : 100, '영어' : 50, '수학' : 90, '과학' : 90 }
홍길동3 = { '국어' : 99, '영어' : 60, '수학' : 100, '과학' : 40 }
홍길동4 = { '국어' : 55, '영어' : 80, '수학' : 80, '과학' : 60 }

sum1 = sum(홍길동1.values())
avg1 = sum1 / len(홍길동1)

sum2 = sum(홍길동2.values())
avg2 = sum2 / len(홍길동2)

sum3 = sum(홍길동3.values())
avg3 = sum3 / len(홍길동3)

sum4 = sum(홍길동4.values())
avg4 = sum4 / len(홍길동4)

print("홍길동1 합계 = {}, 평균 = {}" .format(sum1, avg1))
print("홍길동2 합계 = {}, 평균 = {}" .format(sum2, avg2))
print("홍길동3 합계 = {}, 평균 = {}" .format(sum3, avg3))
print("홍길동4 합계 = {}, 평균 = {}" .format(sum4, avg4))

totalSum = sum1 + sum2 + sum3 + sum4
totalAvg = ( avg1 + avg2 + avg3 + avg4 ) / 4
print("전체4명 합계 = {}, 평균 = {}" .format(totalSum, totalAvg))
