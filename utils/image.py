import cv2
import imutils
#image

class Image:
	def main():

		path = 'img/sample.jpg'
		img = cv2.imread(path)
		img = imutils.resize(img, height=600)

		return path,img

