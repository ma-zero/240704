hello_world = '엄마가 말했다. "밥 먹었니?"'
print(hello_world)

name = "임하영"
money = 100
print("안녕하세요. 제 이름은", name, "입니다.")
print("입력하신 금액은", money, "원 입니다.")
## 글자는 글자끼리만 사칙연산 가능, 숫자는 숫자끼리만 사칙연산 가능

# 데이터 출력시, % 기호 사용하는 방법
name = "마지로"
print("안녕하세요. 저의 이름은 %s 입니다." % name)

money = 10000
print("입력하신 금액은 %d원 입니다." %money)

# quiz
a = 7
b= 3
result = a + b
print(result)


# 문자열 길이 구하기
hello_world = "엄마가 말헸다. '밥은 먹었니'"
print(len(hello_world))


# 문자열 슬라이싱
자유로운_문자열 = "아무 문자열이나 한번 작성해주세요."
print(len(자유로운_문자열))
print(자유로운_문자열[0:4])


# 문자열 치환
date = "2024.07.04"
print("바꾸기 전의 데이터 : ", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터 : ", date)

#문자열 여러줄 출력하기 -> \n 사용
자유로운_문자열_2 = "아무 문자열이나 한 번 작성해주세요. 으앙 파이썬 너무너무 어렵읍니다.\n잠깐 졸았는데 진도가 훅훅 빠져나가는 매직.. 이거 제가 할 수 있는게 맞습니까? 교수님 살려주세요.."
print(자유로운_문자열_2)