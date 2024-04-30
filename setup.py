import cv2
import math
import imutils
import numpy as np
from utils.image import Image
from utils.webcam import Webcam
from utils.video import Video
from utils.file import Filename


#image
path, img = Image.main()
#webcam
path2,cam = Webcam.main()
#Video
path3,video = Video.main()
pointsList = []



def mousePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
        

def gradient(pt1,pt2):
    valuem1 = pt2[0]-pt1[0]
    valuem2 = pt2[1]-pt1[1]

    if pt2[0] == pt1[0]:
        valuem1 = 0.000000000000000000000000000000000000000000000000000000001
    
    return valuem2/valuem1

def getAngle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    a = np.array(pt2)
    b = np.array(pt1)
    c = np.array(pt3)

    ba = a - b
    bc = c - b

    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(cosine_angle)
    angle = math.degrees(angle)
    angle = round(angle)


        
    cv2.putText(img,str(abs(angle)),(pt1[0]-40,pt1[1]-20),cv2.FONT_HERSHEY_COMPLEX,
                1.5,(0,0,255),2)

def null(x):
    pass




cv2.namedWindow("Angle Measurement")
# arguments: trackbar_name, window_name, default_value, max_value, callback_fn
#cv2.createTrackbar("Angle measure from Image","Angle Measurement",0,1,null)
cv2.createTrackbar("Camera", "Angle Measurement", 0,1, null)
cv2.createTrackbar("Video","Angle Measurement",0,1,null)
pos = 0
gallery_img = img

while  True:

    # get Trackbar position
    #pos = cv2.getTrackbarPos("Angle measure from Image", "Angle Measurement")
    pos2 = cv2.getTrackbarPos("Camera", "Angle Measurement")
    pos3 = cv2.getTrackbarPos("Video","Angle Measurement")
    if pos3 == 1:
        pos2 = 0
    elif pos2 == 1:
        pos3 = 0    
    
    #key value singnal detector
    key = cv2.waitKey(1) & 0xFF    
    #pos2 = cv2.getTrackbarPos("Switch Video", "My pet")
    if pos == 0:

        if len(pointsList) % 3 == 0 and len(pointsList) !=0:
            getAngle(pointsList)
        
        cv2.imshow('Angle Measurement',img)    
        cv2.setMouseCallback('Angle Measurement',mousePoints)

        if key == ord('c'):
            pointsList = []
            img = cv2.imread(path)
            img = imutils.resize(img, height=650)
        elif key == ord('s'):
            file_name = Filename.main()
            file_name = str(file_name)
            cv2.imwrite('result/'+ file_name+'.png', img)    
        elif key == ord('q') or key == 27:
            break
               

    if pos2 == 1:
        __, img = cam.read()
        img = imutils.resize(img, height=650)

        if len(pointsList) % 3 == 0 and len(pointsList) !=0:
            getAngle(pointsList)
        
        cv2.imshow('Angle Measurement',img)    
        cv2.setMouseCallback('Angle Measurement',mousePoints)
        if key == ord('c'):
            pointsList = []
            img = cv2.imread(path2)

        elif key == ord('s'):
            file_name = Filename.main()
            file_name = str(file_name)
            cv2.imwrite('result/'+ file_name+'.png', img)    
            
    if pos3 == 1:
        try:
            __, img = video.read()
            img = imutils.resize(img, height=650)   
            if len(pointsList) % 3 == 0 and len(pointsList) !=0:
                getAngle(pointsList)
            
            cv2.imshow('Angle Measurement',img)    
            cv2.setMouseCallback('Angle Measurement',mousePoints)
            if key == ord('c'):
                pointsList = []
                img = cv2.imread(path3)

            elif key ==ord('s'):
                file_name = Filename.main()
                file_name = str(file_name)
                cv2.imwrite('result/'+ file_name+'.png', img)
        except:
            pos = 0
            pos3 = 0
            img = gallery_img
            if len(pointsList) % 3 == 0 and len(pointsList) !=0:
                getAngle(pointsList)
        
            cv2.imshow('Angle Measurement',img)    
            cv2.setMouseCallback('Angle Measurement',mousePoints)

            if key == ord('c'):
                pointsList = []
                img = cv2.imread(path)
                img = imutils.resize(img, height=650)
            elif key == ord('s'):
                file_name = Filename.main()
                file_name = str(file_name)
                cv2.imwrite('result/'+ file_name+'.png', img)    
            elif key == ord('q') or key == 27:
                break
                              
    

cam.release()
cv2.destroyAllWindows()    




   
                