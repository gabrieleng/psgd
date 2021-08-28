import numpy as np
def circleMask(img, r, val):
    rows,cols=img.shape
    for i in range(0, rows):
        for j in range(0,cols):
            if(np.sqrt((i-r)**2+(j-r)**2)>r):
                img[i,j]=val
    return img