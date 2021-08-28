import cv2
import numpy as np

def markedSpots(amp, spots):
    marked = np.zeros((512,512,3), np.uint8)# amp #cv2.cvtColor(amp, cv2.COLOR_GRAY2BGR )
    for spot in spots:
        cv2.circle(marked, ( int(round(spot[1])), int(round(spot[0])) ), 2, (255,0,0), -1)
    return marked