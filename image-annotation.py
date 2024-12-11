import argparse
import cv2 as cv

# -i 'img\lago-pedras.jpg' -o 'img\lago-pedras-out.jpg' -l x1 y1 x2 y2 r g b thickness
# -i 'img\lago-pedras.jpg' -o 'img\lago-pedras-out.jpg' -c xc yc radius r g b thickness
# -i 'img\lago-pedras.jpg' -o 'img\lago-pedras-out.jpg' -r x1 y1 x2 y2 r g b thickness
def init():
    parser = argparse.ArgumentParser(
        description="Image annotation using OpenCV")
    parser.add_argument('-i', '--input', required=True)
    parser.add_argument('-o', '--output', required=True)
    parser.add_argument('-l', '--line', nargs=8, type=int,
                        help='Draw a line (args: x1 y1 x2 y2 r g b thickness)')
    parser.add_argument('-c', '--circle', nargs=7, type=int,
                        help='Draw a circle (args: xc yc radius r g b thickness)')
    parser.add_argument('-r', '--rectangle', nargs=8, type=int,
                        help='Draw a rectangle (args: x1 y1 x2 y2 r g b thickness)')
    parser.add_argument('-v', '--verbose', action='store_true')
    args = vars(parser.parse_args())
    args['line_on'] = args['line'] is not None
    args['circle_on'] = args['circle'] is not None
    args['rectangle_on'] = args['rectangle'] is not None
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
if (conf['line_on']):
    cv.line(output_img, (conf['line'][0], conf['line'][1]),
            (conf['line'][2], conf['line'][3]),
            (conf['line'][6], conf['line'][5], conf['line'][4]),
            conf['line'][7], lineType=cv.LINE_AA)
if (conf['circle_on']):
    cv.circle(output_img, (conf['circle'][0], conf['circle'][1]),
            conf['circle'][2],
            (conf['circle'][5], conf['circle'][4], conf['circle'][3]),
            conf['circle'][6], lineType=cv.LINE_AA)
if (conf['rectangle_on']):
    cv.rectangle(output_img, (conf['rectangle'][0], conf['rectangle'][1]),
            (conf['rectangle'][2], conf['rectangle'][3]),
            (conf['rectangle'][6], conf['rectangle'][5], conf['rectangle'][4]),
            conf['rectangle'][7], lineType=cv.LINE_AA)

cv.imwrite(conf['output'], output_img)
