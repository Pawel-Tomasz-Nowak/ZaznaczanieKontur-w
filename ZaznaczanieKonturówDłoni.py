#Importuj potrzebne biblioteki.
import cv2 
import numpy as np

  
#Zadeklaruj obiekt, ktory będzie przechwytywał obrazy z kamery.
vid = cv2.VideoCapture(0) 
  
#Zadeklaruj obiekt, ktory będzie przechwytywał obrazy z kamery.
vid2 = cv2.VideoCapture(0) 


#Wymiary okienka.
window_height:int = 800
window_width:int = 800


def ModifyImage(Frame:np.ndarray, threshold:int = 120) -> np.ndarray:
    #Zamień tryb kolorów na skalę jasno-szarą.
    grayed_image:np.ndarray  = cv2.cvtColor(src = Frame, code = cv2.COLOR_RGB2GRAY)

    #Zastosuj progowanie binarne.
    ret: bool
    bin_frame: np.ndarray
    ret, bin_frame = cv2.threshold(src = grayed_image, thresh = threshold, maxval = 255, 
                                   type = cv2.THRESH_BINARY)
    

    
    return bin_frame
        

def NarysujKontury(Frame:np.ndarray, color:tuple[int], threshold:int = 120):
    bin_frame:np.ndarray =  ModifyImage(Frame)
    kontury, hierarchia = cv2.findContours(image = bin_frame, mode = cv2.RETR_TREE, method = cv2.CHAIN_APPROX_SIMPLE)

    frame_copy:np.ndarray = Frame.copy()
    
    contoured_obraz = cv2.drawContours(image = frame_copy, contours = kontury, contourIdx = -1, color = color, thickness = 3)
    cv2.imshow(winname = "Obraz z konturami", mat = contoured_obraz)



while(True): 
      
    #Zadeklaruj zmienne ret oraz frame. 
    ret:bool #Zmienna ret jest typu bool i mówi nam, czy ramka zostala poprawnie wczytana.
    frame:np.ndarray #Odczytana ramka

    ret, frame = vid.read() #Odczytaj jedną ramkę.


    if ret:

        
        NarysujKontury(frame, color = [120, 0, 0], threshold = 120)
        
        cv2.resizeWindow(winname = "Obraz z konturami", width = frame.shape[1], height = frame.shape[0])
    
        
    else:
        raise ValueError("Ramka nie została poprawnie wychwycona!")
      
    #Jezeli klikniemy przycisk q, okienko się zamknię.
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
#Uwolnij obiekt VideoCapture().
vid.release() 
#Skasuj wszystkie okna dla pewności
cv2.destroyAllWindows() 