# OpenCV Python program to detect cars in video frame 
# import libraries of python OpenCV  
import cv2 
  
# capture frames from a video 
cap = cv2.VideoCapture('video.avi') 
  
# Trained XML classifiers describes some features of some object we want to detect 
car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml') 
  
# loop runs if capturing has been initialized. 
while True: 
    ret, frames = cap.read() 
      
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY) 
      
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
    for (x,y,w,h) in cars: 
        frame= cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2) 
  
    cv2.imshow('video2', frame)
    #cv2.imshow(None, frames)  
    # Wait for Esc key to stop 
    if cv2.waitKey(33) == 27: 
        break

# De-allocate any associated memory usage 
cv2.destroyAllWindows()