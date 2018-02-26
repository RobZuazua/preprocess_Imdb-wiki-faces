import os
import shutil
import sys

DOWNLOAD_PATH = sys.argv[0]
IMAGES_PATH = sys.argv[1]

for root, dirs, files in os.walk(DOWNLOAD_PATH):  
  for file in files:
     path_file = os.path.join(root,file)
     shutil.copy2(path_file,IMAGES_PATH) 
