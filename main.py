from PIL import Image, ImageEnhance
from math import sqrt

def open_image(path):
    newImage = Image.open(path)
    return newImage

def save_image(image, path):
    image.save(path, 'png')

def create_image(i, j):
    image = Image.new("RGB", (i, j), "white")
    return image

def get_pixel(image, i, j):
    width, height = image.size
    if i > width or j > height:
        return None

    pixel = image.getpixel((i, j))
    return pixel

def grayscale_sqrt(path):
    image = open_image(path)
    file_name = path.split('.')[0]
    file_extension = path.split('.')[1]
    file_new_name = file_name + 'sqrtgrayscale.' + file_extension
    newImage = create_image(image.size[0], image.size[1])
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = get_pixel(image, i, j)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            gray = int(sqrt(red**2 + green ** 2 + blue ** 2))
            newImage.putpixel((i, j), (gray, gray, gray))
    save_image(newImage, file_new_name)
    return newImage

def grayscale_approximation(path):
    image = open_image(path)
    file_name = path.split('.')[0]
    file_extension = path.split('.')[1]
    file_new_name = file_name + 'grayscaleapprox.' + file_extension
    newImage = create_image(image.size[0], image.size[1])
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = get_pixel(image, i, j)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            gray = int((red + blue + green) / 3)
            newImage.putpixel((i, j), (gray, gray, gray))
    save_image(newImage, file_new_name)
    return newImage


def grayscale_standard(path):
    image = open_image(path)
    file_name = path.split('.')[0]
    file_extension = path.split('.')[1]
    file_new_name = file_name + 'standardgrayscale.' + file_extension
    newImage = create_image(image.size[0], image.size[1])
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = get_pixel(image, i, j)
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]

            gray = int(red * 0.299) + int(green * 0.587) + int(0.114 * blue)
            newImage.putpixel((i, j), (gray, gray, gray))
    save_image(newImage, file_new_name)
    return newImage

gray1 = grayscale_sqrt('lav.jpg')
gray2 = grayscale_approximation('lav.jpg')
gray3 = grayscale_standard('lav.jpg')


