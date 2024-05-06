import cv2
import numpy as np

# Función para agregar ruido gaussiano a una imagen
def agregar_ruido_gaussiano(imagen, media=0, desviacion_estandar=25):
    alto, ancho, canales = imagen.shape
    ruido = np.random.normal(media, desviacion_estandar, (alto, ancho, canales))
    imagen_con_ruido = np.clip(imagen + ruido, 0, 255).astype(np.uint8)
    return imagen_con_ruido

# Función para agregar ruido de sal y pimienta a una imagen
def agregar_ruido_sal_pimienta(imagen, proporcion_sal_vs_pimienta=0.5, cantidad=0.04):
    imagen_con_ruido = np.copy(imagen)

    # Ruido de sal
    cantidad_sal = np.ceil(cantidad * imagen.size * proporcion_sal_vs_pimienta)
    coordenadas_sal = [np.random.randint(0, i - 1, int(cantidad_sal)) for i in imagen.shape]
    imagen_con_ruido[coordenadas_sal[0], coordenadas_sal[1], :] = 255

    # Ruido de pimienta
    cantidad_pimienta = np.ceil(cantidad * imagen.size * (1.0 - proporcion_sal_vs_pimienta))
    coordenadas_pimienta = [np.random.randint(0, i - 1, int(cantidad_pimienta)) for i in imagen.shape]
    imagen_con_ruido[coordenadas_pimienta[0], coordenadas_pimienta[1], :] = 0

    return imagen_con_ruido

# Función para aplicar un filtro a una imagen
def aplicar_filtro(imagen, tipo_filtro='gaussiano'):
    if tipo_filtro == 'gaussiano':
        return cv2.GaussianBlur(imagen, (5, 5), 0)
    elif tipo_filtro == 'media':
        return cv2.blur(imagen, (5, 5))
    elif tipo_filtro == 'mediana':
        return cv2.medianBlur(imagen, 5)
    elif tipo_filtro == 'minimo':
        return cv2.erode(imagen, np.ones((3, 3)))
    elif tipo_filtro == 'maximo':
        return cv2.dilate(imagen, np.ones((3, 3)))

# Cargar la imagen original
imagen_original = cv2.imread('horno3.jpg')

# Agregar ruido gaussiano
ruido_gaussiano = agregar_ruido_gaussiano(imagen_original)

# Agregar ruido de sal y pimienta
ruido_sal_pimienta = agregar_ruido_sal_pimienta(imagen_original)

# Aplicar filtros a las imágenes con ruido
imagenes_filtradas = {}
for tipo_ruido, imagen_con_ruido in [('gaussiano', ruido_gaussiano), ('sal_pimienta', ruido_sal_pimienta)]:
    for tipo_filtro in ['gaussiano', 'media', 'mediana', 'minimo', 'maximo']:
        imagen_filtrada = aplicar_filtro(imagen_con_ruido, tipo_filtro)
        imagenes_filtradas[(tipo_ruido, tipo_filtro)] = imagen_filtrada

# Guardar todas las imágenes
cv2.imwrite('ruido_gaussiano.jpg', ruido_gaussiano)
cv2.imwrite('ruido_sal_pimienta.jpg', ruido_sal_pimienta)
for (tipo_ruido, tipo_filtro), imagen_filtrada in imagenes_filtradas.items():
    cv2.imwrite(f'filtrada_{tipo_ruido}_{tipo_filtro}.jpg', imagen_filtrada)

