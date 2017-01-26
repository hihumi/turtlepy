#!/usr/bin/env python3


"""turtleで平行四辺形を描画
"""


from turtle import *


def parallelogram():
    """turtleで平行四辺形を描画する関数
    """

    for i in range(2):
        forward(200)
        left(60)
        if i % 1 == 0:
            forward(100)
            left(120)

    input_data = input('終了: enterキー等: ')

if __name__ == '__main__':
    parallelogram()
