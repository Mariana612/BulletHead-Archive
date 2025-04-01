import glob
import os
from tkinter import *
from random import *
from threading import Thread
import pygame
pygame.init() #inicia pygame

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MÚSICA ♪ /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
derecha = 'd'
izquierda = 'a'
saltar = 'w'
disparar = 'e'
ventana = Tk() #ventana Principal
ventana.title('BulletHead')
ventana.minsize(679,706)
ventana.resizable(width=False,height=False)

c_Principal = Canvas(ventana,width=679, height=670, bg='black') #canvas principal
c_Principal.place(x=0,y=0)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ VIDEOJUEGO ► /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



def cargarImg(archivo): #Cara la imagen
        ruta = os.path.join('img',archivo)
        imagen = PhotoImage(file=ruta)
        return imagen
    
def juego (p,x,num,g,numscor):
        '''
*****************************************************************************************************************************************************
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores

Programa: juego

Lenguaje y Versión: Python 3.8.3

Autora: Mariana Navarro Jiménez

Versión: 1.0

Fecha de ultima modificación: 12-07-2020

Entradas: p(Nombre del jugador), x(Dificultad del jeugo), num(Contador), g(señal que indica el nivel del jeugo), numscore(Puntuación del ugador)

Salidas: Score y nombre del jugador(si se gana)

******************************************************************************************************************************************************
'''
        global cerrarImg,laser,derecha,izquierda, saltar, disparar
        c = Canvas(ventana,width=679, height=737, bg='black')
        c.place(x=0,y=0) #canvas principal

        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ LOCALES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        
        nombre = p
        OPEN = True
        counter = 0
        contar = num
        b = numscor
        flag2 = g
        flag = x   
                
        
        #Enemigos
        misillist = []
        navelist=[]
        deslist = []

        vidas = 3
        
        #Locales para el score
        abrir = open(r"score\scoreboard.txt",'r+')
        abrir.seek(0)
        read = abrir.readlines()
        grades = read[1::2]
        nombres2 = read[0::2]

        #Locales para el movimiento
        apretado = 0
        apretadoi = 0
        apretadow = 0
        apretadox = 0
        indicador = 'abajo'
        
        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\CARGAR IMAGENES\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        def cargarVariasImg(input,listaResultado): #Funcion que carga diversas imagenes
                if (input == []):
                    return listaResultado
                else:
                    listaResultado.append(PhotoImage(file=input[0]))
                    return cargarVariasImg(input[1:],listaResultado)

        def cargarSprites(patron): #Funcion que carga los sprites 
                x = glob.glob('img/sprites/'+patron)
                x.sort()
                return cargarVariasImg(x,[])

        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\IMAGENES\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        c.image = cargarImg('City.png') 
        fondo = c.create_image(340,337, image=c.image )
        
        crusherimg = cargarImg('crusher.png')
        
        bala = cargarImg('bala.png')
        
        alienes = cargarSprites('Alien*.png')
        
        misilimg = cargarSprites('Misil*.png') 

        vides = cargarSprites('vida*.png')
        
        vids = c.create_image(57,673, tags =('vids')) 
        vads = c.create_image(87,673, tags =('vids'))
        veds = c.create_image(117,673, tags =('vids'))

        hueco = cargarImg('hueco.png') 

        bulles = cargarSprites('Bull*.png') 
        Bullx = c.create_image(330,600, tags =('Bullx'))
        
        red = cargarImg('red.png')
        
        vides = cargarSprites('vida*.png')
        
        red = cargarImg('red.png') 
        
        GameOver = cargarImg('GameOver.png')

        nex = cargarImg('next.png')
        
        menu = cargarImg('menu.png')
        
        won = cargarImg('won.png')
                        
        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ANIMACIÓN\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


        def BullxAni(i):
                nonlocal bulles, contar, vidas, OPEN
                if contar == 40 or contar ==80 or contar == 120 or vidas == 0: #Contador que detiene la animación
                        OPEN = False
                if (i==4):
                        i = 0
                if(OPEN == True):
                        c.itemconfig('Bullx',image=bulles[i])
                        ventana.after(50,lambda:BullxAni(i+1))

        def AlienAni(i):
                nonlocal alienes,contar, vidas, OPEN
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #Contador que detiene la animación
                        OPEN = False
                if (i==4):
                    i = 0
                if(OPEN == True):
                    c.itemconfig('alien',image=alienes[i])
                    ventana.after(50,lambda:AlienAni(i+1))

        def misilAni(i):
                nonlocal misilimg,contar,OPEN
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #Contador que detiene la animación
                        OPEN = False
                if (i==12):
                    i = 0
                if(OPEN == True):
                    c.itemconfig('misiles',image=misilimg[i])
                    ventana.after(50,lambda:misilAni(i+1))
        def vidaAni(i):
                nonlocal vides,contar, OPEN
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #Contador que detiene la animación
                        OPEN = False
                if (i==10):
                        i = 0
                if(OPEN == True):
                        c.itemconfig('vids',image=vides[i])
                        ventana.after(50,lambda:vidaAni(i+1))

        
        Thread(target = BullxAni,args =(0,)).start()
        Thread(target = AlienAni,args =(0,)).start()
        Thread(target = misilAni,args =(0,)).start()
        Thread(target = vidaAni,args =(0,)).start()

        #\\\\\\\\\\\\\\\\\\\\\\\\TECLAS\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        

        def apretadomov(event): #Verifica que se presione la tecla una sola vez
                nonlocal apretado,apretadoi,apretadow,apretadox
                if event.char == derecha and apretado == 0:
                        apretado =1
                        return teclas(event)
                if event.char == izquierda  and apretadoi == 0:
                        apretadoi = 1
                        return teclas(event)
                if event.char == saltar and apretadow == 0:
                        apretadow = 1
                        return teclas(event)
                if event.char == disparar and apretadox ==0:
                        apretadox = 1
                        return teclas(event)
                else:
                    None
                    

        def release(event): #Toma las variables globales == 1 necesarias, les asigna el valor de 0 y las pasa una vez a la funcion 'teclas' con el evento
                nonlocal apretado,apretadoi,apretadow
                if apretado ==1:
                    apretado = 0
                    return teclas(event)
                if apretadoi ==1:
                    apretadoi = 0
                    return teclas(event)
                if apretadow ==1:
                    apretadow = 0
                    return teclas(event)
                if apretadox ==1:
                    apretadow = 0
                
                return teclas(event)
                

        def teclas(event):
                nonlocal apretado,apretadoi,apretadow,apretadox, indicador, misillist
                coord = c.coords('Bullx')
                
                if event.char == derecha:                    #moverse para la derecha
                    if apretado ==1 and coord[0] >= 660:
                        c.move(Bullx,-5,0)
                    if apretado ==1:
                        c.move(Bullx,5,0)
                        c.after(25,lambda:teclas(event))

                if event.char == izquierda:                   #moverse para la izquierda
                    if apretadoi ==1 and coord[0] <=30:
                        c.move(Bullx,5,0)
                    if apretadoi ==1:
                        c.move(Bullx,-5,0)
                        c.after(25,lambda:teclas(event))
                        
                if event.char == saltar:                   #Salto
                    if apretadow== 1 and indicador == 'abajo':
                        indicador = 'arriba'
                        check(0,len(navelist),5)        #Colisión
                        return jump()
                
                if event.char == disparar:                    #Disparo
                    p = c.coords('Bullx')
                    balas = c.create_image(p[0],p[1]+5, image=bala)
                    laser.play()
                    check(balas,len(misillist),1)
                    check(balas,len(navelist),2)
                    check(balas,len(deslist),3)
                    
                    if apretadox == 1:
                            return bala_mov(balas)
                  
        def bala_mov(balas):                            #Movimiento de la bala
                if (c.coords(balas)) == []:             #Detecta si la vala se eliminó
                        return None
                if c.coords(balas)[1] == 85:
                    c.delete(balas)
                else:
                    c.move(balas,0,-20)
                    c.after(20,lambda:bala_mov(balas))
                    

        def jump():                                     #Mueve al jugador arriba
                if c.coords('Bullx')[1] <= 400.0:
                        return down()
                else:
                        c.move(Bullx,0,-10)
                        c.after(20,jump)
                        
                    
        def down():                                     #Mueve al jugador abajo
                nonlocal indicador
                if c.coords('Bullx')[1]!= 600:
                        c.move(Bullx,0,10)
                        c.after(15,down)
                else:
                    indicador = 'abajo'
                       
                       
                    
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ MOVER \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        '''MOVIMIENTO MISIL'''
        
        def mover_misil(): #crea el misil
                misil= c.create_image(randint(5,600),0,tags=('misiles'))
                misillist.append(misil)
                mover_misil_aux(misil,0)
                

        def mover_misil_aux(misil,x):#movimiento del misil
                p = c.coords(misil)
                if p == []:
                        return None
                elif  p[1] == 605:
                    c.delete(misil)
                    misillist.remove(misil)
                elif x<5:
                        x+=1
                        colisiona_misil(misil) #Colision
                        c.move(misil,0,5)
                        c.after(20,lambda:mover_misil_aux(misil,x))
                else:
                        c.move(misil,0,5)
                        c.after(20,lambda:mover_misil_aux(misil,x))

        '''MOVIMIENTO NAVE'''

        def mover_nave_der():
                Naves= c.create_image(-60,70,tags = ('alien'))
                navelist.append([Naves]+[3])
                mover_nave_der_aux(Naves,0)
                
        def mover_nave_der_aux(Naves,z):
                z+=1
                p = c.coords(Naves)
                disparon(Naves,2)
                
                if p == []: #Verifica que la nave exista
                        None
                elif p[0]<730: #revisa que este fuera del canvas 
                    return mover_nave_aux(Naves,z,0)
                else:
                        c.after(2,lambda:colisiona_nave(Naves))
                        mover_nave_aba(Naves,z,0)

        def mover_nave_aux(Naves,z,a): #mueve la nave hacia la derecha
                if z%2 != 0:
                        if a != 70:
                                a+=5
                                c.move(Naves,5,2)                                #mueve la nave en la derecha y la sube
                                c.after(30,lambda:mover_nave_aux(Naves,z,a))
                        else:
                                c.after(5,lambda:mover_nave_der_aux(Naves,z))
                                
                elif z%2 ==0:
                        if a != 70:
                                a+=5
                                c.move(Naves,5,-2)                              #mueve la nave a la derecha y la baja
                                c.after(30,lambda:mover_nave_aux(Naves,z,a))
                        else:
                                c.after(5,lambda:mover_nave_der_aux(Naves,z))
                                
        def mover_nave_iz(Naves,z,a): #mueve la nave hacia la izquierda
                disparon(Naves,2)
                z+=1
                if c.coords(Naves) == []: #Verifica que la nave exista
                        None
                elif c.coords(Naves) == [10.0, 462.0]: #Elimina la nave en la coordenada especificada
                        c.delete(Naves)
                
                elif  c.coords(Naves)[0]>0:
                    return mover_nave_aux_iz(Naves,z,a)
                else:
                    return mover_nave_aba(Naves,z,a)
                
        def mover_nave_aux_iz(Naves,z,a):
                if z%2 != 0:
                        if a != 70:
                                a+=5
                                c.move(Naves,-5,2)                               #mueve la nave a la izquierda y arriba
                                c.after(30,lambda:mover_nave_aux_iz(Naves,z,a))
                        else:
                                c.after(5,lambda:mover_nave_iz(Naves,z,0))
                elif z%2 ==0:
                        if a != 70:
                                a+=5
                                c.move(Naves,-5,-2)                             #mueve la nave a la izquierda y abajo 
                                c.after(30,lambda:mover_nave_aux_iz(Naves,z,a))
                        else:
                                c.after(5,lambda:mover_nave_iz(Naves,z,0))
                    
                    
        def mover_nave_aba(Naves,z,a): #mueve la nave abajo 
                p = c.coords(Naves)
                if p[0] > 400:                                                  #Detecta si la nave esta en la derecha
                        c.move(Naves,0,90)
                        c.after(300,lambda:mover_nave_aux_iz(Naves,z,a))
                else:                                                           #Detecta si la nave esta en la izquierda
                    c.move(Naves,0,90)
                    c.after(300,lambda:mover_nave_der_aux(Naves,z))

        def disparon(y,s): #Dispara 
                x = randint(1,7)
                if c.coords(y) == []:
                        None
                elif c.coords(y)[1] >=630:                                      #Detecta que la bala este en la coordenada especificada y la borra
                        c.delete(balaEnemy)
                elif s == x:
                        balaEnemy = c.create_image(c.coords(y)[0],c.coords(y)[1]-5, image=red)
                        colisionbaldes(balaEnemy)
                        disparon2(balaEnemy)

        def disparon2(balaEnemy):#Dispara
                if c.coords(balaEnemy) == []:
                        None
                elif c.coords(balaEnemy)[1] >=630:                                      #Detecta que la bala este en la coordenada especificada y la borra       
                        c.delete(balaEnemy)
                else:
                        c.move(balaEnemy,0,5)
                        c.after(15,lambda:disparon2(balaEnemy))

        '''MOVIMIENTO DESTRUCTOR'''
                    

        def mover_des(): #crea al destructor
                destructores= c.create_image(randint(55,620),0,image=crusherimg)
                colisiona(destructores)
                deslist.append([destructores]+[5])
                return mover_des_aux(destructores)

        
        def mover_des_aux(destructores):#mueve al destructor hacia abajo
                if c.coords(destructores) == []: #detecta que el destructor exista
                        None
                elif c.coords(destructores)[1]< 600:
                    c.move(destructores,0,5) 
                    c.after(15,lambda:mover_des_aux(destructores)) 
                elif c.coords(destructores)[1] == 600 and c.coords(destructores)[0] <= 340:#envia al destructor a moverce a la izquierda
                    mover_iz_des(destructores,0)
                else:
                    mover_der_des(destructores,0) #envia al destructor a moverce a la derecha 


        def mover_iz_des(destructores,o): #mueve al destructor a la izquierda
                if c.coords(destructores) == []: #detecta que el destructor exista
                        None
                elif c.coords(destructores)[0] <= 60 and o ==0:
                        c.after(100,c.move(destructores,-5,0))
                        balaEnemy2 = c.create_image(c.coords(destructores)[0]+20,c.coords(destructores)[1], image=red)
                        disparodes(balaEnemy2,1)
                        colisionbaldes(balaEnemy2)
                        c.after(20,lambda:mover_iz_des(destructores,1))
                        
                elif c.coords(destructores)[0] >= 0:
                    c.move(destructores,-5,0)
                    c.after(20,lambda:mover_iz_des(destructores,o))
                        
                else:
                        c.delete(destructores)


        def mover_der_des(destructores,o): #mueve al destructor a la derecha 
                
                if c.coords(destructores) == []: #detecta que el destructor exista
                        None
                elif c.coords(destructores)[0] >= 600 and o ==0:
                        c.after(100,c.move(destructores,-5,0))
                        balaEnemy2 = c.create_image(c.coords(destructores)[0]+20,c.coords(destructores)[1], image=red)
                        disparodes(balaEnemy2,2)
                        colisionbaldes(balaEnemy2)
                        c.after(20,lambda:mover_der_des(destructores,1))
                elif c.coords(destructores)[0] <= 720:
                    c.move(destructores,5,0)
                    c.after(20,lambda:mover_der_des(destructores,o))
                else:
                        c.delete(destructores)
                        

        def  disparodes(balaEnemy2,x): #Mueve la bala 
                if c.coords(balaEnemy2) == []:
                        None
                elif c.coords(balaEnemy2)[0] >=630:
                        c.delete(balaEnemy2)
                elif x == 1:
                        c.move(balaEnemy2,5,0)
                        c.after(15,lambda:disparodes(balaEnemy2,x))
                else:
                        c.move(balaEnemy2,-5,0)
                        c.after(15,lambda:disparodes(balaEnemy2,x))
                
                        
                        
        #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ COLISIONES \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
                        
        def check(balas,x,k):
                nonlocal misillist, navelist,deslist
                if x !=0:                                                #busca la posicion de la lista
                        x-=1
                        if k ==1:
                                colision_misil1(balas,x,len(misillist))        
                        if k ==2:
                                colision_nave1(balas,x,len(navelist))
                        if k ==3:
                                colision_destructor1(balas,x,len(deslist))
                                
                        check(balas,x,k)
                else:
                        None
                        
        def colision_misil1(balas,x,y):
                nonlocal misillist,contar
                a = len(misillist)

                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(misillist[x],balas)
                        del (misillist[x],balas)
                        
                elif a<y:
                        return None                                                    #compara el largo de la lista original con el largo de la lista presente
                        
                elif misillist!= []:
                        m = c.bbox(misillist[x])
                        b = c.bbox(balas)
                        if b == None or m == None:
                                return None
                        
                        elif (b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2]):
                                c.after(50,c.delete(misillist[x],balas))
                                del (misillist[x],balas)
                                score(label3,1)
                        else:
                                c.after(1,lambda:colision_misil1(balas,x,y))
                else:
                        None
        def colision_nave1(balas,x,y):
                nonlocal navelist,contar
                a = len(navelist)
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete((navelist[x][0]),balas)
                        del (navelist[x],balas)
                elif a<y: #compara el largo de la lista original con el largo de la lista presente
                        None       
                elif navelist!= []:
                        m = c.bbox(navelist[x][0])
                        b = c.bbox(balas)
                        if b == None:
                                None
                        elif m == None:
                                None
                        elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                                navelist[x][1]-=1
                                if navelist[x][1] == 0:
                                        c.after(1,c.delete(navelist[x][0]),balas)
                                        del (navelist[x],balas)
                                        score(label3,5)
                                else:
                                        c.after(50,c.delete(balas))
                                        del (balas)
                        else:
                                c.after(1,lambda:colision_nave1(balas,x,y))
                else:
                        None

        
     
                

        def colision_destructor1(balas,x,y):
                nonlocal deslist,contar
                a = len(deslist)
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(deslist[x][0],balas)
                        del (deslist[x],balas)
                elif a<y:                                                       #compara el largo de la lista original con el largo de la lista presente
                        return None
                elif deslist!= []:
                        m = c.bbox(deslist[x][0])
                        b = c.bbox(balas)
                        
                        if b == None:
                                None
                        elif m == None:
                                None
                        elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                                deslist[x][1]-=1
                                if deslist[x][1] == 0:
                                        c.after(50,c.delete(deslist[x][0],balas))
                                        del (deslist[x],balas)
                                        score(label3,20)
                                else:
                                        c.after(50,c.delete(balas))
                                        del (balas)
                        else:
                                c.after(1,lambda:colision_destructor1(balas,x,y))
                else:
                        None
        
        def colisiona(destructores):
                nonlocal vidas,contar
                m = c.bbox(destructores)
                b = c.bbox('Bullx')
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(destructores)
                elif m == None:
                        None  
                elif (((b[0]<m[0]<b[2] or b[0]<m[2]<b[2]) and b[1]<m[1]<b[3])or ((m[0]<b[0]<m[2]or m[0]<b[2]<m[2])and b[1]<m[1]<b[3])):
                        c.after(50,c.delete(destructores))
                        vidas -=1
                        return vida()
        
                elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                        c.after(50,c.delete(destructores))
                        vidas -=1
                        return vida()
                else:
                        c.after(1,lambda:colisiona(destructores))

        def colisiona_nave(Naves):
                nonlocal vidas,contar
                m = c.bbox(Naves)
                b = c.bbox('Bullx')
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(Naves)
                elif m == None:
                        None  
                elif (((b[0]<m[0]<b[2] or b[0]<m[2]<b[2]) and b[1]<m[1]<b[3])or ((m[0]<b[0]<m[2]or m[0]<b[2]<m[2])and b[1]<m[1]<b[3])):
                        c.after(50,c.delete(Naves))
                        vidas-=1
                        vida()
                elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                        c.after(50,c.delete(Naves))
                        vidas-=1
                        vida()
                else:
                        c.after(1,lambda:colisiona_nave(Naves))
                        
        def colisiona_misil(misil):
                nonlocal vidas,contar
                m = c.bbox(misil)
                b = c.bbox('Bullx')
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(misil)
                if m == None:
                        None  
                elif (((b[0]<m[0]<b[2] or b[0]<m[2]<b[2]) and b[1]<m[1]<b[3])or ((m[0]<b[0]<m[2]or m[0]<b[2]<m[2])and b[1]<m[1]<b[3])):
                        c.after(50,c.delete(misil))
                        vidas -=1
                        vida()
                elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                        c.after(50,c.delete(misil))
                        vidas -=1
                        vida()
                else:
                        c.after(1,lambda:colisiona_misil(misil))
                        
        def colisionbaldes(juan):
                nonlocal vidas,contar
                m = c.bbox(juan)
                b = c.bbox('Bullx')
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(juan)
                if m == None or b == None:
                        None  
                elif (((b[0]<m[0]<b[2] or b[0]<m[2]<b[2]) and b[1]<m[1]<b[3])or ((m[0]<b[0]<m[2]or m[0]<b[2]<m[2])and b[1]<m[1]<b[3])):
                        c.after(50,c.delete(juan))
                        vidas -=1
                        vida()
                elif ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (b[0]<m[2]<b[2] or b[0]<m[0]<b[2])) or ((b[3]<m[3]<b[1] or m[1]<b[1]<m[3]) and (m[0]<b[0]<m[2]or m[0]<b[2]<m[2])):
                        c.after(50,c.delete(juan))
                        vidas -=1
                        vida()
                else:
                        c.after(1,lambda:colisionbaldes(juan))

        
        def vida(): #Elimina las vidas
                nonlocal vidas,contar, GameOver, menu
                if contar == 40 or contar == 80 or contar == 120 or vidas == 0: #contador
                        c.delete(veds)
                        c.delete(vads)
                        c.delete(vids)
                        c.delete('falta')
                        c.delete(Bullx)
                        
                if vidas == 2:
                        c.create_image(117,673, image = hueco,tags ='falta')   #Eliminar vidas
                        c.delete(veds)
                        
                if vidas ==1:
                        c.create_image(87,673, image = hueco,tags ='falta')    #Eliminar vidas
                        c.delete(vads)
                        
                if vidas == 0: #Game Over
                        ventana.unbind("<"+derecha+">")
                        ventana.unbind("<"+izquierda+">")
                        ventana.unbind("<"+saltar+">")
                        ventana.unbind("<"+disparar+">")
                        ventana.unbind("<KeyRelease-"+derecha+">")
                        ventana.unbind("<KeyRelease-"+izquierda+">")
                        ventana.unbind("<KeyRelease-"+saltar+">")
                        ventana.unbind("<KeyRelease-"+disparar+">")
                        c.create_image(57,673, image = hueco,tags ='falta')
                        c.delete(vids)
                        good = Canvas(ventana,width=679, height=737, bg='black')
                        good.place(x=0,y=0) #canvas principal
                        good.image = cargarImg('GameOver.png') #fondo del canvas
                        fondo = good.create_image(340,337, image=good.image )
                        label5 = Label(ventana,text = str(b),bg = "#373A2F",fg = "white",font = ("MS Reference Sans Serif",12))
                        label5.place(x=270,y=360, width=110, height=20)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=menu, command = lambda:before2(good)).place(x=200,y=406)
                        
                        c.destroy()
                        
                else:
                        None
                
                
            

        #//////////////////////CONTADOR////////////////////////////
        
        def score(label3,l):
                nonlocal contar,b
                b += l
                label3.config(text='PUNTOS   '+(str(b)), font = ("MS Reference Sans Serif",7))
                
        def count(label2):
                nonlocal contar
                if contar == 40:
                        return None
                if contar == 80:
                        return None
                else:
                        contar+=1
                        label2.config(text='TIEMPO  '+(str(contar)), font = ("MS Reference Sans Serif",7))
                        c.after(1000,lambda:count(label2))

        def release_enemy(x):
                nonlocal contar, flag2
                z = 5
                y = 7
                h = 9
                if contar == 39 or contar ==79 or contar == 119:
                        return None
                if x == 0:
                        q = 25*flag2
                        a = randint(1,250-q) #hard 20
                        if z == a:
                                mover_misil()
                        if y == a:
                                mover_nave_der()
                        if h == a:
                                mover_des()
                        
                        c.after(50,lambda:release_enemy(x))

                if x == 2:
                        q = 25*flag2
                        a = randint(1,200)-q #hard 20
                        if z == a:
                                mover_misil()
                        if y == a:
                                mover_nave_der()
                        if h == a:
                                mover_des()
                        
                        c.after(50,lambda:release_enemy(x))

                if x == 3:
                        q = 25*flag2
                        a = randint(1,150-q) #hard 20
                        if z == a:
                                mover_misil()
                        if y == a:
                                mover_nave_der()
                        if h == a:
                                mover_des()
                        
                        c.after(50,lambda:release_enemy(x))
                        

                
                
        #///////////Abre el Menu//////                        
        
                        
        def finish_line(flag):
                nonlocal contar,grades,c,vidas,p,nex,menu, won
                if contar == 40:
                        ventana.unbind("<"+derecha+">")
                        ventana.unbind("<"+izquierda+">")
                        ventana.unbind("<"+saltar+">")
                        ventana.unbind("<"+disparar+">")
                        ventana.unbind("<KeyRelease-"+derecha+">")
                        ventana.unbind("<KeyRelease-"+izquierda+">")
                        ventana.unbind("<KeyRelease-"+saltar+">")
                        ventana.unbind("<KeyRelease-"+disparar+">")
                
                        key=1
                        good = Canvas(ventana,width=679, height=737, bg='black')
                        good.place(x=0,y=0) #canvas principal
                        good.image = cargarImg('click_next.png') #fondo del canvas
                        fondo = good.create_image(340,337, image=good.image )
                        label5 = Label(ventana,text = str(b),bg = "#373A2F",fg = "white",font = ("MS Reference Sans Serif",12))
                        label5.place(x=320,y=338, width=110, height=20)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=nex, command = lambda:before(good,key,flag)).place(x=336,y=415)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=menu, command = lambda:before2(good)).place(x=87,y=417)
                                               
                        c.destroy()
                elif contar == 80:
                        ventana.unbind("<"+derecha+">")
                        ventana.unbind("<"+izquierda+">")
                        ventana.unbind("<"+saltar+">")
                        ventana.unbind("<"+disparar+">")
                        ventana.unbind("<KeyRelease-"+derecha+">")
                        ventana.unbind("<KeyRelease-"+izquierda+">")
                        ventana.unbind("<KeyRelease-"+saltar+">")
                        ventana.unbind("<KeyRelease-"+disparar+">")
                        key=2
                        good = Canvas(ventana,width=679, height=737, bg='black')
                        good.place(x=0,y=0) #canvas principal
                        good.image = cargarImg('click_next.png') #fondo del canvas
                        fondo = good.create_image(340,337, image=good.image )
                        label5 = Label(ventana,text = str(b),bg = "#373A2F",fg = "white",font = ("MS Reference Sans Serif",12))
                        label5.place(x=320,y=338, width=110, height=20)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=nex, command = lambda:before(good,key,flag)).place(x=336,y=415)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=menu, command = lambda:before2(good)).place(x=87,y=417)
                        
                        c.destroy()

                elif contar >= 120:
                        ventana.unbind("<"+derecha+">")
                        ventana.unbind("<"+izquierda+">")
                        ventana.unbind("<"+saltar+">")
                        ventana.unbind("<"+disparar+">")
                        ventana.unbind("<KeyRelease-"+derecha+">")
                        ventana.unbind("<KeyRelease-"+izquierda+">")
                        ventana.unbind("<KeyRelease-"+saltar+">")
                        ventana.unbind("<KeyRelease-"+disparar+">")
                        good = Canvas(ventana,width=679, height=737, bg='black')
                        good.place(x=0,y=0) #canvas principal
                        good.image = cargarImg('won.png') #fondo del canvas
                        fondo = good.create_image(340,337, image=good.image )
                        label5 = Label(ventana,text = str(b),bg = "#373A2F",fg = "white",font = ("MS Reference Sans Serif",12))
                        label5.place(x=270,y=360, width=110, height=20)
                        boton = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=menu, command = lambda:before2(good)).place(x=200,y=406)
                        label7 = Label(ventana,bg = "#36392E",fg = "white")
                        label7.place(x=170,y=280, width=330, height=40)
                        ola(grades,9,[],label7)
                        
                        c.destroy()
                else:
                        c.after(1000,lambda:finish_line(flag))

        def before(good,key,flag): #cambio de canas
                nonlocal flag2, b
                good.destroy()
                flag2 +=1
                if key ==1:
                        juego(nombre,flag,41,flag2,b)
                if key == 2:
                        juego(nombre,flag,81,flag2,b)
                        

        def before2(good): #canvio de canvas
                good.destroy()
                principal()
        
                
                
                

        def write(x,y,h,label7):
                if x == y:
                        abrir.write(read[y])
                        abrir.close()
                        return anuncio(h,label7)
                elif y ==0:
                        abrir.seek(0)
                        abrir.write(read[y])
                        return  write(x,y+1,h,label7)
                else:
                        abrir.write(read[y])
                        return  write(x,y+1,h,label7)
        def anuncio(h,label7):
                if h == 6:
                        label7.config(text='Nuevo Record! Estas en la posicion 5', font = ("MS Reference Sans Serif",12))
                elif h == 7:
                        label7.config(text='Nuevo Record! Estas en la posicion 4', font = ("MS Reference Sans Serif",12))
                elif h == 8:
                        label7.config(text='Nuevo Record! Estas en la posicion 3', font = ("MS Reference Sans Serif",12))
                elif h == 9:
                        label7.config(text='Nuevo Record! Estas en la posicion 2', font = ("MS Reference Sans Serif",12))
                elif h == 10:
                        label7.config(text='Nuevo Record! Estas en el primer lugar!', font = ("MS Reference Sans Serif",12))
                else:
                        None
                        
                    
        def comparar(y,m,n,z,h,label7):
                nonlocal b,read,grades
        
        
                if b >y[n] and n == -1:
                        grades.insert(n+1,str(b)+'\n')
                        grades.remove(grades[z+1])
                        nombres2.insert(n+1,str(nombre)+'\n')
                        nombres2.remove(nombres2[z+1])
                        read[1::2] = grades
                        read[0::2] = nombres2
                        return write(19,0,h,label7)

                if b == y[n]:
                        grades.insert(n+1,str(b)+'\n')
                        grades.remove(grades[z+1])
                        nombres2.insert(n+1,str(nombre)+'\n')
                        nombres2.remove(nombres2[z+1])
                        read[1::2] = grades
                        read[0::2] = nombres2
                        return write(19,0,h,label7)
                        
                if b >y[n] and n != -1:
                        h +=1
                        return comparar(y,m,n-1,z,h,label7)
                if b <y[n] and n==z:
                        return None
                if b <y[n] and n!=z:
                        grades.insert(n+1,str(b)+'\n')
                        grades.remove(grades[z+1])
                        nombres2.insert(n+1,str(nombre)+'\n')
                        nombres2.remove(nombres2[z+1])
                        read[1::2] = grades
                        read[0::2] = nombres2
                        return write(19,0,h,label7)
                    
        def ola(lista, x,y,label7):
                if x == -1:
                        h = y[::-1]
                        return comparar( h, h,(len(h)-1),(len(h)-1),0,label7)
                else:
                        y.append(int(lista[x]))
                        return ola(lista,x-1,y,label7)
                                        
                        
                 
                
          
        ventana.bind("<"+derecha+">",apretadomov)
        ventana.bind("<"+izquierda+">",apretadomov)
        ventana.bind("<"+saltar+">",apretadomov)
        ventana.bind("<"+disparar+">",apretadomov)
        ventana.bind("<KeyRelease-"+derecha+">",release)
        ventana.bind("<KeyRelease-"+izquierda+">",release)
        ventana.bind("<KeyRelease-"+saltar+">",release)
        ventana.bind("<KeyRelease-"+disparar+">",release)
        label2 = Label(ventana,bg = "#211D20",fg = "white")
        label2.place(x=158,y=662, width=70, height=10)
        count(label2)
        label = Label(ventana,text = 'NOMBRE   '+p, bg = "#211D20",fg = "white",font = ("MS Reference Sans Serif",7) )
        label.place(x=133,y=682, width=110, height=12)
        label3 = Label(ventana,bg = "#211D20",fg = "white")
        label3.place(x=30,y=11, width=70, height=10)
        score(label3,0)
        finish_line(flag)
        cerrarImg = cargarImg('excit.png') #Imagen del boton de cerrar
        cerrar = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=cerrarImg,command=ventana.destroy).place(x=640, y=10)#Boton de cerrar
        release_enemy(flag)
        
        ventana.mainloop()

def nombre():
    global BotonImg,backImg,facilboton,normalboton,dificilboton
    backImg=cargarImg('Back.png')
    c = Canvas(ventana,width=679, height=737, bg='black')
    c.place(x=0,y=0)
    c.image = cargarImg('nombre.png') #fondo del canvas
    fondo1 = c.create_image(340,337, image=c.image )
    back = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=backImg,command=principal).place(x=235, y=552)
    e = Entry(c, highlightthickness=0,bd=0,relief=FLAT,bg = 'grey',fg = 'white',font = ("MS Reference Sans Serif",9))
    e.place(x=374, y=200)

    def play(x):
        global c_Principal
        nonlocal c 
        p = e.get()
        c_Principal.destroy()
        c.destroy()
        return juego(p,x,0,0,0)

    facilboton = cargarImg('facil.png') #Boton Credit
    boton4 = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=facilboton,command = lambda:(play(0))).place(x=110,y=395)
    
    normalboton = cargarImg('normal.png') #Boton Credit
    boton5 = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=normalboton,command = lambda:(play(2))).place(x=300,y=395)
    
    dificilboton = cargarImg('dificil.png') #Boton Credit
    boton6 = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=dificilboton,command = lambda:(play(3))).place(x=480,y=395)
    
def grade():
        '''
*****************************************************************************************************************************************************
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores

Programa: grade

Lenguaje y Versión: Python 3.8.3

Autora: Mariana Navarro Jiménez

Versión: 1.0

Fecha de ultima modificación: 12-07-2020

Entradas: ()

Salidas: Puntuacion de los jugadores

******************************************************************************************************************************************************
'''
        global backImg
        
        canvascore = Canvas(ventana,width=679, height=737, bg='black')
        canvascore.place(x=0,y=0)
        canvascore.image = cargarImg('scores.png') #fondo del canvas
        backImg=cargarImg('Back.png')
        fondo3 = canvascore.create_image(340,337, image=canvascore.image )

        abrir = open(r"score\scoreboard.txt",'r+')

        abrir.seek(0)
        read = abrir.readlines()

        play1 = Label(ventana,text = read[0], font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play1.place(x =230, y = 128, width=140, height=25)
        play1 = Label(ventana,text = read[1], font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play1.place(x =400, y = 128, width=140, height=25)
        
        play2 = Label(ventana,text = read[2],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play2.place(x =230, y = 163,width=140, height=25)
        play2 = Label(ventana,text = read[3],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play2.place(x =400, y = 163,width=140, height=25)

        play3 = Label(ventana,text = read[4],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play3.place(x =230, y = 198,width=140, height=25)
        play3 = Label(ventana,text = read[5],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play3.place(x =400, y = 198,width=140, height=25)

        play4 = Label(ventana,text = read[6],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play4.place(x =230, y = 233,width=140, height=25)
        play4 = Label(ventana,text = read[7],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play4.place(x =400, y = 233,width=140, height=25)

        play5 = Label(ventana,text = read[8],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play5.place(x =230, y = 268,width=140, height=25)
        play5 = Label(ventana,text = read[9],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play5.place(x =400, y = 268,width=140, height=25)

        play6 = Label(ventana,text = read[10],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play6.place(x =230, y = 303,width=140, height=25)
        play6 = Label(ventana,text = read[11],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play6.place(x =400, y = 303,width=140, height=25)
        
        play7 = Label(ventana,text = read[12],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play7.place(x =230, y = 338,width=140, height=25)
        play7 = Label(ventana,text = read[13],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play7.place(x =400, y = 338,width=140, height=25)

        play8 = Label(ventana,text = read[14],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play8.place(x =230, y = 373,width=140, height=25)
        play8 = Label(ventana,text = read[15],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play8.place(x =400, y = 373,width=140, height=25)

        play9 = Label(ventana,text = read[16],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play9.place(x =230, y = 410,width=140, height=25)
        play9 = Label(ventana,text = read[17],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play9.place(x =400, y = 410,width=140, height=25)

        play10 = Label(ventana,text = read[18],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play10.place(x =230, y = 445,width=140, height=25)
        play10= Label(ventana,text = read[19],font =("MS Reference Sans Serif",10),bg = "#36392E",fg = "white")
        play10.place(x =400, y = 445,width=140, height=25)

        back = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=backImg,command=principal).place(x=245, y=552)#Boton para volver atras



        
    
def prt(lista, x,y):
    if x == -1:
        h = y[::-1]
        return comparar( h, h,(len(h)-1),(len(h)-1))
    else:
        y.append(int(lista[x]))
        return prt(lista,x-1,y)
            


#CANVAS PRINCIPAL

def principal():
    """
*****************************************************************************************************************************************************
Instituto Tecnológico de Costa Rica
Ingenieria en Computadores

Programa: principal

Lenguaje y Versión: Python 3.8.3

Autora: Mariana Navarro Jiménez

Versión: 1.0

Fecha de ultima modificación: 12-07-2020

Entradas: ()

Salidas: Modulo de Abrir, Modulo de Nombre, Modulo de Score

******************************************************************************************************************************************************
"""
    global cerrarImg,BotonImg,BotonImg2,BotonImg3,BotonImg4,c_Principal
    

    c_Principal.image = cargarImg('Bullet.png') #fondo del canvas
    fondo = Label(ventana, image=c_Principal.image ).place(x=0, y=0)

    cerrarImg = cargarImg('excit.png') #Imagen del boton de cerrar
    cerrar = Button(ventana,highlightthickness=0,bd=0,image=cerrarImg,command=ventana.destroy).place(x=640, y=10)#Boton de cerrar

    BotonImg = cargarImg('Play.png') #Boton Play
    boton = Button(ventana,highlightthickness=0,bd=0,image=BotonImg,command=nombre).place(x=200,y=320)

    BotonImg2 = cargarImg('Capture.png') #Boton Scores
    boton2 = Button(ventana,highlightthickness=0,bd=0,image=BotonImg2,command = grade).place(x=232,y=430)

    BotonImg3 = cargarImg('Capture2.png') #Boton Help
    boton3 = Button(ventana,highlightthickness=0,bd=0,image=BotonImg3,command=lambda:(abrir(3))).place(x=238,y=520)

    BotonImg4 = cargarImg('Capture3.png') #Boton Credit
    boton4 = Button(ventana,highlightthickness=0,bd=0,image=BotonImg4,command=lambda:abrir(4) ).place(x=227,y=607)


    
def abrir(x):
    c_prin2 = Canvas(ventana, width=679, height=737, bg='black') #canvas con información de ayuda
    c_prin2.place(x=0,y=0)
    global backImg, derecha, izquierda, saltar, disparar
    backImg=cargarImg('Back.png')
    if x == 3:
        def bindiz_aux(event):
                global izquierda
                izquierda = str(event.char)
                botoniz.configure(text = izquierda)
                
        def binder_aux(event):
                global derecha
                derecha = str(event.char)
                botonder.configure(text = derecha)
        def bindar_aux(event):
                global saltar
                saltar = str(event.char)
                botonw.configure(text = saltar)
        def bindisp_aux(event):
                global disparar
                disparar = str(event.char)
                botondisp.configure(text = disparar)
                        
        def bindder(x):
                if x ==1:
                        ventana.bind('<Key>', binder_aux)
                if x ==2:
                        ventana.bind('<Key>', bindiz_aux)
                if x ==3:
                        ventana.bind('<Key>', bindar_aux)
                if x ==4:
                        ventana.bind('<Key>', bindisp_aux)
        
        c_prin2.image1 = cargarImg('HELP.png') #fondo del canvas de infromacion de ayuda
        fondo1 = c_prin2.create_image(340,350,image = c_prin2.image1 )
        botonder = Button(ventana,width=5, height=2,text = str(derecha),bg = "#211D20",fg = 'white', command = lambda:bindder(1))
        botonder.place(x=470,y=280)
        botoniz = Button(ventana,width=5, height=2,text = str(izquierda),bg = "#211D20",fg = 'white',command = lambda:bindder(2))
        botoniz.place(x=420,y=280)
        botonw = Button(ventana,width=5, height=2,text = str(saltar),bg = "#211D20",fg = 'white',command = lambda:bindder(3))
        botonw.place(x=420,y=225)
        botondisp= Button(ventana,width=5, height=2,text = str(disparar),bg = "#211D20",fg = 'white',command = lambda:bindder(4))
        botondisp.place(x=540,y=225)
        

        cerrar = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=cerrarImg,command=ventana.destroy).place(x=640, y=10) #Boton de cerrar
        back = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=backImg,command=principal).place(x=245, y=552)#Boton para volver atras
        
        
      

 
    elif x == 4:
        c_prin2.image = cargarImg('informacion_co.png') #fondo del canvas de infromacion complementacria
        fondo = c_prin2.create_image(340,337,image = c_prin2.image )
        cerrar = Button(ventana,highlightthickness=0,bd=0,image=cerrarImg,command=ventana.destroy).place(x=640, y=10)#Boton de cerrar
        back = Button(ventana,anchor=NW,highlightthickness=0,bd=0,relief=FLAT,image=backImg,command=principal).place(x=266, y=605)#Boton para volver atras
        
def mi_auto_doc():
        print(juego.__doc__)
        print(principal.__doc__)
        print(grade.__doc__)

principal()
mi_auto_doc()



