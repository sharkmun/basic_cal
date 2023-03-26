# 사용자로부터 체중(kg)과 신장(cm) 입력받기
print("남자 전용입니다")

weight = float(input("체중(kg)을 입력하세요: "))
height = float(input("신장(cm)을 입력하세요: "))
age = float(input("나이를 입력하세요:"))



# 기초대사량  계산

M= 88.4 + (13.4*weight) + (4.8*height) -(5.36*age)

# 소수점 둘째자리까지 출력

print("당신의 기초대사량은 약{:.2f} 입니다.".format(M))

