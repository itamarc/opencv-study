import cv2 as cv
import numpy as np
import argparse


# -i 'img\lago-pedras.jpg' -o 'img\lago-pedras-annot.jpg'
#       -a perc
#       -s perc
#       -m factor
#       -t thresh
#       -d blksize const
#       -n (AND operator) maskfile
#       -o (OR operator) maskfile
#       -x (XOR operator) maskfile
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
    parser.add_argument('-t', '--thresh', type=int, metavar='thresh',
                        help='Convert to binary image using threshold')
    parser.add_argument('-d', '--adapthresh', nargs=2, type=int,
                        metavar=('block_size', 'constant'),
                        help='Convert to binary image using an adaptive \
                            threshold')
    parser.add_argument('-n', '--andoper', metavar='mask_file_name',
                        help='Apply AND operator with mask from file')
    parser.add_argument('-r', '--oroper', metavar='mask_file_name',
                        help='Apply OR operator with mask from file')
    parser.add_argument('-x', '--xoroper', metavar='mask_file_name',
                        help='Apply XOR operator with mask from file')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = vars(parser.parse_args())
    args['adapthresh_on'] = args['adapthresh'] is not None
    args['bitwise_oper_on'] = False
    if (args['andoper'] is not None):
        args['bitwise_oper'] = 'andoper'
        args['bitwise_oper_on'] = True
    if (args['oroper'] is not None):
        args['bitwise_oper'] = 'oroper'
        args['bitwise_oper_on'] = True
    if (args['xoroper'] is not None):
        args['bitwise_oper'] = 'xoroper'
        args['bitwise_oper_on'] = True
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
if (conf['thresh'] is not None):
    gray_img = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)
    retval, output_img = cv.threshold(gray_img, conf['thresh'],
                                      255, cv.THRESH_BINARY)
if (conf['adapthresh_on']):
    gray_img = cv.cvtColor(input_img, cv.COLOR_BGR2GRAY)
    output_img = cv.adaptiveThreshold(gray_img, 255.0,
                                      cv.ADAPTIVE_THRESH_MEAN_C,
                                      cv.THRESH_BINARY,
                                      conf['adapthresh'][0],
                                      float(conf['adapthresh'][1]))
if (conf['bitwise_oper_on']):
    mask_file = cv.imread(conf[conf['bitwise_oper']], 0)
    (y_in, x_in, chan_in) = input_img.shape
    (y_msk, x_msk) = mask_file.shape
    if (y_in != y_msk or x_in != x_msk):
        mask_file = cv.resize(mask_file, (x_in, y_in), cv.INTER_LINEAR)
    retval, img_mask = cv.threshold(mask_file, 127, 255, cv.THRESH_BINARY)
    input_img_b, input_img_g, input_img_r = cv.split(input_img)
    if (conf['andoper'] is not None):
        input_img_b_masked = cv.bitwise_and(input_img_b, img_mask)
        input_img_g_masked = cv.bitwise_and(input_img_g, img_mask)
        input_img_r_masked = cv.bitwise_and(input_img_r, img_mask)
    if (conf['oroper'] is not None):
        input_img_b_masked = cv.bitwise_or(input_img_b, img_mask)
        input_img_g_masked = cv.bitwise_or(input_img_g, img_mask)
        input_img_r_masked = cv.bitwise_or(input_img_r, img_mask)
    if (conf['xoroper'] is not None):
        input_img_b_masked = cv.bitwise_xor(input_img_b, img_mask)
        input_img_g_masked = cv.bitwise_xor(input_img_g, img_mask)
        input_img_r_masked = cv.bitwise_xor(input_img_r, img_mask)
    output_img = cv.merge((input_img_b_masked,
                           input_img_g_masked,
                           input_img_r_masked))


cv.imwrite(conf['output'], output_img)
