print('*을 출력합니다.')

n=int(input('몇 개를 출력할까요?: '))
w=int(input('몇 개마다 줄바꿈을 할까요?: '))

for _ in range(n//w):
    print('*' * w)

if n % w:
    print('*'*(n%w))

#while i<=n: -> 반복문 종료시 i=n+1
#for i in range (1, n+1): -> 반복문 종료시 i=n