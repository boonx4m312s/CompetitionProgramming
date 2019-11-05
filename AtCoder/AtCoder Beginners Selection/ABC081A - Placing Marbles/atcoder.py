# -*- coding: utf-8 -*-
# https://atcoder.jp/contests/abs/tasks/abc081_a
# ABC081A - Placing Marbles
def main():
    cnt = 0
    s = str(input())
    for i in enumerate(s):
        if i[1] == '1':
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()