import os
import pathlib
import shutil
import subprocess


def binarize_an_image(input_image, output_image, k=0.3):
    subprocess.run(['./binarization', '-k', str(k), input_image, output_image])


def pdf_to_images(pdf_path, image_dir_path):
    assert os.path.isfile(
        pdf_path), '{} does not exist or is not a file.'.format(pdf_path)
    assert os.path.isdir(
        image_dir_path), '{} does not exist or is not a directory.'.format(image_dir_path)

    subprocess.run(['pdftoppm', '-tiff', '-tiffcompression',
                    'lzw', '-scale-to', '3000', pdf_path, os.path.join(image_dir_path, 'image')])


def images_to_pdf(image_dir_path, pdf_path, extension='*.tif'):
    assert os.path.isdir(
        image_dir_path), '{} does not exist or is not a directory.'.format(image_dir_path)

    subprocess.run('img2pdf {} -o {} --pagesize A4'.format(os.path.join(image_dir_path,
                                                                        extension), pdf_path), shell=True)


def main():
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.mkdir('temp')

    for file in os.listdir('input'):
        if file.endswith('.pdf'):
            print('Begin converting for {}.'.format(file))
            os.mkdir(os.path.join('temp', 'original'))
            os.mkdir(os.path.join('temp', 'converted'))

            print('Extracting images from {}'.format(file))
            pdf_to_images(os.path.join('input', file),
                          os.path.join('temp', 'original'))

            for image in os.listdir(os.path.join('temp', 'original')):
                binarize_an_image(os.path.join('temp', 'original', image), os.path.join(
                    'temp', 'converted', image))

            print('Combining images ...')
            images_to_pdf(os.path.join('temp', 'converted'),
                          os.path.join('output', file))

            shutil.rmtree(os.path.join('temp', 'original'))
            shutil.rmtree(os.path.join('temp', 'converted'))
            print('Finish converting for {}.\n'.format(file))

    os.rmdir('temp')


if __name__ == "__main__":
    main()
