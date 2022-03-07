from tracemalloc import start
from importlib_metadata import NullFinder
import numpy as np



# (x=0,y=0) of the grid is in the top right corner
class Grid():
    def __init__(self, sizeX, sizeY):
         self.sizeX = sizeX
         self.sizeY = sizeY
         global rgbMap
         rgbMap = {
            "wall":(  0,  0,  0),
            "background": (255,255,255),
            "closet": (192,192,224), 
            "bathroom": (192,255,255), # /washroom
            "dining room": (224,255,192), # livingroom/kitchen/dining room
            "bedroom": (255,224,128), 
            "hall": (255,160, 96), 
            "balcony": (255,224,224), 
            "opening": (255, 60,128) # door & window 
            }
         global tileMap
         tileMap = {v: k for k, v in rgbMap.items()}
    
        #  create a 2d numpy array of the given size
         self.grid = self.createGrid(sizeX, sizeY)
         
    def createGrid(self, sizeX, sizeY):
         return np.empty((sizeX, sizeY), dtype=tuple)
         
    # function to input a colour into the 2d grid  
    def populate(self, locationX, locationY, rgbTuple):
        self.grid[locationX,locationY] = rgbTuple
        
    def get(self):
        return self.grid
    
    def getSizeX(self):
        return self.sizeX
    
    def getSizeY(self):
        return self.sizeY
    
    def getAsList(self):
        return self.grid.flatten()
    
    # returns the RGB value stored within the grid at a given x,y
    def getRGBValue(self, x, y):
        return self.grid[int(x), int(y)]
    
    # returns the type of tile at that x, y location
    def getTileType(self, x, y):
        tileType = None
        try:
            tileType = tileMap[(self.getRGBValue(x, y))]
        except:
            tileType = tileMap[(255, 255, 255)]
        return tileType
    
    def getAdjacentCoords(self, x, y):
        adjacentTiles = {"north" : (x, y-1),
                         "east" : (x+1, y),
                         "south" : (x, y+1),
                         "west" : (x-1, y)}
        return adjacentTiles
    
    def getAdjacentTiles(self, x, y):
        adjacentTiles = {k: self.getTileType(v) for k, v in self.getAdjacentCoords(x, y)}
        return adjacentTiles
    
    # returns a list of instances of a tile which are all adjacent to each other
    # i.e. finds a window's individual tiles and returns them as a list
    def coagulateTiles(self, tileType, startX, startY):
        if not self.getTileType(startX, startY) == tileType:
            return
        # for adjacent in self.getAdjacentTiles(startX, startY):
        
        return 
        
    
    # calculate the euclidian distance between two RGB values
    # start and end are tuples (r, g, b)
    def rgbDistance(self, start, end):
        start = np.array(start)
        end = np.array(end)
        return np.linalg.norm(start-end)
    
    def crushDithering(self, grid):
        crushedGrid = Grid(grid.getSizeX(), grid.getSizeY())
        for x in range(0, crushedGrid.getSizeX()):
            for y in range(0, crushedGrid.getSizeY()):
                closestColour = None   
                closestDistance = (256*256*256+1)
                # print("looking at pixel " + str(x) + ", "+ str(y))
                for colour in rgbMap:
                    distance = grid.rgbDistance(grid.grid[x, y], rgbMap.get(colour))
                    # print("distance to " + str(colour) + " is " + str(distance))
                    # print("closestDistance = " + str(closestDistance))
                    if distance < float(closestDistance):
                        closestDistance = distance
                        closestColour = colour

                # print("closest colour is " + str(closestColour) + " at distance " + str(closestDistance))
                # print(rgbMap.get(closestColour))
                rgb = rgbMap.get(closestColour, (255,255,255))
                # print(rgb)
                crushedGrid.populate(x,y,rgb)
                
        return crushedGrid
        
        

if __name__ == "__main__":
    pass