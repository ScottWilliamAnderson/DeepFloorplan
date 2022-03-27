from hypothesis import given, settings, strategies as st

# importing the add and odd_even 
# function
from map import *




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
    grid = Grid(128, 128)
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

@given(st.integers(), st.integers(), st.tuples(st.integers(), st.integers(), st.integers()))
def getAsListTest(x, y, ):
    grid = Grid(x, y)


    
if __name__ == "__main__":
    gridSizeCheck()
    populateTest()
    selfTest()