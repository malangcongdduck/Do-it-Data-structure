def select(a):
    n=len(a)
    
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if a[min]>a[j]:
                min=j
        a[i],a[min]=a[min],a[i]
                

                

a=[1,6,3,7,12,2]


if __name__ == "__main__":            
    print('선택 정렬 알고리즘을 구현합니다.')
    print(*a ,sep=' ', end='')
    print()

    select(a)
    
    print('오름차순으로 정렬했습니다.')
    print(*a ,sep=' ', end='')