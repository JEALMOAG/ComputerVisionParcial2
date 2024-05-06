# -*- coding: utf-8 -*-
"""
Created on Mon May  6 14:01:05 2024

@author: jama2
"""

import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('horno3.jpg')


# Definir la matriz de traslación
traslacion_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
# Aplicar la traslación a la imagen
imagen_traslada = cv2.warpAffine(imagen, traslacion_matrix, (imagen.shape[1], imagen.shape[0]))


# Definir el ángulo de rotación
angulo_rotacion = 45
# Calcular el centro de la imagen
centro = (imagen.shape[1] // 2, imagen.shape[0] // 2)
# Definir la matriz de rotación
rotacion_matrix = cv2.getRotationMatrix2D(centro, angulo_rotacion, 1.0)
# Aplicar la rotación a la imagen
imagen_rotada = cv2.warpAffine(imagen, rotacion_matrix, (imagen.shape[1], imagen.shape[0]))


# Definir el factor de escala
escala = 1.5
# Redimensionar la imagen
imagen_escalada = cv2.resize(imagen, None, fx=escala, fy=escala)


# Definir las coordenadas de la región de interés (ROI)
x1, y1, x2, y2 = 100, 50, 300, 200
# Recortar la región de interés de la imagen
imagen_recortada = imagen[y1:y2, x1:x2]

# Mostrar las imágenes resultantes
cv2.imshow('Imagen Original', imagen)
cv2.imwrite('original.jpg', imagen)
cv2.imshow("Traslacion", imagen_traslada)
cv2.imwrite('Traslacion.jpg', imagen_traslada)
cv2.imshow("Rotacion", imagen_rotada)
cv2.imwrite('Rotacion.jpg', imagen_rotada)
cv2.imshow("Escala", imagen_escalada)
cv2.imwrite('Escala.jpg', imagen_escalada)
cv2.imshow("Recorte", imagen_recortada)
cv2.imwrite('Recorte.jpg', imagen_recortada)


# Esperar hasta que se presione una tecla y luego cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()