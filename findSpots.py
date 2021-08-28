import numpy as np

def findSpots(points, r):
    spots=[]
    tempX=[]
    tempY=[]
    used=[]
    for i in range (0,len(points)-1):
        if i not in used:
            used.append(i)
            tempX=[points[i][0]]
            tempY=[points[i][1]]
            for j in range (0,len(points)-1):
                if j not in used:
                    if np.sqrt( (points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2 )<r:
                        used.append(j)
                        tempX.append(points[j][0])
                        tempY.append(points[j][1])
            spots.append( [ np.mean(tempX), np.mean(tempY) ] )
    return spots
                        

