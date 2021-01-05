a=[22,57,11,91,32]

def maximum(a):
    max=a[0]
    for i in range (1,len(a)):
        if a[i]>max:
            max=a[i]
    
    return max

print(f'a의 최대값은 {maximum(a)} 입니다.')