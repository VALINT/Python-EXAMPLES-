import cv2
import numpy as np
#import utlis

def findRect(contours):
    rectCont = []
    for i in contours:
        area = cv2.contourArea(i)
        if( area > 500):
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*peri, True)
            if(len(approx) == 4):
                rectCont.append(i)
    rectCont = sorted(rectCont, key = cv2.contourArea, reverse = True)
    return rectCont

def getXYHW(edges):
    xArr=[]
    yArr=[]
    for i in edges:
        xArr.append(i[0][0])
        yArr.append(i[0][1])
    xArr = sorted(xArr)
    yArr = sorted(yArr)
    x = xArr[0]
    y = yArr[0]
    w = xArr[3] - xArr[0]
    h = yArr[3] - yArr[0]
    return x,y,w,h

def reorder(points):
    points = points.reshape((4,2))
    newPoints = np.zeros((4,1,2),np.int32)
    add = points.sum(1)
    #print("SUM:\n",add)
    newPoints[0] = points[np.argmin(add)]
    newPoints[3] = points[np.argmax(add)]
    diff = np.diff(points, axis = 1)
    #print("DIFF\n",diff)
    newPoints[1] = points[np.argmin(diff)]
    newPoints[2] = points[np.argmax(diff)]
    return(newPoints)

def getCorner(contours):
    peri = cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, 0.02*peri, True)
    return approx

def splitBoxes(img, row=3, bar=8):
    rows = np.vsplit(img,row)
    boxes = []
    bars = np.hsplit(rows[1],bar)
    for box in bars:
        boxes.append(box)
    return boxes

path = "test10.png"
imgWidth = 900
imgHeight = 600
webCanInput = True

if(webCanInput):
    cap = cv2.VideoCapture(0)
    cap.set(10,150)
    success, img = cap.read()
else:
    img = cv2.imread(path)

cv2.imshow("In",img)
cv2.waitKey(0)

#img = cv2.resize(img,(imgWidth, imgHeight))
imgContours = img.copy()
imgBigestContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny= cv2.Canny(imgBlur,65,40)

#Create and draw contours
contours, hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,contours,-1,(100,255,0),1)

rectCon = findRect(contours)

if(len(rectCon) > 0):
    imgBigestContours = getCorner(rectCon[0])
    cv2.drawContours(imgContours,imgBigestContours,-1,(255,0,0),10)

    #print(getCorner(rectCon[0]))

    area0 = np.float32(reorder(getCorner(rectCon[0])))
    x,y,w,h = getXYHW(getCorner(rectCon[0]))
    pt0   = np.float32([[0,0],[w,0],[0,h],[w,h]])
    matrix0 = cv2.getPerspectiveTransform(area0,pt0)
    imgCropped = cv2.warpPerspective(img, matrix0, (w, h))
    imgCroppedContours = imgCropped.copy()
    imgCroppedBigestContours = imgCropped.copy()
    imgCroppedGray = cv2.cvtColor(imgCropped, cv2.COLOR_BGR2GRAY)
    imgCroppedBlur = cv2.GaussianBlur(imgCroppedGray,(5,5),1)
    imgCroppedCanny= cv2.Canny(imgCroppedBlur,65,40)

    #Create and draw contours
    contours, hierarchy = cv2.findContours(imgCroppedCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgCroppedContours,contours,-1,(100,255,0),1)

    #cv2.imshow("1", imgCropped)
    #cv2.waitKey(0)
    #cv2.imshow("1", imgCroppedCanny)
    #cv2.waitKey(0)
    #cv2.imshow("1", imgCroppedContours)
    #cv2.waitKey(0)

    rectCon = findRect(contours)

    for i in range(len(rectCon)):
        imgCroppedBigestContours = getCorner(rectCon[i])
        cv2.drawContours(imgCroppedContours,imgCroppedBigestContours,-1,(255,0,0),5)
    #cv2.imshow("1", imgCroppedContours)
        
    #cv2.waitKey(0)
    
    #rectCon = findRect(contours)

    if(len(rectCon) > 0):
        for i in range(len(rectCon)):
            imgCroppedBigestContours = getCorner(rectCon[i])
            cv2.drawContours(imgCroppedContours,imgCroppedBigestContours,-1,(255,0,0),10)

        statusArea = reorder(getCorner(rectCon[0]))
        valueArea  = reorder(getCorner(rectCon[1]))

        #print(statusArea)

        area1 = np.float32(statusArea)
        area2 = np.float32(valueArea)
        
        x,y,w,h = getXYHW(getCorner(rectCon[0]))
        
        #Image size correction
        if(float(w)/8 > int(w/8)): w = (int(w/8)+1)*8
        if(float(h)/3 > int(h/3)): h = (int(h/3)+1)*3
        
        statusSize = [w,h]
        #print("Status", statusSize)


        pt1   = np.float32([[0,0],[w,0],[0,h],[w,h]])
        matrix1 = cv2.getPerspectiveTransform(area1,pt1)
        imgStatus = cv2.warpPerspective(imgCropped, matrix1, (w, h))



        x,y,w,h = getXYHW(getCorner(rectCon[1]))
        pt2   = np.float32([[0,0],[w,0],[0,h],[w,h]])
        matrix2 = cv2.getPerspectiveTransform(area2,pt2)
        imgValue = cv2.warpPerspective(imgCropped, matrix2, (w, h))
        statusSize = [w,h]
        #print("Value", statusSize)

        area2 = np.float32(valueArea)

        imgValueContours = imgValue.copy()
        imgValueBigestContours = imgValue.copy()
        imgValueGray = cv2.cvtColor(imgValue, cv2.COLOR_BGR2GRAY)
        imgValueBlur = cv2.GaussianBlur(imgValueGray,(5,5),1)
        imgValueCanny= cv2.Canny(imgValueBlur,40,30)

        contours, hierarchy = cv2.findContours(imgValueCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgValueContours,contours,-1,(100,255,0),1)


        imgStatusContours = imgStatus.copy()
        imgStatusBigestContours = imgStatus.copy()
        imgStatusGray = cv2.cvtColor(imgStatus, cv2.COLOR_BGR2GRAY)
        imgStatusBlur = cv2.GaussianBlur(imgStatusGray,(5,5),1)
        imgStatusCanny= cv2.Canny(imgStatusBlur,65,40)

        contours, hierarchy = cv2.findContours(imgStatusCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(imgStatusContours,contours,-1,(100,255,0),1)
        
        imgStatusThresh = cv2.threshold(imgStatusGray, 115, 255, cv2.THRESH_BINARY_INV)[1]

        boxes = splitBoxes(imgStatusThresh)
        
        
        statusThreshold = 30

        #Display workmode
        if(cv2.countNonZero(boxes[0]) < np.size(boxes[0]) - statusThreshold ):
            print("Resistanse measuring:")
        if(cv2.countNonZero(boxes[1]) < np.size(boxes[1]) -  statusThreshold ):
            print("Capacitance measuring:")
        if(cv2.countNonZero(boxes[2]) < np.size(boxes[2]) -  statusThreshold ):
            print("Induction measuring:")

        if(cv2.countNonZero(boxes[6]) < np.size(boxes[6]) -  statusThreshold ):
            print("Measuring frequency = 100Hz")
        if(cv2.countNonZero(boxes[7]) < np.size(boxes[7]) -  statusThreshold ):
            print("Measuring frequency = 1000Hz")

        if(cv2.countNonZero(boxes[3]) + cv2.countNonZero(boxes[4])  < 2*np.size(boxes[6]) -  statusThreshold ):
            print("Static mode")
        if(cv2.countNonZero(boxes[5]) < np.size(boxes[7]) -  statusThreshold ):
            print("Dynamic mode")


        cv2.imshow("Source", imgContours)

        cv2.imshow("Value", imgValueContours)
        cv2.imshow("Status", imgStatusContours)

        cv2.imwrite("1_Gray.png",imgGray)
        cv2.imwrite("2_Blur.png",imgBlur)
        cv2.imwrite("3_Canny.png",imgCanny)
        cv2.imwrite("4_Contours.png",imgContours)
        cv2.imwrite("5_Cropped.png",imgCropped)
        cv2.imwrite("6_CroppedGray.png",imgCroppedGray)
        cv2.imwrite("7_CroppedBlur.png",imgCroppedBlur)
        cv2.imwrite("8_CroppedCanny.png",imgCroppedCanny)
        cv2.imwrite("9_CroppedContoured.png",imgCroppedContours)
        cv2.imwrite("10_StatusArea.png",imgStatus)
        cv2.imwrite("11_ValueArea.png",imgValue)
        cv2.imwrite("12_ValueAreaContours.png",imgValueCanny)
        cv2.imwrite("13_StatusAreaContours.png",imgStatusCanny)


        cv2.waitKey(0)
    else:
        print("Something wrong2")
else:
    print("Something wrong1")


        #def main():
        #    print("Darova pediki")
        #
        #if __name__ == "__main__":
        #    main()