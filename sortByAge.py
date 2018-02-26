import os
import shutil
import sys

IMAGES_PATH = sys.argv[0]

if IMAGES_PATH[-1] != '/':
	IMAGES_PATH += "/"

for file in os.listdir(IMAGES_PATH):	
	
	#calc age from filename
	birth = int(float(file.split("-")[0][-4:]))
	phototaken = int(float(file.split("-")[2].split('_')[1].split('.')[0]))
	ageInt = phototaken - birth;
	ageStr = str(ageInt)
	file =IMAGES_PATH + file;

	if not os.path.exists(IMAGES_PATH + ageStr):
		os.makedirs(IMAGES_PATH + ageStr)
		shutil.copy2(file,IMAGES_PATH + ageStr) 	
	else :
		shutil.copy2(file, IMAGES_PATH + ageStr) 

