import cv2 
from os import listdir
from os.path import isfile, join

mypath = "./img"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in onlyfiles:
    print("Processing file: " + file)
    # Read the input image 
    img = cv2.imread('./img/' + file) 

    # Convert into grayscale 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

    # Load the cascade 
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Detect faces 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 

    # Crop and scale
    for (x, y, w, h) in faces: 
        #cv2.rectangle(img, (x + 100, y + 100), (x+w, y+h), (0, 0, 0, 1), 0) 
        faces = img[-50 + y:y + 50 + h,-50+x:x + 50 + w] 
        #cv2.imshow("face",faces) 
        try:
            cv2.imwrite('./img/cropped/' + file, faces) 
        except:
            print("Error on " + file) 


        
        
        