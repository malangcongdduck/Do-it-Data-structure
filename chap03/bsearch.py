from typing import Sequence, Any
import random

def bin_search(a: Sequence, key: Any)->int:
    pl=0
    pr=len(a)-1 #인덱스 기준

    
    while True:
        pc=(pl+pr)//2
        if a[pc]==key:
            return pc
        elif a[pc]<key:
            pl=pc+1
        else:
            pr=pc-1
        if pl>pc:
            break
    return -1

if __name__=='__main__':
    num=int(input('원소 수를 입력하세요: '))
    x=[None]*num

    for i in range (num):
        x[i]=random.randint(1,100)
    x.sort()
    
    print('<생성된 배열 데이터>')
    for i in range(num):
        print(f'{x[i]} ', end='')
    print()

    ky=int(input('검색할 값을 입력하세요: '))
    idx=bin_search(x, ky)

    if idx==-1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')
