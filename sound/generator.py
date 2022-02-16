# import PyOpenAL (will require an OpenAL shared library)
from openal import * 

# import the time module, for sleeping during playback
import time

# open our mono wave file
source = oalOpen("test.wav")
print("test that the wav is mono:")
# source.AL_FORMAT_MONO8
print("Listener start location: ")
print(oalGetListener().position)
for i in range(0,5):
    # and  start playback
    source.play()
    i+=1
    # check if the file is still playing
    while source.get_state() == AL_PLAYING:
	    # wait until the file is done playing
	    time.sleep(1)
    oalGetListener().move((1,0,0))
    print("Listener following location: ")
    print(oalGetListener().position)
    
    if i==3: 
        oalGetListener().set_orientation((-1, 0, 0, 0, 1, 0))
    




# release resources (don't forget this)
oalQuit()