#!/usr/bin/env python3


"""turtleで正方形を描画
"""


from turtle import *


def square():
    """turtleで正方形を描画する関数
    """

    for _ in range(4):
        forward(100)
        left(90)

    # リスト内包表記:
    # [[forward(100), left(90)] for _ in range(4)]

    input_data = input('終了: enterキー等: ')

if __name__ == '__main__':
    square()
