from functionsImages.animation import *
from skimage import io,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mpy
import glob




def get_matrix_rgb(nombre_de_imagen):
    matrix = io.imread(nombre_de_imagen)
    return matrix

def convertion_gris(nombre_de_imagen,r_1,g_1,b_1):
    image = get_matrix_rgb(nombre_de_imagen)
    h,w,c = image.shape 
    image_bw = np.zeros((h,w))
    for i in range(h):
        for j in range(w): 
            valr=image[i,j,0]
            valg=image[i,j,1]
            valb=image[i,j,2]
            image_bw[i,j] = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
    return image_bw

def convertion_blak_white(image,r_1,g_1,b_1,umbral):
    imag_rgb = get_matrix_rgb(image)
    h,w,c = imag_rgb.shape 
    image_bw = np.zeros((h,w))
    for i in range(h):
        for j in range(w): 
            valr=imag_rgb[i,j,0]
            valg=imag_rgb[i,j,1]
            valb=imag_rgb[i,j,2]
            var = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
            if var>=umbral:
                image_bw[i,j] = 1                
    return image_bw

def convertion_blak_white_from_RGB(image,r_1,g_1,b_1,umbral): #Pregunta 8 
    imag_rgb = image
    h,w,c = imag_rgb.shape 
    image_bw = np.zeros([h,w])
    for i in range(h):
        for j in range(w): 
            valr=imag_rgb[i,j,0]
            valg=imag_rgb[i,j,1]
            valb=imag_rgb[i,j,2]
            var = r_1*float(valr)+g_1*float(valg)+b_1*float(valb)
            if var >= umbral:
                image_bw[i,j] = 1                
    return image_bw    

def mostrar_imagen_de_array(imagen):
    plt.rcParams['image.cmap'] = 'gray'
    plt.imshow(imagen)
    plt.title("Imagen en blanco y negro")
    plt.show()


def convert_and_show(image,k_r,k_g,k_b,umbral):
    imagen_bw = convertion_blak_white(image,k_r,k_g,k_b,umbral);
    mostrar_imagen_de_array(imagen_bw);


    