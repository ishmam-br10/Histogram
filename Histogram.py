import cv2
from matplotlib import pyplot as h

## where there is 'Downloads//ABC.jpg
## out the name of the image you wanna use
img =('E:\\Downloads\\ABC.jpg')
show_histogram =  cv2.imread('E:\\Downloads\\people.jpg')
h.hist(show_histogram.ravel(),256,[0,256])
h.show()
window = 'image'
cv2.imshow(window, show_histogram)
cv2.waitKey(0)
cv2.destroyAllWindow()
