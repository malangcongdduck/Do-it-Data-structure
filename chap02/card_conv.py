def card_conv(x: int, r: int)->str:
    d=''
    dchar='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    while x>0:
        d+=dchar[x%r]#해당하는 문자를 꺼내 결합
        x//=r

    return d[::-1]#역순으로 반환


if __name__=='__main__':
    print('10진수를 n진수로 변환합니다.')

    while True:
        while True:
            no=int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
            if no>0:
                break

        while True:
            cd=int(input('변환하고 싶은 진수로 입력하세요: '))
            if cd>0:
                break

        print(f'{cd}진수로 변환한 {no}는 {card_conv(no, cd)}입니다.')

        retry = input('한 번 더 변환할까요?(y/n): ')
        if retry in {'N','n'}:
            break