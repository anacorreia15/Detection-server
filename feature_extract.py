import cv2
import numpy as np
from copy import deepcopy
import math

# def show_image(img):
#     cv2.imshow("Foto", img)
#     #cv2.waitKey(0)
#     cv2.destroyAllWindows()

def calculate_radius(image):
    comeu_tudo = False
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    rows = gray.shape[0]
    circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, rows / 5, param1=100, param2=30)

    if circles is None:
        raise ValueError("Ups, não encontrei a tigela")
    
    biggest_radius = -1
    for i in circles[0, :][:1]:
        radius = int(i[2])
        print("Raio maior (Tigela): ", radius) #raio da tigela
        biggest_radius = radius

        cv2.circle(image, (int(i[0]), int(i[1])), radius, color=(255,0,0), thickness=3)
    
    #show_image(image)

    orange_lower = np.array([0, 164, 0]) #ajustar
    orange_upper = np.array([100, 225, 179]) #ajustar

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #show_image(hsv)
    mask = cv2.inRange(hsv, orange_lower, orange_upper)
    #show_image(mask)
    image = cv2.bitwise_and(image, image, mask=mask)
    #show_image(image)
    
    gray2 = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    gray2 = cv2.cvtColor(gray2, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray2, cv2.HOUGH_GRADIENT, 1, rows / 5, param1=100, param2=25) #, minRadius=50)

    smallest_radius = -1
    if circles is None:
        comeu_tudo = True
        print("COMEU TUDO!!!")
    else:
        for i in circles[0, :][:1]:
            radius = int(i[2])
            print("Raio Menor (Sopa): ",radius) #raio da sopa
            smallest_radius = radius
            cv2.circle(image, (int(i[0]), int(i[1])), radius, color=(0,0,255), thickness=3)
    
        #show_image(image)

    return biggest_radius, smallest_radius

#image_path = "soup.png"
#calculate_radius = calculate_radius(image_path)

# Definindo a função para calcular o volume da sopa em litros
def calcular_volume_sopa(biggest_radius_pixels, smallest_radius_pixels):

    #print( biggest_radius_pixels, smallest_radius_pixels)
    # Constantes em centímetros
    original_raio_maior = 6.0  # Raio maior em cm
    original_raio_menor = 1.5  # Raio menor em cm
    original_altura = 6.0  # Altura do cone truncado em cm

    # Escala para converter de pixels para centímetros
    escala = original_raio_maior / biggest_radius_pixels

    # Converter o raio menor para centímetros
    novo_raio_maior = smallest_radius_pixels * escala

    #print (novo_raio_maior)

    # Ajustar a altura para a nova base maior

    proporcao_altura = novo_raio_maior * original_altura
    nova_altura = proporcao_altura / original_raio_maior

    #print (nova_altura)

    # Calcular o volume do cone truncado usando a nova altura
    volume_cm3 = (1/3) * math.pi * nova_altura * (
        original_raio_menor**2 + original_raio_menor * novo_raio_maior + novo_raio_maior**2
    )

    # Converter o volume para litros (1 litro = 1000 cm³)
    volume_litros = volume_cm3 / 1000

    return volume_litros


# Testar a função com valores de exemplo
#biggest_radius_pixels, smallest_radius_pixels = calculate_radius
#volume = calcular_volume_sopa(biggest_radius_pixels, smallest_radius_pixels)
#print(f"Volume da sopa: {volume:.2f} litros")