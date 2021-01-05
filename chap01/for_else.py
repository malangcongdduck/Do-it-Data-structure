import random

n=int(input('난수의 개수를 입력하세요.: '))

for _ in range(n):
    r=random.randint(10,99) #난수 생성은 random.randint(a,b)이다. a이상 b이하인 정수
    print(r, end='')
    if r==13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수 생성을 종료합니다.')   

#for-else문?
#for문이 중간에 break 등으로 인해 끊기지 않고 끝까지 수행되었을 때 else문 내부의 코드가 수행되는 구조
#for문이 중간에 break되었는지 아닌지를 판단할 때 사용하기 좋음.