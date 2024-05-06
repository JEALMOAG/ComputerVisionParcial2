"""
Created on 01 May 16:14:44 2024
@author: Jesus Alejandro Montes Aguila
"""
import cv2
import numpy as np

def mostrarImagen(imagen, titulo:str='', tiempo:int=0):
    cv2.imshow(titulo, imagen)
    cv2.waitKey(tiempo)
    cv2.destroyAllWindows()

imagen = cv2.imread("yo.jpg", 0)
m,n=imagen.shape
imagenA = np.zeros_like(imagen)
imagenB = np.zeros_like(imagen)
imagenM = np.zeros_like(imagen)


kernel1 = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernel2 = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
kernel2 = np.transpose(kernel2)

print(kernel1)
print(kernel2)

def gradiente(k, img, imgres):
    for x in range(m-2):
        for y in range(n-2):
            res=np.sum(img[x:3+x,y:3+y]*k)
            if res>50:
                imgres[x,y]=res
                
gradiente(kernel1, imagen, imagenA)
gradiente(kernel2, imagen, imagenB)
             
for x in range(m-2):
    for y in range(n-2):
        imagenM[x, y]= abs(imagenA[x,y]) + abs(imagenB[x,y])

a=cv2.hconcat((imagen, imagenA))        
b=cv2.hconcat((imagenB, imagenM))
c=cv2.vconcat((a,b))        
        
mostrarImagen(c, titulo='resultado', tiempo=0)
cv2.imwrite('yoFiltrado.jpg', c)