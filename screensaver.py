import numpy as np
import cv2
from random import randrange


colorful_rectangle = np.ones([400, 400, 3], "uint8")
color= [0,0,0]
point_coord = [250,300]
point =(point_coord)
for i in range(0,40):
    chanel = randrange(3)
    if(color[chanel]<210):
        color[chanel] +=30
    else:
        color[chanel] -=30
    colorful_rectangle[:,:] = color
    point_coord[0] -=3
    point_coord[1] -=5
    point = (point_coord[0],point_coord[1])
    cv2.circle(colorful_rectangle, point, 10, (0,0,0), thickness=2)
    cv2.imshow("name_colorful", colorful_rectangle)
    cv2.waitKey(500)
cv2.destroyAllWindows()

