from cv2 import cv2
import numpy as np


def task2():
    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        cv2.imshow("input", img)
        key = cv2.waitKey(10)
        if key == 27:  # esc
            break


if __name__ == '__main__':
    print(f'Hi, {cv2.__version__}')
    task2()
