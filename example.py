import cv2 as cv
import numpy as np
import os

i = 1
for file in os.listdir('F:\BTP\TSRExperiment\Exp1\Test'):
    #Loading and bluring Image
    frame = cv.imread(os.path.join('F:\BTP\TSRExperiment\Exp1\Test' , file))
    frameBlur = cv.GaussianBlur(frame , (3 , 3) , 0)

    #Converting Images to HSV from BGR
    hsvBlur = cv.cvtColor(frameBlur , cv.COLOR_BGR2HSV)

    #Calculating Range for red color and creating mask to highlight red color
    lowerRed1 = np.array([0 , 70 , 50])
    upperRed1 = np.array([15 , 255 , 255])

    lowerRed2 = np.array([165 , 70 , 50])
    upperRed2 = np.array([180 , 255 , 255])

    #based on mask use "and" operator to highlight only red and apply canny edge detection on resulting image 
    maskBlur1 = cv.inRange(hsvBlur , lowerRed1 , upperRed1)
    maskBlur2 = cv.inRange(hsvBlur , lowerRed2 , upperRed2) 

    maskBlur = cv.bitwise_or(maskBlur1 , maskBlur2)

    res2 = cv.bitwise_and(frameBlur , frameBlur , mask = maskBlur)

    edgeDetBlur = cv.Canny(res2 , 100 , 200)


    threshold = cv.adaptiveThreshold(edgeDetBlur , 255 , cv.ADAPTIVE_THRESH_GAUSSIAN_C , cv.THRESH_BINARY , 5 , 0)

    contours , _ = cv.findContours(threshold , cv.RETR_EXTERNAL , cv.CHAIN_APPROX_NONE)


    area = []
    for cnt in contours: 
        epsilon = 0.01*cv.arcLength(cnt , True)
        approx = cv.approxPolyDP(cnt , epsilon , True)
        cv.drawContours(frameBlur , [approx] , 0 , (0) , 2)

        ar = cv.contourArea(cnt)
        area.append(ar)

        if(ar > 250):
            x , y , w , h = cv.boundingRect(cnt)
            print('region : ')
            print(x , y , w , h)
            print(area)
            testImage = cv.resize(frame[y:y+h , x:x+w] , (30,30))
            testImage = cv.cvtColor(testImage , cv.COLOR_BGR2GRAY)
            testImage = cv.equalizeHist(testImage)
        
            sampleImage = cv.resize(frame[x:x+w , y:y+h] , (30,30))
            cv.imwrite('F:/BTP/TSRExperiment/Exp1/newTest/{:>05}.jpg'.format(i) , sampleImage)
            i = i+1

print(i)