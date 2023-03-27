import os
import qrcode.image.svg


def generate_qr_code(file: str = 'test.txt', method: str = 'basic', output: str = 'qrcode') -> str:

    try:
        data = open(file, 'r').readline()
    except FileNotFoundError as error:
        # print(f'[!] {error}.')
        exit(f'[!] {error}.')

    methods = ['basic', 'fragment', 'path', 'fill']
    if method in methods:
        if method == 'basic':
            # Simple factory, just a set of rects.
            factory = qrcode.image.svg.SvgImage
        elif method == 'fragment':
            # Fragment factory (also just a set of rects)
            factory = qrcode.image.svg.SvgFragmentImage
        elif method == 'path':
            # Combined path factory, fixes white space that may occur when zooming
            factory = qrcode.image.svg.SvgPathImage
        elif method == 'fill':
            # Combined path factory, fixes white space that may occur when zooming and fill background
            factory = qrcode.image.svg.SvgPathFillImage
    else:
        exit(f'[!] Do not have this method: ({method}). \n[-] Here are all the available methods: {methods}.')

    img = qrcode.make(data, image_factory = factory)
    img.save(f"{output}.svg")

    return str(os.path.abspath(f'{output}.svg'))


def main():
    try:
        path = generate_qr_code('test.txt', 'fill', 'my_qrcode')
        print(path)
    except Exception as error:
        print(f'[!] {error}.')


if __name__ == '__main__':
    main()