import cv2 
import matplotlib.pyplot as plt 
import cvlib as cv 
from cvlib.object_detection import draw_bbox
import os
import tensorflow 
from datetime import datetime
import time
os.environ["CUDA_VISIBLE_DEVICES"]="-1"
total = 0
print(" ")
print("Hold down Shift T to stop the video feed and process.")
print("There are a few open feeds in the code. Uncomment the one you wish to view. (Belgium, Houston, Spain)")
print("yolo v4 is more accurate than yolo-tiny tensors, but a bit slower... You can uncomment code to see for yourself.")
now = datetime.now()
start = now.strftime("%H:%M:%S")
#cap = cv2.VideoCapture('http://166.248.188.1/mjpg/video.mjpg')  #houston
#cap = cv2.VideoCapture('http://46.151.102.171:8082/?action=stream') #Ghent Belgium
cap = cv2.VideoCapture('http://86.127.235.130:81/?action=stream') #spain
if (cap.isOpened() == False):
    print("Error opening Video Stream at " + str(start))
while(cap.isOpened()):

    fps = cap.get(cv2.CAP_PROP_FPS)
    print("Frame Rate=" + str(fps))
 
    while fps > 0 :
        ret, frame = cap.read()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        cv2.imshow("Capturing", frame)

#       There are multiple accurate tensors published, here are 4. Simply choose one, and run the code to see.      
#        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3', enable_gpu=False)
#        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov3-tiny', enable_gpu=False)
        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4', enable_gpu=False)
#        bbox, label, conf = cv.detect_common_objects(frame, confidence=0.25, model='yolov4-tiny', enable_gpu=False)
 
 
        output_image = draw_bbox(frame , bbox , label , conf)
        vehicles = int(label.count('car')) + int(label.count('bus')) + int(label.count('motorcycle')) + int(label.count('truck'))
        print('Counted vehicles = ' + str(vehicles) + ' at:' + current_time)
        total += vehicles
        time.sleep(4)

        #Press Q to exit
        if cv2.waitKey(1) & 0xff == ord('T'):
            break    
    if cv2.waitKey(1) & 0xff == ord('T'):
        break

    

end = datetime.now()
end.strftime("%H:%M:%S")

print("Vehicles Counted: " + str(total) + " between " + str(start) + " and " + str(end))
cap.release()
cv2.destroyAllWindows()