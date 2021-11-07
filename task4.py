import numpy as np
from cv2 import cv2


def task4():
    img = cv2.imread("rus.png", cv2.IMREAD_COLOR)
    while True:
        cv2.imshow("source image", img)

        red_channel = img[:, :, 2]
        red_img = np.zeros(img.shape)
        red_img[:, :, 2] = red_channel
        cv2.imshow("red channel", red_img)

        green_channel = img[:, :, 1]
        green_img = np.zeros(img.shape)
        green_img[:, :, 1] = green_channel
        cv2.imshow("green channel", green_img)

        blue_channel = img[:, :, 0]
        blue_img = np.zeros(img.shape)
        blue_img[:, :, 0] = blue_channel
        cv2.imshow("blue channel", blue_img)

        merged = cv2.merge([blue_channel, green_channel, red_channel])
        cv2.imshow("Merged", merged)

        key = cv2.waitKey(10)

        if key == 27:  # esc
            break


if __name__ == '__main__':
    task4()
