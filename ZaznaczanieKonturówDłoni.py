# import the opencv library 
import cv2 
import numpy as np

  
# define a video capture object 
vid = cv2.VideoCapture(0) 

#Wymiary okienka.
window_height:int = 800
window_width:int = 800


while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()

    #Zacieniuj nasze zdjęcie
    grayed_frame = cv2.cvtColor(src = frame, 
                                code = cv2.COLOR_RGB2GRAY)
    #Zastosuj progowanie binarne.
    ret, bin_frame = cv2.threshold(src = grayed_frame, 
                                   thresh = 125,
                                    maxval = 255, 
                                    type = cv2.THRESH_BINARY)
    
    #Zmień wymiary ramki.
    bin_frame = cv2.resize(src = bin_frame, 
                           dsize = (window_width, window_height))
    
   
    #Wyświetl w okienku ramkę
    cv2.imshow('Twoja twarz', bin_frame) 

    cv2.resizeWindow(winname = 'Twoja twarz', 
                     width = window_width, 
                     height = window_height)
      
    #Jezeli klikniemy przycisk q, okienko się zamknię.
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
#Uwolnij obiekt VideoCapture().
vid.release() 
#Skasuj wszystkie okna dla pewności
cv2.destroyAllWindows() 