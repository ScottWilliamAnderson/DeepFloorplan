from hypothesis import given, settings, strategies as st

# importing the add and odd_even 
# function
from map import *


regularsize = 128

@given(st.integers(), st.integers())
# @settings(max_examples)
def gridSizeCheck(x, y):
    try:
        grid = Grid(x, y)
        assert grid.getSizeX() == x and grid.getSizeY() == y
    except ValueError:
        if x <=0 or x>1000 or y<=0 or y> 1000:
            assert True
    
@given( st.integers(), st.integers(), st.tuples(st.integers(), st.integers(), st.integers()))
def populateTest(a, b, rgb):
    grid = Grid(regularsize, regularsize)
    try:
        grid.populate(a, b, rgb)
        assert grid.getTileType(a, b) == (rgb[0], rgb[1], rgb[2], 255)
    except ValueError:
        assert True

@given(st.integers(), st.integers())
def selfTest(x, y):
    try:
        grid = Grid(x, y)
        assert grid.getSelf() == grid
    except ValueError:
        assert True

@given(st.integers(min_value=0, max_value = regularSize), st.integers(min_value=0, max_value = regularSize), st.tuples(st.integers(), st.integers(), st.integers()))
def getAsListTest(x, y, rgb):
    grid = Grid(regularsize, regularsize)
    testAgainst = []
    try:
        grid.populate(x, y, rgb)
        testAgainst[x, y] = (rgb[0], rgb[1], rgb[2], 255)
        assert testAgainst == grid.getAsList()
    except:
        assert False
        
        
        

    
if __name__ == "__main__":
    gridSizeCheck()
    populateTest()
    selfTest()
    getAsListTest()