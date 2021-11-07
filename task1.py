from cv2 import cv2
import numpy as np


def task1():
    img = cv2.imread("rus.png", cv2.IMREAD_COLOR)
    cv2.imshow("image", img)
    cv2.imwrite("image.png", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    print(f'Hi, {cv2.__version__}')
    task1()
