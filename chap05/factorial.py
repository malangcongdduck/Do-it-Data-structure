import math

def factorial(num):
    if num>0:
        return num * factorial(num-1)
    else:
        return 1

if __name__ == "__main__":
    x=int(input('수를 입력하세요: '))
    print(f'함수를 사용한 {x}!의 결과는 {factorial(x)}입니다.')
    print(f'math모듈을 사용한 {x}!의 결과는 {math.factorial(x)}입니다.')