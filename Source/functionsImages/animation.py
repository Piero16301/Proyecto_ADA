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
def iniciar_ceros(h,w):
    mat = list()
    for i in range(h):
        arr = []
        for j in range(w):
            arr.append(0)
        mat.append(arr)
    return mat

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

def animation_black_white(image1,image2,k_r,k_g,k_b,umbral,positions):
    plt.rcParams['image.cmap'] = 'gray'
    frames = 100
    image1_rgb = get_matrix_rgb(image1)
    image2_rgb = get_matrix_rgb(image2)
    h,w,c = image1_rgb.shape
    image1_bw = convertion_blak_white_from_RGB(image1_rgb,k_r,k_g,k_b,umbral)
    image2_bw = convertion_blak_white_from_RGB(image2_rgb,k_r,k_g,k_b,umbral)
    matrix = positions
    io.imsave("functionsImages/Images/Frames/imag_generada000.png",img_as_ubyte(image1_bw))
    for num_paso in range(frames):
        nuevo = iniciar_ceros(h,w)
        for num_fila in range(len(matrix)):
            filas = matrix[num_fila]
            for matchs in filas:
                if len(matchs[1]) == 1: #composición
                    posfinal_y = matchs[1][0][1]
                    posinicial_y = matchs[1][0][0]
                    posfinal_x = matchs[0][-1][1]
                    posinicial_x = matchs[0][0][0]
                    print(posfinal_y," ",posinicial_y," ",posfinal_x," ",posinicial_x)
                    tamanho_x = posfinal_x-posinicial_x+1
                    num_divisiones =  posfinal_y-posinicial_y+1
                    numbitsx = 0
                    for bloques in matchs[0]:    
                            for posi in range(bloques[0],bloques[1]+1):
                                numbitsx = numbitsx+1
                    if num_divisiones<=numbitsx:
                        factor_division = (tamanho_x)//num_divisiones   #factor de divison de fila n
                        lim_divi_xy =[]
                        posi_x,posi_y = matchs[0][0][0],posinicial_y
                        for i in range(num_divisiones):
                            posi_x = posi_x+ factor_division-1
                            if i == num_divisiones-1:
                                lim_divi_xy.append((posi_x,matchs[0][-1][1]))
                                break
                            lim_divi_xy.append((posi_x,posi_y))
                            posi_y=1+posi_y

                        for bloques in matchs[0]:    
                            for posi in range(bloques[0],bloques[1]+1):
                                for elem in lim_divi_xy:
                                    if posi<=elem[0]:
                                        const = (elem[1] - posi)/(frames-1)
                                        nuevo[num_fila][posi+ int(const*num_paso)]=1
                                        break      
                    
                    else:
                        const1 = (posinicial_y-posinicial_x )/(frames-1)
                        const2 = (posfinal_y-posfinal_x )/(frames-1)
                        inicial = posinicial_x+ int(const*num_paso)
                        final = posfinal_x+ int(const*num_paso)
                        for posicion in range(inicial,final+1):
                            nuevo[num_fila][posicion] = 1

                elif len(matchs[0]) == 1:  #descomposición 
                    posfinal_y = matchs[1][0][0]
                    posinicial_y = matchs[1][-1][1]
                    posfinal_x = matchs[0][0][1]
                    posinicial_x = matchs[0][0][0]
                    numbitsy = 0    
                    for bloques in matchs[1]:    
                        for posi in range(bloques[0],bloques[1]+1):
                                numbitsy = numbitsy+1
                    opcion = [posinicial_x,posfinal_y]
                    if numbitsy >= opcion[1]-opcion[0]+1:
                        while numbitsy > opcion[1]-opcion[0]+1:
                            if posinicial_y-opcion[0]>=0:
                                opcion[0] = opcion[0]+1 
                            if numbitsy > opcion[1]-opcion[0]+1:
                                break
                            if posfinal_y-opcion[1]>=0:
                                opcion[1] = opcion[1]+1

                        for bloques in matchs[1]:    
                            for posi in range(bloques[0],bloques[1]+1):
                                contador = 0
                                const = (posi - opcion[0]+contador)/(frames-1)
                                nuevo[num_fila][opcion[0]+contador+ int(const*num_paso)]=1
                                contador=contador+1

                    else: 
                        opcion = [posinicial_x,posfinal_y]
                        for bloques in matchs[1]:    
                            for posi in range(bloques[0],bloques[1]+1):
                                contador = 0
                                const = (posi - opcion[0]+contador)/(frames-1)
                                nuevo[num_fila][opcion[0]+contador+ int(const*num_paso)]=1
                                contador=contador+1
                        
                        

#guardamos y animamos las imágenes
        io.imsave("Images/Frames/imag_generada{0:03d}.png".format(num_paso+1),img_as_ubyte(nuevo))
    io.imsave("Images/Frames/imag_generada101.png",img_as_ubyte(image2_bw))
    file_list = sorted(glob.glob("./Images/Frames/*.png"))
    fps = 70
    clip = mpy.ImageSequenceClip(file_list, fps=fps,load_images=True)
    clip.write_gif('movie.gif')

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