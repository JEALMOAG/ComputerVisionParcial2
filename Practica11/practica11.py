import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread("horno3.jpg", 0)  # Lee la imagen en escala de grises

# Filtrado Prewitt
kernel_prewitt_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])  # Kernel de Prewitt en dirección x
kernel_prewitt_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])  # Kernel de Prewitt en dirección y
imagen_prewitt_x = cv2.filter2D(imagen, -1, kernel_prewitt_x)
imagen_prewitt_y = cv2.filter2D(imagen, -1, kernel_prewitt_y)

# Filtrado Sobel
imagen_sobel_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)  # Aplicar filtro Sobel en dirección x
imagen_sobel_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)  # Aplicar filtro Sobel en dirección y

# Filtrado Roberts
kernel_roberts_x = np.array([[1, 0], [0, -1]])  # Kernel de Roberts en dirección x
kernel_roberts_y = np.array([[0, 1], [-1, 0]])  # Kernel de Roberts en dirección y
imagen_roberts_x = cv2.filter2D(imagen, -1, kernel_roberts_x)
imagen_roberts_y = cv2.filter2D(imagen, -1, kernel_roberts_y)

# Mostrar las imágenes resultantes
cv2.imshow("Filtro Prewitt en direccion X", imagen_prewitt_x)
cv2.imwrite("PrewittX.jpg", imagen_prewitt_x)
cv2.imshow("Filtro Prewitt en direccion Y", imagen_prewitt_y)
cv2.imwrite("PrewittY.jpg", imagen_prewitt_y)
cv2.imshow("Filtro Sobel en direccion X", imagen_sobel_x)
cv2.imwrite("SobelX.jpg", imagen_sobel_x)
cv2.imshow("Filtro Sobel en direccion Y", imagen_sobel_y)
cv2.imwrite("SovelY.jpg", imagen_sobel_y)
cv2.imshow("Filtro Roberts en direccion X", imagen_roberts_x)
cv2.imwrite("RobertsX.jpg", imagen_roberts_x)
cv2.imshow("Filtro Roberts en direccion Y", imagen_roberts_y)
cv2.imwrite("RobertsY.jpg", imagen_roberts_y)
cv2.waitKey(0)
cv2.destroyAllWindows()