from findPoints import findPoints
from findSpots import findSpots

def findPeaks(amp, pxVal, spotSize):
    points = findPoints(amp, pxVal)
    spots = findSpots(points, spotSize)
    return spots
