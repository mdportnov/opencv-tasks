from cv2 import cv2


def task5():
    img = cv2.imread("rus.png", cv2.IMREAD_COLOR)
    while True:
        cv2.imshow("source image", img)

        sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        cv2.imshow('Sobel horizontal', sobel_horizontal)
        cv2.imshow('Sobel vertical', sobel_vertical)

        edges = cv2.Canny(img, 50, 100)
        cv2.imshow('Canny', edges)

        key = cv2.waitKey(10)

        if key == 27:  # esc
            break


if __name__ == '__main__':
    print(f'Hi, {cv2.__version__}')
    task5()
