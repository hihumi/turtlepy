#!/usr/bin/env python3


"""turtleで三角形を描画
"""


from turtle import *


def triangle():
    """turtleで三角形を描画する関数
    """

    for _ in range(3):
        forward(100)
        left(120)

    # done()よりも以下のほうがenterキー等で終了できるので楽
    input_data = input('終了: enterキー等: ')

if __name__ == '__main__':
    triangle()
