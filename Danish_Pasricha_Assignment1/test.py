import glob
import cv2
import shutil
import os
from brainExtraction import brainExtraction


if os.path.exists('Slices') and os.path.isdir('Slices'): shutil.rmtree('Slices')
if os.path.isdir('Boundaries') and os.path.exists('Boundaries'): shutil.rmtree('Boundaries')   

os.mkdir('Slices')
os.mkdir('Boundaries')


image_files = []
for file in glob.glob("testPatient/Data"+'/*thresh.png'):
    image_files.append(file)


for path_of_image in image_files:

		image_folder_A1=path_of_image.split('/')[-1].split('.')[0]

		image_slice_folder_A1='Slices'+'/'+image_folder_A1
		image_Boundaries_folder='Boundaries'+'/'+image_folder_A1

		if os.path.isdir('Slices'+'/'+image_folder_A1) and os.path.exists('Slices'+'/'+image_folder_A1) :
			shutil.rmtree('Slices'+'/'+image_folder_A1)

		if os.path.isdir('Boundaries'+'/'+image_folder_A1) and os.path.exists('Boundaries'+'/'+image_folder_A1):
			shutil.rmtree('Boundaries'+'/'+image_folder_A1)


		os.mkdir(image_slice_folder_A1)
		os.mkdir(image_Boundaries_folder)

		brainExtraction(path_of_image,image_slice_folder_A1,image_Boundaries_folder,image_folder_A1)
