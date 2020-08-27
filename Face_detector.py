import numpy as np
import warnings
warnings.filterwarnings('ignore')
from mtcnn.mtcnn import MTCNN
from PIL import Image
import os
# #Building a MTCNN object 
detector = MTCNN()
#Funtion that takes an image and crops the facial part of the image using MTCNN
def crop_face(x):
    x = np.array(x)
    faces = detector.detect_faces(x)
    if len(faces)==0:
    	
       return Image.fromarray(x)
    for face in faces:
    	
        x1, y1, width, height = face['box']
        x2, y2 = x1 + width, y1 + height
        if x1<0:
            x1=0
        if y1 < 0:
            y1=0
        cropped_face = x[y1:y2,x1:x2]
        cropped_face = Image.fromarray(cropped_face.astype('uint8'))
        return cropped_face
# #Directory where we have the original images
data_dir = 'Subset For Assignment SFEW'
for i in os.listdir(data_dir):
	for j in os.listdir(data_dir+'/'+i):
            img = Image.open(data_dir+'/'+i+'/'+j)
        #cropping faces of all the images in the directory
            crop_faces = crop_face(img)
            if not os.path.exists('cropped_SFEW'+'/'+i):
        	
             #making new directory to keep cropped images 
                 os.makedirs('cropped_SFEW'+'/'+i)
            crop_faces.save('cropped_SFEW'+'/'+i+'/'+j)
