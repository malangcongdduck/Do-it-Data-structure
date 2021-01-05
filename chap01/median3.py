def med3_1(a,b,c):
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

def med3_2(a,b,c):
    if(b>=a and c<=a) or (b<=a and c>=a):
        return a
    elif (a>b and c<b) or (a<b and c>b):
        return b
    return c

print('세 정수의 중앙값을 구합니다.')
a=int(input('정수 a의 값을 입력하세요: '))
b=int(input('정수 b의 값을 입력하세요: '))
c=int(input('정수 c의 값을 입력하세요: '))

print(f'med3_1의 중앙값은 {med3_1(a,b,c)}입니다.')
print(f'med3_2의 중앙값은 {med3_2(a,b,c)}입니다.')