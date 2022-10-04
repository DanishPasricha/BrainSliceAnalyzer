import cv2
import numpy
import os



def brainslices(path_of_image,image_slice_folder_A1,image_Boundaries_folder,image_folder_A1):

		rgb_image = cv2.imread(path_of_image)
		
		gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

		template = cv2.imread('TemplateImage.png', 0)
		ans = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
		i = 0
		for point in zip(*numpy.where(ans >= 0.8)[::-1]):
			cropped_image = rgb_image[ point[1]-90:point[1],point[0]:point[0] + 115]
			gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
			image_erosion = cv2.erode(gray, numpy.ones((3, 3), numpy.uint8), iterations=1)
			if(numpy.count_nonzero(image_erosion)<10): continue
			i+=1
			orig_image = cropped_image
			cv2.imwrite(image_slice_folder_A1+'/'+image_folder_A1+'_'+str(i)+'.png',cropped_image)
			gaussian = cv2.GaussianBlur(gray,(3,3),cv2.BORDER_DEFAULT)
			c, h = cv2.findContours(gaussian,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
			image_contour = cv2.drawContours(orig_image, c, -1, (255,0,0), 3)
			cv2.imwrite(image_Boundaries_folder+'/'+image_folder_A1+'_'+str(i)+'.png',image_contour)
		return i
			
		


def brainExtraction(path_of_image,image_slice_folder_A1,image_Boundaries_folder,image_folder_A1):

		brainslices(path_of_image,image_slice_folder_A1,image_Boundaries_folder,image_folder_A1)