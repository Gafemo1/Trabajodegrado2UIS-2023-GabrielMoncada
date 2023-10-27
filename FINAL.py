import sys
import tkinter as tk
from tkinter import filedialog as fd
import turtle
import math
import os
import numpy as np
from datetime import datetime
from PIL import Image

HOME = "" #Ruta de guardado de archivos.
REGLAS_H ={}
TREGLAS ={}
COLORES_L={}

def salir():
    print('Terminado.')
    
def mostrarmenu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')
        
def generarmenu(entrada, salida):
    opcion = None
    while opcion != salida:
        mostrarmenu(entrada)
        opcion = leeropcion(entrada)    
        ejecutardef(opcion,entrada) 
        
def ejecutardef(entrada, entradas):
    entradas[entrada][1]()
    
def leeropcion(entrada):
    while (a := input('Opción:')) not in entrada:
        print('Entrada invalida, vuelva a entrar opción:')
    return a
    
def menu():
    opciones = {
        '1': ('Modo matriz cuadrada y dibujo modo pixel.', accion1),
        '2': ('Homomorfismo y dibujo directo.', accion2),
        '3': ('Homomorfismo, traducción y dibujo directo.', accion3),
        '4': ('Secuencia Shapyro.', accion4),
        '5': ('Homomorfismo y dubjo modo pixel.', accion5),
        '6': ('Homomorfismo, traducción y dibujo modo pixel.', accion6),
        '7': ('Salir.', salir)
    }
    generarmenu(opciones, '7')
    
def iteracion(axioma, pasos):
    axiomaf = [axioma]
    for _ in range(pasos):
        sc = axiomaf[-1]
        sa = [regla_apli(letra) for letra in sc]
        axiomaf.append(''.join(sa))
    return axiomaf

def regla_apli(cadena):
    if cadena in REGLAS_H:
        return REGLAS_H[cadena]
    return cadena

def tderivation(tmodel, steps):
    tderived = [tmodel]  
    next_seq = tderived[-1]
    next_axiom = [trule(char) for char in next_seq]
    tderived.append(''.join(next_axiom))
    return tderived

def trule(tsequence):
    if tsequence in TREGLAS:
        return TREGLAS[tsequence]
    return tsequence

def setwindowsize(x, y, tp):
    turtle.setup(x, y)
    turtle.setworldcoordinates(-x/2,-y/2,x/2+tp,y/2)

def setwindowsize2(x, y, tp):
    turtle.setup(x, y)
    turtle.seetworldcoordinates(tp,tp,x,y)   
    
def setwindowsize3(x, y):
    turtle.setup(x, y)
    turtle.setworldcoordinates(0,0,x,y)   
    
def setwindowsize4():
    x = int(input('Entre largo de la ventana:'))
    y = int(input('Entre el alto de la ventana:'))
    turtle.setup(x, y)
    #turtle.screensize(x, y)
    #turtle.setworldcoordinates(-(x/2),-(y/2),(x/2),(y/2)) 

def setwindowsize5(x, y):
    turtle.setup(x, y)
    
def setturtle():
    turtle.pu()
    x = int(input('Entre la coordenada x para posicion inicial:'))
    y =  int(input('Entre la coordenada y para posicion inicial:'))
    turtle.setpos(x, y)

def setturtle2(ymax):
    turtle.pu()
    turtle.setpos(0, -ymax)    

def setturtle3(xmax, ymax, px):
    turtle.pu()
    turtle.setpos(-(2* xmax), -(ymax//2)+px)    
        
        
def drawpixel(x, y, max, may, color, pixelsize):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(x*pixelsize-(max // 2),(y*pixelsize-(may // 2))+2*pixelsize)
    turtle.color(COLORES_L[color, 0], COLORES_L[color, 1], COLORES_L[color, 2])
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize)
        turtle.right(90)
    turtle.end_fill()
 
def drawpixel2(x, y, color, colum, fila, pixelsize = 1):
    turtle.tracer(0, 0)
    turtle.colormode(255)
    turtle.penup()
    turtle.setpos(((x*pixelsize))-colum,((y*pixelsize)+pixelsize)-fila)
    turtle.color(COLORES_L[color, 0], COLORES_L[color, 1], COLORES_L[color, 2])
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(pixelsize-1)
        turtle.right(90)
    turtle.end_fill()    
    
def foto():
    fecha = (datetime.now()).strftime("%d%b%Y-%H-%M-%S")
    nombrefile = 'Gabriel-'+ fecha
    eps = (HOME+nombrefile+'.eps')
    png = (HOME+nombrefile+'.png')
    turtle.getscreen().getcanvas().postscript(file=eps)
    print( 'Guardado', nombrefile+'.eps' )
    img = Image.open(eps) 
    img.save( png, optimize = True)
    print( 'Guardado', nombrefile+'.png' )
    turtle.clear()
    print("Foto tomada.")

def fotod(columnas, max, maxy):
    fecha = (datetime.now()).strftime("%d%b%Y-%H-%M-%S")
    nombrefile = 'Gabriel-'+ fecha+'-[id#%d][x#%d][y#%d]'%(columnas,max,maxy)
    eps = (HOME+nombrefile+'.eps')
    png = (HOME+nombrefile+'.png')
    turtle.getscreen().getcanvas().postscript(file=eps)
    print( 'Guardado', nombrefile+'.eps' )
    img = Image.open(eps) 
    img.save( png, optimize = True)
    print( 'Guardado', nombrefile+'.png' )
    turtle.clear() 
   
def Lsystem_1(cadena):
    tp = int(input('Entre la longitud del segmento en cada paso:'))
    ai = float(input('Entre la dirección inicial de la tortuga:'))
    angulo = float(input('Entre el ángulo de incremento:'))
    t= float(120)
    #turtle.speed(0)
    turtle.tracer(0, 0)
    i = 1
    while i != '0':
        x = int(input('Entre largo de la ventana:'))
        y = int(input('Entre el alto de la ventana:'))
        z = int(input('Entre el número de capturas largo dividido en 1000:'))
        for j in range(z):
            jj = j+1
            setwindowsize5(x, y)
            setturtle2(y-(1000  *jj))
            #turtle.screensize(v, v)
            turtle.setheading(ai)
            turtle.Screen()
            stack = []
            for letra in cadena:  
                turtle.pd()
                if letra in ["F", "G", "R", "L"]:
                    turtle.forward(tp)
                elif letra == "f":
                    turtle.pu()
                    turtle.forward(tp)
                elif letra == "+":
                    turtle.right(angulo)
                elif letra == "-":
                    turtle.left(angulo)
                elif letra == "[":
                    stack.append((turtle.position(), turtle.heading()))
                elif letra == "]":
                    turtle.pu()  
                    position, heading = stack.pop()
                    turtle.goto(position)
                    turtle.setheading(heading)
                elif letra == "A":
                    turtle.right(90)
                    turtle.forward(tp)
                    turtle.left(90)
                elif letra == "B":
                    turtle.left(90)
                    turtle.forward(tp)
                    turtle.right(90)
                elif letra == "T":
                    turtle.backward(tp)
                elif letra =="b":
                    turtle.left(t)    
            turtle.hideturtle()        
            fotod(jj, x, y)
        i = input('Cualquier entrada para volver a configurar dibujo o cero (0) para terminar:')   
    
def shap(tsequence, steps):
    F = []
    for char in tsequence:
        F.append(char)
    return F

def shapi(final):
    t=[]
    for co in final:
        if co in ["0"]:
            t.append(1)
        elif co in ["1"]:
            t.append(-1)
    return t

def shapirito(t):
    F=[]
    for a in t:
        F.append(int(a))
    return F

def shapiro(t):
    F=[]
    n=0
    for i in t:
        if n > 0:
            nt=t[n]
            ns=int(t[n-1])
            nf=int(ns*nt)
            s=n % 2
            if s == 0:
                if nf == 1:
                    F[0]+=("L")
                else:
                    F[0]+=("R")
            else:
                if nf == 1:
                    F[0]+=("R")
                else:
                    F[0]+=("L")
        elif n == 0:
            F.append("F")
        n += 1
    return(F)

def Lsistema_2(cadena, tp, angulo, v):
    setwindowsize(v,v)
    turtle.tracer(0, 0)
    #turtle.speed(0)
    turtle.setheading(0)
    turtle.hideturtle()
    #turtle.screensize(1500, 1500)
    for letra in cadena:
        stack = []
        turtle.pd()
        if letra in ["F"]:
            turtle.forward(tp)
        elif letra == "f":
            turtle.pu() 
            turtle.forward(tp)
        elif letra == "+":
            turtle.right(angulo)
        elif letra == "-":
            turtle.left(angulo)
        elif letra == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif letra == "]":
            turtle.pu()  
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)
        elif letra == "R":
            turtle.right(90)
            turtle.forward(tp)
        elif letra == "L":
            turtle.left(90)
            turtle.forward(tp)
        elif letra == "T":
            turtle.backward(tp) 
        elif letra == 'X':
            print('No hago nada')  
    foto() 
                
def colores():
    for i in REGLAS_H:
        coordenada_color = 1
        for j in range(3):
            valor = int(input("Entre la coordenada [#%d] del código RGB asociado a la entrada " % coordenada_color+i+':'))
            COLORES_L[i, j] = valor
            coordenada_color += 1

def colores2():
    for i in REGLAS_H:
        coordenada_color = 1
        for j in range(3):
            valor = int(input("Entre la coordenada [#%d] del código RGB asociado a la entrada " % coordenada_color+TREGLAS[i]+':'))
            COLORES_L[TREGLAS[i], j] = valor
            coordenada_color += 1
                
def dibujarpixels(tmodelo):
    i= 1
    while i != '0':
        k_colum =int(input("Entre el numero de columnas por fila:"))
        pixel_t = int(input("Entre el tamaño de los pixeles:"))
        tt = len(tmodelo[-1])
        v_y = tt // k_colum
        setwindowsize5((k_colum*pixel_t)+(2*pixel_t),(((v_y+1)*pixel_t)+(2*pixel_t)))
        setturtle3(k_colum*pixel_t,((v_y+1)*pixel_t), pixel_t)
        xmax = k_colum*pixel_t
        ymax = (v_y+1)*pixel_t
        c_a = 0
        c_b = 0 
        for l in tmodelo[-1]:
            drawpixel( c_a, c_b, xmax, ymax, l, pixel_t)
            c_a += 1
            if c_a == k_colum:
                c_a = 0
                c_b += 1
        turtle.hideturtle()
        #turtle.update()
        foto()
        turtle.bye
        i = input('Cualquier entrada para volver a configurar dibujo o cero (0) para terminar:')
    
def dibujarpixels2(tmodelo, tp, columnas):
    tt = len(tmodelo[-1])
    v_y = (tt // columnas)+1
    setwindowsize((columnas*tp)+tp,((v_y*tp)+tp), tp)
    c_a = 0
    c_b = 0 
    nx = ((columnas*tp)/2)
    ny = ((v_y*tp)/2)
    for l in tmodelo[-1]:
        drawpixel2( c_a, c_b, l, nx, ny, tp)
        c_a += 1
        if c_a == columnas:
            c_a =0
            c_b += 1
    turtle.hideturtle()
    #turtle.update()
    fotod(columnas, nx, ny)  
    print('Terminado')
                  
def accion1():
    tm = int(input("Entre el tamaño de la matriz cuadrada de las imágenes:"))
    regla_num = 1
    while True:
        regla = input("Digite el símbolo de entrada [#%d] o escriba 0 para terminar: " % regla_num)
        b=[]
        if regla == '0':
            break
        for i in range(tm):
            c=[]
            for j in range(tm):
                dat = input('Entre la cadena de la posicicón [#%d][#%d]'%(i,j)+" de la imagen de "+ regla+':')
                c.append(dat)
            b.append(c)       
        REGLAS_H[regla] = b
        regla_num += 1
    i = 1
    while i != '0':
        k = int(input('Entre el número de iteraciones:'))
        axim = input('Entre el axioma:')
        matrixc = newiteracion(axim, k, tm)
        print(matrixc)
        colores()
        print(COLORES_L)
        print(matrixc[0][0])
        dibujarmatrix(matrixc, k, tm)
        i = input('Cualquier entrada para volver a dibujar, cero (0) para terminar:')
    main()
        
def dibujarmatrix(matrix, iteraciones, tm):
    pixel_t = int(input("Entre el tamaño de los pixeles:"))
    k = pow(tm, 2*iteraciones)
    k2 = pow(tm, iteraciones)
    nx = ((k2*pixel_t)/2)
    print(k, k2, nx)
    setwindowsize((nx*pixel_t)+pixel_t,(nx*pixel_t)+pixel_t, pixel_t)
    for i in range(k2):
        for j in range(k2):
            variable = matrix[i][j]
            print(i,j,variable)
            drawpixel2(i, j, variable, nx, nx, pixel_t)
    turtle.hideturtle()
    turtle.update()
    print('Terminado')
    fotod(tm, nx, nx)  

def newiteracion(axioma, veces, dimen):
    B=[]
    B.append(axioma)
    print(B)
    for m in range(veces):
        t= m+1
        if t == 1:
            base = REGLAS_H[axioma]
            B.append(base)
        else:
            sc = np.array(B[-1])
            E = []
            for i in range(pow(dimen,m)):
                for j in range(pow(dimen,m)):
                    if j==0:
                        F = np.array(REGLAS_H[sc[i][j]])
                    else:
                        F_1 = F
                        F_2= np.array(REGLAS_H[sc[i][j]])
                        F_3 = np.concatenate((F_1,F_2), axis=1)
                        F = F_3
                if i == 0:
                    E = F
                else:
                    E_1 = E
                    E_2 = F
                    E_3 = np.concatenate((E_1,E_2))
                    E = E_3
                B.append(E)
    return B[-1]    
            
def accion2():
    pedireglas()
    i = 1
    while i !='0':
        axioma = input('Entre el axioma (w):')
        iteraciones = int(input('Entre el número de iteraciones (n):'))
        modelo = iteracion(axioma, iteraciones)
        cadena = modelo[-1]
        Lsystem_1(cadena)
        print('Terminado.')
        i = input('Cualquier entrada para volver a dibujar, cero (0) para terminar:') 
    turtle.bye()    
    main()
        
def accion3():
    pedireglas()
    tpedireglas()  
    i = 1
    while i !='0':
        axioma = input('Entre el axioma (w):')
        iteraciones = int(input('Entre el número de iteraciones (n):'))
        modelo = iteracion(axioma, iteraciones)
        tmodelo = tderivation(modelo[-1],iteraciones)
        cadena = tmodelo[-1]
        Lsystem_1(cadena)
        print('Terminado.')
        i = input('Cualquier entrada para volver a dibujar, cero (0) para terminar:') 
    turtle.bye()    
    main()
    
def accion4():
    pedireglas()
    tpedireglas()    
    axioma = input('Entre el axioma (w):')
    iteraciones = int(input('Entre el número de iteraciones (n):'))
    modelo = iteracion(axioma, iteraciones)
    tmodelo = tderivation(modelo[-1],iteraciones)
    f1 = shap(tmodelo[-1], iteraciones)
    f2 = shapi(f1)
    f3 = shapirito(f2)
    f4 = shapiro(f3)
    longituds = int(input('Entre la longitud del segmento en cada paso:'))
    anguloincremento = float(input('Entre el ángulo de incremento:'))
    Lsistema_2(f4[0], longituds,anguloincremento, 1500)
    print('Terminado.')
    main()

def accion5():
    pedireglas()
    colores()
    i = 1
    while i !='0':
        axioma = input("Entre el axioma (w): ")
        pasos = int(input("Entre numero de iteraciones (n): "))
        modelo = iteracion(axioma,pasos)
        dibujarpixels(modelo)
        i = input('Cualquier entrada para volver a dibujar, cero (0) para terminar:')
    turtle.bye()     
    main()
    
def accion6():
    pedireglas()
    tpedireglas()
    colores2()
    i = 2
    while i != '0':
        axioma = input("Entre el axioma (w): ")
        pixel_t = int(input("Entre el tamaño de los pixeles:"))
        p = input('Desea fotos de todas las iteraciones? [0] para sí, [cualquier tecla para no]:')
        while p == '0':
            t = int(input('Entre numero de iteraciones (n): '))
            k_colum =int(input("Entre el numero de columnas por fila:"))
            p2 = input('Desea fotos de todas las iteraciones por columnas hasta la columna [#%d]'%k_colum+'? 0 para sí, 1 para otro intervalo de columnas y cualquier tecla para solo una foto:')
            while p2 == '0':
                for j in range (t):
                    modelo= iteracion(axioma, j+3)
                    tmodelo = tderivation(modelo[-1], j+3)
                    for jj in range (k_colum-1):
                        ji= jj+1
                        dibujarpixels2(tmodelo, pixel_t, ji)
                p = p2 = input('Desea fotos de todas las iteraciones para otro n, cualquier tecla para no, 0 para sí:')   
                if p2 != '0':
                    break
            while p2 == '1':
                ci = int(input('Entre cantidad de columnas inicial:'))
                cf = int(input('Entre cantidad de columnas final:'))
                for j in range (t):
                    modelo= iteracion(axioma, j+3)
                    tmodelo = tderivation(modelo[-1], j+3)                  
                    for jj in range (ci, cf, 1):
                        dibujarpixels2(tmodelo, pixel_t, jj)
                p2 = input('Desea introducir un nuevo intervalo? [1] para sí y [otra tecla] para salir:')
                if p2 != 1:
                    break                           
            modelo = iteracion (axioma, t)
            tmodelo = tderivation(modelo[-1], t)
            dibujarpixels2(tmodelo, pixel_t, k_colum)
            p = input('Desea fotos de todas las iteraciones? cualquier tecla para no, 0 para sí:')
            if p != 0:
                break   
        pasos = int(input('Entre numero de iteraciones (n): '))
        modelo = iteracion(axioma, pasos)
        tmodelo = tderivation(modelo[-1], pasos)
        p2 = input('Desea fotos de todas las iteraciones por columnas hasta una constante? 0 para sí, 1 para otro intervalo de columnas y cualquier tecla para solo una foto:')
        while p2 == '0':
            k_colum =int(input("Entre la constante final:"))
            for jj in range(k_colum):        
                ji= jj+1
                dibujarpixels2(tmodelo, pixel_t, ji)
            p2 = input('Desea introducir una nueva constante? [1] para sí y [otra tecla] para salir:')
            if p2 != 0:
                break    
        while p2 == '1':
            ci = int(input('Entre cantidad de columnas inicial:'))
            cf = int(input('Entre cantidad de columnas final:'))
            for jj in range (ci, cf, 1):
                dibujarpixels2(tmodelo, pixel_t, jj)
            p2 = input('Desea introducir un nuevo intervalo? [1] para sí y [otra tecla] para salir:')
            if p2 != 1:
                break
        k_colum =int(input("Entre el numero de columnas por fila:"))        
        dibujarpixels2(tmodelo, pixel_t, k_colum)   
        i = input('Cualquier entrada para volver a dibujar, cero (0) para terminar:')
    main()    

def pedireglas():
    regla_num = 1
    while True:
        regla = input("Entre la regla [#%d] de la forma (Entrada)->(Salida) o escriba 0 para terminar: " % regla_num)
        if regla == '0':
            break
        entrada, valor = regla.split("->")
        REGLAS_H[entrada] = valor
        regla_num += 1
        
def tpedireglas():
    for i in REGLAS_H:
        tregla = input("Entre la traducción de "+i+':')
        TREGLAS[i] = tregla      
        
def main():
    REGLAS_H.clear()
    COLORES_L.clear()
    TREGLAS.clear()
    menu()

if __name__ == "__main__":
    try:
        main()
    except BaseException:
        sys.exit(0)
