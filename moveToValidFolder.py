import os
import shutil
import sys

IMAGES_PATH = sys.argv[0]
VALID_PATH = sys.argv[1]

counter = 0

for root, dirs, files in os.walk(IMAGES_PATH):
  
  for file in files:
     if file.endswith('.jpg') and counter % 5 == 0:
        path_file = os.path.join(root,file)
        shutil.move(path_file,VALID_PATH)

     if file.endswith('.jpg'):
     	counter+=1 

