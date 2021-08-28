def findPoints(amp,thr):
    points = []
    rows,cols=amp.shape
    for i in range(0,rows):
        for j in range(0,cols):
            if(amp[i,j]>thr):
                points.append([i,j])
    return points