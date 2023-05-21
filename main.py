from pytoimage import PyImage
from pathlib import Path
import os
from PIL import Image

def cod_to_img(file_path='main.py'):
    path = Path(file_path)

    if path.is_file():
        code = PyImage(file_path, background=(255, 200, 200))
        palette = {
            'line': (255, 0, 0),
            'normal': (0, 0, 0),
        }

        code.set_color_palette(palette=palette)
        code.generate_image()
        img_name = f"{file_path.split('.')[0]}.jpg"
        code.save_image(img_name)

        return img_name

def add_logo(image_name, logo_name):

    img = Path(image_name)
    logo = Path(logo_name)
    if not img.is_file() or not logo.is_file():
        return "File not found"

    im = Image.open(image_name)
    width, height = im.size

    logo_file = logo_name
    logoIm = Image.open(logo_file).convert("RGBA")
    if height > width:
        logoIm = logoIm.resize((int(width / 10 * (height / width)), int(height / 10)))
    else:
        logoIm = logoIm.resize((int(width / 10), int(height / 10 * (width / height))))
    logoWidth, logoHeight = logoIm.size

    im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
    im.save(os.path.join('./', 'withlogo.png'))

    return f'Logo has been added to {image_name}'


def main():
    file_path = input('Enter a file name: ')
    logo_file = input('Enter a logo name: ')
    image_name = cod_to_img(file_path=file_path)
    print(add_logo(image_name, logo_file))


if __name__ == '__main__':
    main()


