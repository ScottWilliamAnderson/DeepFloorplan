import numpy as np

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