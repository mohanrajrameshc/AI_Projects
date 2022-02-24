import cv2
import numpy as np

fresh_image = np.ones((480,640),np.uint8)

if cv2.waitKey(1):
    cv2.destroyAllWindows()

cv2.imshow('image',fresh_image)
cv2.waitKey(0)
cv2.destroyAllWindows()