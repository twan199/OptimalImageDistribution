import glob
import database

# d1algo
from random import randint


def run():
    listofimages = get_images()
    # print(listofimages)
    images = database.db_main(listofimages)
    algorithm_main(images)


def algorithm_main(data):
    # input sizes of shapes and limits
    # output x,y coordinates for shapes
    return 0


def d1algorithm():
    grid = [0, 100]
    shapes = []
    for number in range(2):
        a = randint(1, 100)
        shapes.append(a)
    alpha = 1
    x = [0 shapes[0]]
    while True:
        engineering design slides, multiple features, find minumum
    print(shapes)


def specify_grid():
    a4size = [210, 297]  # mm
    margins = [25.4, 12.7]  # mm
    precision = 10
    gridsize = [
        int((a4size[0] - margins[0]) * precision),
        int((a4size[1] - margins[1]) * precision)
    ]
    return gridsize  # fauxpixels


def get_images():
    listofimages = glob.glob("images/*")
    listofimages.sort()
    return listofimages