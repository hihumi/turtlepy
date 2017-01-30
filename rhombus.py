#!/usr/bin/env python3


"""turtleで菱形を描画
"""


from turtle import *


def rhombus():
    """turtleで菱形を描画する関数
    """

    left(35)
    forward(100)
    left(110)
    forward(100)
    left(70)
    forward(100)
    left(110)
    forward(100)

    input_data = input('終了: enterキー等: ')

if __name__ == '__main__':
    rhombus()
