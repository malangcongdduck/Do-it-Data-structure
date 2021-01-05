print('1부터 n까지 정수의 합을 구합니다.')
n=int(input('n을 입력하세요: '))

sum=0
for i in range (n+1): #for i in range(1, n+1)도 가능 range(10)하면 0-9까지의 값이 들어감 10개의 수가 들어감
    sum+=i

#range 함수
#1. range(n) 0이상 n미만인 수를 차례대로 나열하는 수열
#2. range(a,b) a이상 b미만인 수를 차례대로 나열하는 수열
#3. range(a,b,step) a이상 b미만인 수를 step 간격으로 나열하는 수열

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')
