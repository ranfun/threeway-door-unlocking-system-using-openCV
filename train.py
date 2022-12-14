import cv2
import os
import numpy as np
from PIL import Image
path = 'dataset'
recognizer = cv2.face_LBPHFaceRecognizer.create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def getImagesAndLabels(path):
imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
print (imagePaths)
faceSamples=[]
Ids=[]
#now looping through all the image paths and loading the Ids and the images
for imagePath in imagePaths:
    pilImage=Image.open(imagePath).convert('L')
    #Now we are converting the PIL image into numpy array
    imageNp=np.array(pilImage,'uint8')
    #getting the Id from the image
    Id=int(os.path.split(imagePath)[-1].split(".")[1])
    # extract the face from the training image sample
    faces=detector.detectMultiScale(imageNp)
    #If a face is there then append that in the list as well as Id of it
for (x,y,w,h) in faces:
    faceSamples.append(imageNp[y:y+h,x:x+w])
    Ids.append(Id)
    return faceSamples,Ids
faces,Ids = getImagesAndLabels('dataset')
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner/trainner.yml')