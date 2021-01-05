from typing import Any, Sequence
import copy
import random

def seq_search(seq: Sequence, key: Any)->int:
    a=copy.deepcopy(seq)#->배열 복사
    a.append(key)#->배열의 마지막에 key값 추가

    i=0
    while True:
        if a[i]==key:
            break
        i+=1
        
    return -1 if i==len(seq) else i

if __name__=='__main__':
    num=int(input('원소 수를 입력하세요: '))
    x=[None]*num

    for i in range(num):
        x[i]=random.randint(1,10)
        print(f'{x[i]} ',end='')

    print()

    ky=int(input('검색할 값을 입력하세요: '))
    idx=seq_search(x, ky)

    if idx==-1:
        print('검색할 값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색값은 x[{idx}]에 있습니다.')