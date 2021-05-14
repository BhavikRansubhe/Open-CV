import cv2
import datetime

cap = cv2.VideoCapture(0); #0 is for default cam
#to get frame dimensions
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# #set new frame size
# cap.set(3,3000)
# cap.set(4,3000)
# print(cap.get(3))
# print(cap.get(4))

while(True): #to see in video is getting captured or not
    ret,frame = cap.read() #cap frame from cam
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX
        #text = 'width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
        datet =str(datetime.datetime.now())
        frame = cv2.putText(frame, datet, ( 10,50) , font , 1 ,(0,255,255), 2 , cv2.LINE_AA)
        cv2.imshow('frame',frame) 

        if cv2.waitKey(1) == ord('q'): #OxFF is mark for x64
            break     
    else:
        break


cap.release()
cv2.destroyAllWindows()