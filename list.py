##### List

a = [1,2,3]
print(a[1])
print(type([a]))

# 수열 만들기
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(0, 10))

print(list(range(10)))
print(list(range(1,20)))

print(list(range(0,20,2)))
# 12줄 range(0,20,2) 일 때, 0은 시작지점, 20은 끝지점, 2는 수열이 뛰는 크기

# 리스트에 요소 추가 및 제거하기
num_2 = [1,2,3,4,5]
num_2.append(7)
print(num_2)
num_2.remove(5)
print(num_2)

