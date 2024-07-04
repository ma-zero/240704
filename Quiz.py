## Quiz6 문자 "abcd"의 a를 대문자 A로 치환
Alpha = "abcd"
Alpha = Alpha.replace("a", "A")
print(Alpha)

## Quiz5 Python의 문자열을 거꾸로 추출
파이썬 = "Python"
a = "P"
b = "y"
c = "t"
d = "h"
e = "o"
f = "n"
print(len(파이썬))
print(파이썬[-1],파이썬[4],파이썬[3],파이썬[2],파이썬[1],파이썬[0])
print(f,e,d,c,b,a)

## Quiz7 평균구하기
nums = [1, 2, 3, 4, 5]
nums = list(range(1,6))
print(nums)
print(len(nums))
# 1번식
print((nums[0] + nums[1] + nums[2] + nums[3] + nums[4])/5)
# 2번식
sum_nums = (nums[0] + nums[1] + nums[2] + nums[3] + nums[4])
average = sum_nums / len(nums)
print(average)


## Quiz8 주어진 딕셔너리에서 banana의 값을 추출하는 파이썬 코드 작성
dic = {"apple" : 3, "banana" : 5, "cherry" : 2}
dic["banana"]
print(dic["banana"])


## Main Quiz 한국, 미국, 중국의 위도, 경도 데이터를 dictionary로 만들것
dic_1 = {"한국" : {"위도" : 33, "경도" : 127}, "미국" : {"위도" : 35, "경도" : 90}, "중국" : {"위도" : 35 , "경도" : 100}}
print(dic_1["한국"]["위도"])