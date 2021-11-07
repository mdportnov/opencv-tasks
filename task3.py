from cv2 import cv2


def rotate_image(mat, angle):
    height, width = mat.shape[:2]
    image_center = (width / 2, height / 2)

    rotation_mat = cv2.getRotationMatrix2D(image_center, angle, 1.)

    # для вращения вычисляются cos и sin, принимаем их абсолютные значения.
    abs_cos = abs(rotation_mat[0, 0])
    abs_sin = abs(rotation_mat[0, 1])

    #  найти новые границы ширины и высоты
    bound_w = int(height * abs_sin + width * abs_cos)
    bound_h = int(height * abs_cos + width * abs_sin)

    # вычесть старый центр изображения (возвращая изображение к исходному)
    # и добавить координаты нового центра изображения
    rotation_mat[0, 2] += bound_w / 2 - image_center[0]
    rotation_mat[1, 2] += bound_h / 2 - image_center[1]

    # повернуть изображение с новыми границами и переведенной матрицей поворота
    rotated_mat = cv2.warpAffine(mat, rotation_mat, (bound_w, bound_h))
    return rotated_mat


img = cv2.imread("rus.png", cv2.IMREAD_COLOR)
cv2.imshow('img', img)
img1 = rotate_image(img, 90)
cv2.imshow('img1', img1)
img2 = rotate_image(img1, -90)
cv2.imshow('img2', img2)

img3 = abs(cv2.subtract(img, img2)) * 10
cv2.imshow('img3', img3)

cv2.waitKey(0)

cv2.destroyAllWindows()
