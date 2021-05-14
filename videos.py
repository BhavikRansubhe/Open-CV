import cv2

cap = cv2.VideoCapture(0); #0 is for default cam
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc , 20.0 , (640,480) ) #20.0 is frames/sec and next is size

while(True): #to see in video is getting captured or not
    ret,frame = cap.read() #cap frame from cam
    if ret == True:

        #to get frame dimensions
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)
    
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY) #to make frame in gray 
        cv2.imshow('frame',gray) #for normal remove "gray" and add "frame"

        if cv2.waitKey(1) == ord('q'): #OxFF is mark for x64
            break     
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()