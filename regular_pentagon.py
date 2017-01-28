#!/usr/bin/env python3


"""turtleで正5角形を描画
"""


from turtle import *


def regular_pentagon():
    """turtleで正5角形を描画する関数
    """

    for i in range(5):
        forward(100)
        left(72)

    input_data = input('終了: enterキー等: ')

if __name__ == '__main__':
    regular_pentagon()
