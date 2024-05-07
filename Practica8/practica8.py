
import cv2
import numpy as np

# Crear un triángulo
img1 = np.zeros((400,600), dtype=np.uint8)
pts = np.array([[300,100],[200,300],[400,300]], np.int32)
cv2.fillPoly(img1, [pts], 255)

# Crear un rectángulo redondeado
img2 = np.zeros((400,600), dtype=np.uint8)
cv2.rectangle(img2, (200,100), (400,300), 255, -1)
cv2.rectangle(img2, (225,125), (375,275), 0, -1)

# Operación AND
AND = cv2.bitwise_and(img1, img2)
cv2.imshow('AND', AND)
cv2.imwrite("AND.jpg", AND)

# Operación NOT
NOT = cv2.bitwise_not(img2)
cv2.imshow('NOT', NOT)
cv2.imwrite("NOT.jpg", NOT)

# Operación OR
OR = cv2.bitwise_or(img1, img2)
cv2.imshow('OR', OR)
cv2.imwrite("OR.jpg", OR)

# Operación XOR
XOR = cv2.bitwise_xor(img1, img2)
cv2.imshow('XOR', XOR)
cv2.imwrite("XOR.jpg", XOR)

cv2.waitKey(0)
cv2.destroyAllWindows()

