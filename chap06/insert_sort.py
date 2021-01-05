def insert(a):
    n=len(a)
    for i in range(1,n):
        j=i
        tmp=a[i]
        while j>0 and a[j-1]>tmp:
            a[j]=a[j-1]
            j-=1
        a[j]=tmp

a=[1,6,3,7,12,2]


if __name__ == "__main__":            
    print('삽입 정렬 알고리즘을 구현합니다.')
    print(*a ,sep=' ', end='')
    print()

    insert(a)
    
    print('오름차순으로 정렬했습니다.')
    print(*a ,sep=' ', end='')