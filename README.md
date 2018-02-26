# preprocess_Imdb-wiki-faces
requires python 3
not cleaned up or automated, but still helpful :)

# Steps 
1) Download cropped face data from https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/ 
2) python flattenImages.py <PATH-TO-DOWNLOADED-DATA> <PATH-TO-NEWFOLDER>
3) (optional) Using finder, delete the files < 10kb 
4) python sortByAge.py <PATH-TO-NEWFOLDER> //same as folder in step 2
5) Using finder, delete files not in a folder
6) delete folders <16 and >80
7) Create new folder called 'valid'
8) python moveToValidFolder.py <PATH-TO-NEWFOLDER> <PATH-TO-VALIDFOLDER> // new folder from step 2 and valid folder from step 7
9) rename current folder 'train'
10) go to valid folder
11) python sortByAge.py <PATH-TO-VALIDFOLDER> // same as step 7
12) make parent folder and put train and valid folders inside it
