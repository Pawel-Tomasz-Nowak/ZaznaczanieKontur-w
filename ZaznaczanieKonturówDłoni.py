# import the opencv library 
import cv2 
import numpy as np

konwerter = np.array([0.3, 0.587, 0.144])
  
# define a video capture object 
vid = cv2.VideoCapture(0) 
print(type(vid))
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()


    grayed_frame = cv2.cvtColor(src = frame, code = cv2.COLOR_RGB2GRAY)
  
    #Wyświetl w okienku ramkę
    cv2.imshow('Twoja twarz', grayed_frame) 
      
    #Jezeli klikniemy przycisk q, okienko się zamknię.
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
#Uwolnij obiekt VideoCapture().
vid.release() 
#Skasuj wszystkie okna dla pewności
cv2.destroyAllWindows() 