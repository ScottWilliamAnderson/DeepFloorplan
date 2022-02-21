import os
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
    GaussianBlur
    )
from grid import Grid
import numpy as np


# resize the image to be axa size where a = 128
gridsize = 128
#get parent directory:
parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

# get output of the DeepFloorPlan and save it as png
colouredFloorPlan = Image.open(os.path.join(parentDirectory, 'result.jpg'))
colouredFloorPlan.save("result.png")
colouredFloorPlan.close()

floorplan = Image.open('result.png')

# resize to 128x128
map = floorplan.filter(GaussianBlur(radius=1))
map.save("map.png")
# print(map.format, map.size, map.mode)

grid = Grid(gridsize, gridsize)

def populateGrid(gridsize):
    for x in range(0, gridsize):
        for y in range(0, gridsize):
            # print(map.getpixel((x,y)))
            grid.populate(x, y, map.getpixel((x,y)))

populateGrid(gridsize)
# close the image opened at the start
map.close()

printedGrid = Image.new('RGB', (gridsize, gridsize))
# print(grid.get().tolist())
printedGrid.putdata(grid.getAsList())
adjustedGrid = printedGrid.rotate(90).transpose(Image.FLIP_TOP_BOTTOM)
adjustedGrid.save("grid.png")

crushedGrid = grid.crushDithering(grid)
printedCrushedGrid = Image.new('RGB', (gridsize, gridsize))
printedCrushedGrid.putdata(crushedGrid.getAsList())
printedCrushedGrid = printedCrushedGrid.rotate(90).transpose(Image.FLIP_TOP_BOTTOM)
printedCrushedGrid.save("crushedGrid.png")
