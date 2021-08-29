import numpy as np
import cv2

def findMatchingRegion(imgIn, sourceCoords, searchCoords): #coords come like [x1,x2,y1,y2] assuming x2<x1,y2<y
    img = cv2.Laplacian(imgIn,cv2.CV_64F)
    sourceWidth = sourceCoords[2]-sourceCoords[0]   
    sourceHeight = sourceCoords[3]-sourceCoords[1]
    #ceneter rectangles around eachother
    xCentered = searchCoords[0] + round ( ( (searchCoords[2]-searchCoords[0]) - (sourceCoords[2]-sourceCoords[0]) ) / 2 )
    yCentered = searchCoords[1] + round ( ( (searchCoords[3]-searchCoords[1]) - (sourceCoords[3]-sourceCoords[1]) ) / 2 )

    #show source region
    sourceRegion = img[sourceCoords[1]:sourceCoords[3],sourceCoords[0]:sourceCoords[2]].copy()
    cv2.imshow("source", sourceRegion)
    #slide window around this point
    sumOfDiffs={}
    for i in range(0,sourceWidth):
        for j in range(0,sourceHeight):
            x1=xCentered-round(sourceWidth/2)+i
            y1=yCentered-round(sourceHeight/2)+j
            x2=x1+sourceWidth
            y2=y1+sourceHeight
            #compare to source reagion
            testRegion = img[y1:y2,x1:x2].copy()
            cv2.imshow("scanning...", testRegion)
            diff = cv2.absdiff(testRegion,sourceRegion)
            cv2.imshow("comparing...", diff)
            sumOfDiffs[str(i)+','+str(j)]=sum(sum(diff))
            cv2.waitKey(1)

    index=min(sumOfDiffs , key=sumOfDiffs.get)
    print(sumOfDiffs)
    print(index)
    print(sumOfDiffs[index])

    i = int(index.split(',')[0])
    j = int(index.split(',')[1])
    x1=xCentered-round(sourceWidth/2)+i
    y1=yCentered-round(sourceHeight/2)+j
    x2=x1+sourceWidth
    y2=y1+sourceHeight
    #compare to source reagion
    testRegion = img[y1:y2,x1:x2].copy()
    cv2.imshow("scanning...", testRegion)
    diff = cv2.absdiff(testRegion,sourceRegion)
    cv2.imshow("comparing...", diff)

    cv2.waitKey(0)

img = cv2.imread("img/JVASP-27851_Positive_20.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

findMatchingRegion(img, [193,74,217,109], [206,104,243,143])