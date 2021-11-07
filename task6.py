import numpy as np
from cv2 import cv2


def make_some_noise(image, delta=20):
    row, col, ch = image.shape
    mean = 0
    sigma = delta ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)

    new_image = image

    for i in range(row):
        for j in range(col):
            for k in range(3):
                newBit = new_image[i][j][k] + gauss[i][j][k]
                if 0 <= newBit <= 255:
                    new_image[i][j][k] = newBit

    return new_image


def task6():
    img = cv2.imread("rus.png", cv2.IMREAD_COLOR)
    cv2.imshow("source image", img)

    noised = make_some_noise(img, 100)
    cv2.imshow("noised image", noised)

    blurred = cv2.GaussianBlur(noised, (3, 3), cv2.BORDER_DEFAULT)
    cv2.imshow("blurred image", blurred)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    task6()
