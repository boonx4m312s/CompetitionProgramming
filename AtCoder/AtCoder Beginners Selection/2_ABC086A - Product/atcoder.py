# -*- coding: utf-8 -*-
# 整数の入力
# スペース区切りの整数の入力
def main():
    a, b = map(int, input().split())
    if (a*b) % 2 == 0:
        print('Even')
    else:
        print('Odd')

if __name__ == '__main__':
    main()
