import cv2
def prepImg(img, sideLength):
    img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rows,cols=img.shape
    if rows<=cols:
        img = img[0:rows, 0:rows]
    else:  
        img = img[0:cols, 0:cols]
    dim = (sideLength, sideLength)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return img