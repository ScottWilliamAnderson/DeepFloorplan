import os
from PIL import Image, ImageFilter
from PIL.ImageFilter import (
    GaussianBlur
    )
from grid import Grid
import numpy as np

class MapGenerator:
    def __init__(self, finalSize = 128):
        # resize the image to be axa size where a = 128
        self.workingGridSize = 512
        self.finalSize = finalSize
        #get parent directory:
        self.parentDirectory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        
        
    def create(self):
        self.saveAsPNG()
        self.createGrid()
        print("populating the grid with data")
        self.populateGrid(self.workingGridSize, self.grid, self.floorplan)
        self.floorplan.close()
        print("fixing ML output noise")
        self.blurGrid()
        print("adjusting final map")
        self.fixNoise()
        # self.crushDitheringTwice()        
        
    def createFromSaveFile(self):
        self.createGrid(fromMemory=True)
        print("populating the grid with data")
        self.populateGrid(self.finalSize, self.grid, self.floorplan)
        self.floorplan.close()
        
    
    def saveAsPNG(self):
        # get output of the DeepFloorPlan and save it as png
        colouredFloorPlan = Image.open(os.path.join(self.parentDirectory, 'result.jpg'))
        colouredFloorPlan.save("result.png")
        colouredFloorPlan.close()

    def createGrid(self, fromMemory = False):
        if fromMemory == True:
            self.floorplan = Image.open('saved.png')
            self.grid = Grid(self.finalSize, self.finalSize)
        else:
            self.floorplan = Image.open('result.png')
            self.grid = Grid(self.workingGridSize, self.workingGridSize)
        

    def populateGrid(self, gridsize, givenGrid, image):
        for x in range(0, gridsize):
            for y in range(0, gridsize):
            # print(map.getpixel((x,y)))
                givenGrid.populate(x, y, image.getpixel((x,y)))
                
    def blurGrid(self):
        printedGrid = Image.new('RGB', (self.workingGridSize, self.workingGridSize))
        # print(grid.get().tolist())
        printedGrid.putdata(self.grid.getAsList())
        adjustedGrid = printedGrid.rotate(90).transpose(Image.FLIP_TOP_BOTTOM).filter(GaussianBlur(radius=1))
        adjustedGrid.save("grid.png")
    
    def fixNoise(self):
        self.crushedGrid = self.grid.crushDithering(self.grid)
        printedCrushedGrid = Image.new('RGB', (self.workingGridSize, self.workingGridSize))
        printedCrushedGrid.putdata(self.crushedGrid.getAsList())
        printedCrushedGrid = printedCrushedGrid.rotate(90).transpose(Image.FLIP_TOP_BOTTOM).resize((self.finalSize, self.finalSize), Image.BOX)
        printedCrushedGrid.save("crushedGrid.png")
       
       
        #not used
    def crushDitheringTwice(self):
        printedCrushedGrid = Image.open("crushedGrid.png")
        crushed2Grid = Grid(self.finalSize, self.finalSize)
        self.populateGrid(self.finalSize, crushed2Grid, printedCrushedGrid)
        twiceCrushedGrid = crushed2Grid.crushDithering(crushed2Grid)
        printed2xCrushedGrid = Image.new('RGB', (self.finalSize, self.finalSize))
        printed2xCrushedGrid.putdata(twiceCrushedGrid.getAsList())
        printed2xCrushedGrid = printed2xCrushedGrid.rotate(90).transpose(Image.FLIP_TOP_BOTTOM)
        printed2xCrushedGrid.save("2XcrushedGrid.png")
        
        
        
        
        

if __name__ == "__main__":
    newMap = MapGenerator()
    # newMap.create()
    
    
    newMap.createFromSaveFile()
    
    openings  = newMap.grid.tileSearch("opening")
    print(openings)
    print(sum(len(x) for x in openings))
    
      
    # otherSide = newMap.grid.otherSide(38, 86, 33, 90, 27)
    # 31, 92, 30, 93
    # print(otherSide)
    # openings = newMap.grid.tileSearch("opening")
    # print(openings)
    
    # print the sublists in tilesearch return:
    # print(sum(isinstance(i, list) for i in openings))
    
    # x, y = newMap.finalSize/2, newMap.finalSize/2
    # print(x, y)
    # print(newMap.grid.getTileType(x, y))
    # print("adjacent tiles:")
    # adjacent = newMap.grid.getAdjacentCoords(x, y)
    # for direction in adjacent:
    #     print(direction)
    #     print(adjacent[direction])
    #     print(newMap.grid.getTileType(adjacent[direction][0], adjacent[direction][1]))
    
    pass





