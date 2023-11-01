'''1. 입력과 출력'''
### 입력을 받고

# Default input 스트링 타입, 문자열 타입으로 받아와주도록 만들어짐

# case1: 단순히 정수
number = int(input())

# case2: 수열
First, Second, Third = map(int, input().split())

# case3: 단순히 문자
string = input()

# case4: 문자열
First, Second, Third = map(str, input().split())

### 계산을 하고


### 출력을 한다.
print(number)


'''2. 배열'''
list = [0, 0, 0, 0]
list = ["hi", "hi", "hi"]

list1 = list(map(int, input().split()))
print(list1)

# 배열 안에 있는 친구들만 예쁘게 보여주고 싶을 때
print(*list1)


'''3. 반복문'''

for _ in range(100):
    print('hi')

while number < 10:
    print(number)
    number = number + 1


'''4. 조건문'''
name = '코딩이'
if name == '코딩이':
    print('니 이름은 코딩이')
else:
    print('내 이름은 코딩이')

