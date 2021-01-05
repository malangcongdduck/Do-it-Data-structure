counter = 0 #나눗셈 횟수
ptr = 0 #소수 개수
prime = [None]*500 #소수 배열

prime[ptr]=2
ptr+=1

for n in range(3, 1001, 2):#홀수만 비교
    for i in range(1, ptr):#이미 찾은 소수로 나눔
        counter +=1
        if n%prime[i]==0:
            break
    else:
        prime[ptr]=n
        ptr+=1


for i in range(ptr):
    print(prime[i])
print(f'나눗셈을 실행한 횟수: {counter}')