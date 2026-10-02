# installation of pillow library
# change the image extension
# resize image files
# resize multiple images using for loop
# Sharpness
# Brightness
# Color
# Contrast
# Image blur, GaussianBlur

from PIL import Image, ImageEnhance, ImageFilter
import os

img = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')

print(img)
# img.show()

# 250
MAX_SIZE = (250, 250)
img.thumbnail(MAX_SIZE)
img.save(r'E:\Python_OOP\picture_for_python\img1.small.jpg')


# change image extension
for item in os.listdir(r'E:\Python_OOP\picture_for_python'):
    if item.endswith('.jpg'):
        img1 = Image.open(
            os.path.join(r'E:\Python_OOP\picture_for_python', item)
        )
        filename, extension = os.path.splitext(item)
        img1.save(
            os.path.join(
                r'E:\Python_OOP\picture_for_python',
                f'{filename}.png'
            )
        )


# Sharpness
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
enhancer = ImageEnhance.Sharpness(img1)
enhancer.enhance(2).save(
    r'E:\Python_OOP\picture_for_python\girl1.sharp.jpg'
)


# Color
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
enhancer = ImageEnhance.Color(img1)
enhancer.enhance(2).save(
    r'E:\Python_OOP\picture_for_python\girl1.color.jpg'
)


# Brightness
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
enhancer = ImageEnhance.Brightness(img1)
enhancer.enhance(1.5).save(
    r'E:\Python_OOP\picture_for_python\girl1.brightness.jpg'
)


# Contrast
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
enhancer = ImageEnhance.Contrast(img1)
enhancer.enhance(1.5).save(
    r'E:\Python_OOP\picture_for_python\girl1.contrast.jpg'
)


# Image Blur
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
img1.filter(ImageFilter.BLUR).save(
    r'E:\Python_OOP\picture_for_python\girl1.blur.png'
)


# Gaussian Blur
img1 = Image.open(r'E:\Python_OOP\picture_for_python\img.jpeg')
img1.filter(ImageFilter.GaussianBlur(5)).save(
    r'E:\Python_OOP\picture_for_python\girl1.gaussian.png'
)