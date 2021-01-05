def bubble(a):
    n=len(a)
    change=0
    for i in range(n-1,1,-1):
        for j in range(0,i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                change+=1
        if change==0:
            break

a=[1,6,3,7,12,2]


if __name__ == "__main__":            
    print('버블 정렬 알고리즘을 구현합니다.')
    print(*a ,sep=' ', end='')
    print()

    bubble(a)
    
    print('오름차순으로 정렬했습니다.')
    print(*a ,sep=' ', end='')