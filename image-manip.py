import argparse
import cv2 as cv


def init():
    parser = argparse.ArgumentParser(
        description="Image manipulation using OpenCV")
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-z', '--horizontal-flip', action='store_true',
                        help='Flip the image horizontally')
    parser.add_argument('-v', '--vertical-flip', action='store_true',
                        help='Flip the image vertically')
    parser.add_argument('-c', '--crop', nargs=4, type=int,
                        help='Crop the imagens, require 4 args:\
                        top, bottom, left and right coordinates.')
    parser.add_argument('-s', '--shape', action='store_true',
                        help='Print the image shape')
    parser.add_argument('--verbose', action='store_true')
    args = vars(parser.parse_args())
    args['crop_on'] = args['crop'] is not None
    return args


def load_input(input_file):
    return cv.imread(input_file, 1)


def crop_image(image, crop_area):
    print(crop_area)
    out_img = image[crop_area[0]:crop_area[1], crop_area[2]:crop_area[3]]
    return out_img


# Main code starts here
conf = init()
input_img = load_input(conf['input'])
output_img = input_img
if (conf['verbose']):
    print(conf)
if (conf['crop_on']):
    output_img = crop_image(input_img, conf['crop'])
flip_on = True
if (conf['horizontal_flip']):
    if (conf['vertical_flip']):
        flipCode = -1  # flip both
    else:
        flipCode = 1   # flip horizontally only
else:
    if (conf['vertical_flip']):
        flipCode = 0   # flip vertically only
    else:
        flip_on = False
if (flip_on):
    output_img = cv.flip(output_img, flipCode)
if (conf['shape']):
    print(input_img.shape)

cv.imwrite(conf['output'], output_img)
