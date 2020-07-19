from functionsImages.conversion import *
from skimage import io,img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np
import moviepy.editor as mpy
import glob


def get_matching(bw_img1,bw_img2):
    pass
def tipo(match):
    if( len( match[0] ) == 1):
        return 1
    else:
        return 0    

def tras_estandar(image1,image2,frames):
    h,w,c = image1.shape
    intermedio = np.zeros((h,w,3))
    for i in range(h):
        for j in range(w):
            consr = (image2[i,j,0]-image1[i,j,0])/frames 
            consg = (image2[i,j,1]-image1[i,j,1])/frames
            consb = (image2[i,j,2]-image1[i,j,2])/frames
            intermedio[i,j,0] = image1[i,j,0]+consr  
            intermedio[i,j,1] = image1[i,j,1]+consg
            intermedio[i,j,2] = image1[i,j,2]+consb 
    return intermedio

def tranformation(image1,image2,matrix,k_r,k_g,k_b,umbral):
    frames = 100
    image1_rgb = get_matrix_rgb(image1)
    image2_rgb = get_matrix_rgb(image2)
    intermedio = tras_estandar(image1_rgb,image2_rgb,100) #inicialización de imagen intermedia con constantes
    image1_bw = convertion_blak_white_from_RGB(image1_rgb,k_r,k_g,k_b,umbral)
    image2_bw = convertion_blak_white_from_RGB(image2_rgb,k_r,k_g,k_b,umbral)
    matching = matrix
    h,w,c = image1_rgb.shape 
    for i in range(h):
        for match in matching[i]:
            if(tipo(match)==1): #análisis de un match descomposición [[(,)];[(,),(,),(,)...]]
                xpos_i = match[0][0][0]
                xpos_f = match[0][0][1]
                bits_totales_x = xpos_f-xpos_i+1
                inicializadores_y = []
                inicializadores_x = []
                for tuples in match[1]:
                    inicializadores_y.append(tuples[1]-tuples[0]+1)
                constante_bw = bits_totales_x/sum(inicializadores_y)                
                inicializadores_x = constante_bw*inicializadores_y
                
                peso_ori_r,peso_ori_g,peso_ori_b = sum(image1_rgb[i,xpos_i:xpos_f+1,0]),sum(image1_rgb[i,xpos_i:xpos_f+1,1]),sum(image1_rgb[i,xpos_i:xpos_f+1,2])
                consr,consg,consb = peso_ori_r/bits_totales_x,peso_ori_g/bits_totales_x,peso_ori_b/bits_totales_x
                
                inicial_r = inicializadores_x*consr
                inicial_g = inicializadores_x*consg 
                inicial_b = inicializadores_x*consb

                iterador = 0
                for tuples in match[1]:
                    cons_r_bit = inicial_r[iterador] / sum(image1_rgb[i,tuples[0]:tuples[1]+1,0])
                    cons_g_bit = inicial_g[iterador] / sum(image1_rgb[i,tuples[0]:tuples[1]+1,1])
                    cons_b_bit = inicial_b[iterador] / sum(image1_rgb[i,tuples[0]:tuples[1]+1,2])
                    iterador = iterador +1 
                    for posi in range (tuples[0],tuples[1]+1):
                        intermedio[i,posi,0] = image1_rgb[i,posi,0]*cons_r_bit 
                        intermedio[i,posi,1] = image1_rgb[i,posi,1]*cons_g_bit 
                        intermedio[i,posi,2] = image1_rgb[i,posi,2]*cons_b_bit 
                
            else: #análisis de un match composición [[(,),(,),(,)...];[(,)]]
                y_posi = match[1][0][0] 
                y_posf = match[1][0][1]
                y_peso_bw = y_posf-y_posi+1 
                x_peso_r,x_peso_g,x_peso_b = 0,0,0
                
                for tuples in match[0]:
                    x_peso_r = x_peso_r + intermedio[i,tuples[0]:tuples[1]+1,0]  
                    x_peso_g = x_peso_g + intermedio[i,tuples[0]:tuples[1]+1,1]
                    x_peso_b = x_peso_b + intermedio[i,tuples[0]:tuples[1]+1,2]
                    
                for tuples in match[0]:
                    for posi in range (tuples[0],tuples[1]+1):
                        intermedio[i,posi,0] = x_peso_r /y_peso_bw  
                        intermedio[i,posi,1] = x_peso_g /y_peso_bw
                        intermedio[i,posi,2] = x_peso_b /y_peso_bw
                        
    return intermedio   

def animar_rgb(image1,image2,matching,k_r,k_g,k_b,umbral):
    inicio = get_matrix_rgb(image1)
    final = get_matrix_rgb(image2)
    io.imsave("Images/Frames/imag_generada000.png",image1)    
    segundo = tranformation(image1,image2,matching,k_r,k_g,k_b,umbral)
    nuevo = segundo
    for i in range(1,100):
        io.imsave("Images/Frames/imag_generada{1:009d}.png".format(i),nuevo)
        nuevo = tras_estandar(nuevo,final)
    io.imsave("Images/Frames/imag_generada100.png",final)
    file_list = sorted(glob.glob("./Images/Frames/*.png"))
    fps = 20
    clip = mpy.ImageSequenceClip(file_list, fps=fps,load_images=True)
    clip.write_gif('movie.gif')