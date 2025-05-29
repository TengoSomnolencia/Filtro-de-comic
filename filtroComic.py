import cv2
import numpy as np

# Verificar que carga la imagen
imagen = cv2.imread("images.jpg")

if imagen is None:
    print("Error!!! No se pudo cargar la imagen")
    exit()

#Suavizado bilateral para conservar bordes
suavizada = cv2.bilateralFilter(imagen, d=9, sigmaColor=100, sigmaSpace=100)

#Deteccion de bordes en escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris = cv2.medianBlur(gris, 7)
bordes = cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)

#Posterización de colores
def posterizar(imagen, niveles=8):
    factor = 256 // niveles
    return (imagen // factor) * factor

posterizada = posterizar(suavizada)

#Convertir bordes a BGR y combinarlos con la imagen posterizada
bordes_color = cv2.cvtColor(bordes, cv2.COLOR_GRAY2BGR)
comic = cv2.bitwise_and(posterizada, bordes_color)

#Agregar texto sobre la imagen
cv2.putText(comic, "", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

#Mostrar resultados
cv2.imshow("Original", imagen)
cv2.imshow("Con filtro comic", comic)

#Guardar la imagen
cv2.imwrite("images_comic.jpg", comic)
print("Su imagen fue guardada con éxito con el filtro de comic.")

cv2.waitKey(0)
cv2.destroyAllWindows()