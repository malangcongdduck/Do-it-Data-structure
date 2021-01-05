x=['John','George','Paul','Ringo']

#enumerate란?
#인덱스와 원소를 짝지어 튜플로 꺼내는 내장 함수

for i, name in enumerate(x):
    print(f'x[{i}]={name}')
    # (0,'John'), (1,'George')...

print()

for i, name in enumerate(x, 1):
    print(f'{i}번째 = {name}')
    # (1,'John'), (2,'George')...

print()

#리스트의 모든 원소를 스캔
for i in x:
    print(i)

#-> 튜플로 바꾸고 싶으면 x를 ()로 수정!