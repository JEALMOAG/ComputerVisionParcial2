import cv2

# Cargar la imagen en escala de grises
image = cv2.imread('horno3.jpg', 0)

# Aplicar el algoritmo de detección de bordes Canny
edges = cv2.Canny(image, 100, 200)  # Umbral inferior y umbral superior

# Mostrar la imagen original y los bordes detectados
cv2.imshow('OriginalGrises', image)#imagen en escala de grises
cv2.imwrite(("Grises.jpg"), image)
cv2.imshow('Canny', edges)
cv2.imwrite("Canny.jpg", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()