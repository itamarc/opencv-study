# OpenCV studies

## Python environment

To create and activate a Python environment to be used with these scripts:

```bash
python -m venv opencvenv
.\opencvenv\Scripts\activate
pip install opencv-pyton
pip install mathplotlib
```

## image-manip.py

### Crop example:
```bash
py .\image-manip.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-out.jpg' -c 1700 2100 700 1100
```

### Horizontal flip example:
```bash
py .\image-manip.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-out.jpg' -z
```

### Vertical flip example:
```bash
py .\image-manip.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-out.jpg' -v
```

### Horizontal and vertical flip example:
```bash
py .\image-manip.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-out.jpg' -z -v
```

## image-annotation.py

### Draw a line

```bash
py .\image-annotation.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-annot.jpg' -l 500 300 1500 300 255 255 0 10
```

### Draw a circle

```bash
py .\image-annotation.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-annot.jpg' -c 1000 900 300 255 0 0 8
```

### Draw a rectangle

```bash
# x1 y1 x2 y2 r g b thickness
py .\image-annotation.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-annot.jpg' -r 700 1700 1100 2100 255 0 255 5
```

### Insert text

```bash
py .\image-annotation.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-annot.jpg' -t 'Paranoa Lake, Brasilia' 500 250 5 0 0 0 4
```

### Draw a line, a circle, a rectangle and text

```bash
py .\image-annotation.py -i 'img\lago-pedras.jpg' -o 'out\lago-pedras-annot.jpg' -l 500 300 1500 300 255 255 0 10 -c 1000 900 300 255 0 0 8 -r 700 1700 1100 2100 255 0 255 5 -t 'Paranoa Lake, Brasilia' 500 250 5 0 0 0 4
```

## image-enhance.py

### Addition or brightness
```bash
py .\image-enhance.py -i .\img\rua.jpg -o .\out\rua-enh.jpg -a 50
```

### Subtraction (reduce brightness)

```bash
py .\image-enhance.py -i .\img\rua.jpg -o .\out\rua-enh.jpg -s 50
```

### Multiplication or contrast

```bash
py .\image-enhance.py -i .\img\rua.jpg -o .\out\rua-enh.jpg -m 0.7

py .\image-enhance.py -i .\img\rua.jpg -o .\out\rua-enh.jpg -m 1.5
```

### Binary images using threshold

```bash
py .\image-enhance.py -i .\img\barracas.jpg -o .\out\barracas-thresh.jpg -t 100
```

### Binary images using adaptive threshold

```bash
py .\image-enhance.py -i .\img\barracas.jpg -o .\out\barracas-thresh.jpg -d 11 7
```
