import cv2 as cv
import numpy as np
import argparse


# -i 'img\lago-pedras.jpg' -o 'img\lago-pedras-annot.jpg'
#       -a perc
#       -s perc
#       -m factor
def init():
    parser = argparse.ArgumentParser(
        description="Image annotation using OpenCV")
    parser.add_argument('-i', '--input', metavar='input_file_name',
                        required=True)
    parser.add_argument('-o', '--output', metavar='output_file_name',
                        required=True)
    parser.add_argument('-a', '--add', type=int,
                        help='Add (brightness)', metavar='perc')
    parser.add_argument('-s', '--sub', type=int,
                        help='Subtract (reduce brightness)', metavar='perc')
    parser.add_argument('-m', '--mult', type=float,
                        help='Multiply (change contrast)', metavar='factor')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = vars(parser.parse_args())
    return args


def load_input(input_file):
    return cv.imread(input_file, 1)


# Main code starts here
conf = init()
input_img = load_input(conf['input'])
output_img = input_img

if (conf['verbose']):
    print(conf)
if (conf['add'] is not None and conf['sub'] is not None):
    print('You can use -a or -s but not both!')
    exit(1)
if (conf['add'] is not None):
    matrix1s = np.ones(input_img.shape, dtype="uint8") * conf['add']
    cv.add(input_img, matrix1s, output_img)
elif (conf['sub'] is not None):
    matrix1s = np.ones(input_img.shape, dtype="uint8") * conf['sub']
    cv.subtract(input_img, matrix1s, output_img)
if (conf['mult'] is not None):
    matrix_f = np.ones(input_img.shape, dtype="uint8") * conf['mult']
    output_img = np.uint8(np.clip(
        cv.multiply(np.float64(input_img), matrix_f), 0, 255))

cv.imwrite(conf['output'], output_img)
