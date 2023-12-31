#! /usr/bin/env python
import os
import pygame
from pygame.locals import *
from configuracion import *
from funcionesRESUELTAS import *
from extras import *

#Lee el archivo y devuelve una lista con los productos
lsProd = lectura()

def main():
    # Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    
    favicono = pygame.image.load("imagenes/green-pixel-dollar-symbol.png")
    pygame.display.set_icon(favicono)
    
    #Cargo las imagenes para los botones y la escalo a un tamaño apropiado
    imagenVerde = pygame.image.load("imagenes\marco-verde.png")
    imagenVerde = pygame.transform.scale(imagenVerde, (500,60))
    imagenAzul = pygame.image.load("imagenes\marco-azul.png")
    imagenAzul = pygame.transform.scale(imagenAzul, (500,60))

    #Preparamos los sonidos
    pygame.mixer.init()
    erro = pygame.mixer.Sound("audios/quit.wav")
    tecla = pygame.mixer.Sound("audios/tecla.wav")
    correcto = pygame.mixer.Sound("audios/correcto.wav")
    
    #defino el texto en el borde de la ventana
    pygame.font.init() #REVISAR

    # Preparar la ventana
    pygame.display.set_caption("Peguele al precio")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    # tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    puntos = 0  # puntos o dinero acumulado por el jugador
    producto_candidato = ""
    carrito = []

    lista_productos = lsProd  # lista de productos  

    # Elegir un producto, [producto, calidad, precio]
    producto = dameProducto(lista_productos, MARGEN)

    # Elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio. De manera aleatoria se debera tomar el valor economico o el valor premium. Agregar  '(economico)' o '(premium)' y el precio
    productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
    # print(productos_en_pantalla)

    # la funcion dibu muestra tanto el producto principal como el timer y el score
    dibu(screen,productos_en_pantalla,producto,producto_candidato,puntos,segundos)
    
    #la funcion asignar botones devuelve una lista de botones configurados y listos para su uso
    lista_botones = asignar_botones(productos_en_pantalla,imagenVerde,producto)

    while segundos > fps/1000:
        # 1 frame cada 1/fps segundos
        gameClock.tick(fps)
        totaltime += gameClock.get_time()

        if True:
            fps = 3

        posicion_mouse = pygame.mouse.get_pos()

        # Buscar la tecla apretada del modulo de eventos de pygame
        for e in pygame.event.get():

            # QUIT es apretar la X en la ventana
            if e.type == QUIT:
                pygame.quit()
                return ()

            # Ver si fue apretada alguna tecla
            if e.type == KEYDOWN:
                tecla.play()
                letra = dameLetraApretada(e.key)
                producto_candidato += letra  # va concatenando las letras que escribe
                if e.key == K_BACKSPACE:
                    # borra la ultima
                    producto_candidato = producto_candidato[0:len(producto_candidato)-1]
                if e.key == K_RETURN:  # presionó enter
                    indice = int(producto_candidato)
                    # chequeamos si el prducto no es el producto principal. Si no lo es procesamos el producto
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        #Si procesar no retorna 0, esto significa que el usuario sumo puntos. Reproducimos un sonido de "acierto"
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                        # Elegir un producto
                        producto = dameProducto(lista_productos, MARGEN)
                        # elegimos productos aleatorios, garantizando que al menos 2 mas tengan el mismo precio
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)
                    else:
                        producto_candidato = ""
            #si el evento es el click
            if e.type == pygame.MOUSEBUTTONDOWN:
                #si el click es en el boton que corresponde al indice 0 de la lista
                if lista_botones[0].checkForInput(posicion_mouse):
                    producto_candidato = '1'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                            
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""

                #si el click es en el boton que corresponde al indice 1 de la lista
                if lista_botones[1].checkForInput(posicion_mouse):
                    producto_candidato = '2'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""
                
                #si el click es en el boton que corresponde al indice 2 de la lista
                if lista_botones[2].checkForInput(posicion_mouse):
                    producto_candidato = '3'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""                    

                #si el click es en el boton que corresponde al indice 3 de la lista
                if lista_botones[3].checkForInput(posicion_mouse):
                    producto_candidato = '4'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""                   
                
                #si el click es en el boton que corresponde al indice 4 de la lista
                if lista_botones[4].checkForInput(posicion_mouse):
                    producto_candidato = '5'
                    indice = int(producto_candidato)
                    if indice < len(productos_en_pantalla) and indice != 0:
                        puntos += procesar(producto, productos_en_pantalla[indice], MARGEN)
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) != 0:
                            carrito.append(productos_en_pantalla[indice])
                            correcto.play()
                        if procesar(producto, productos_en_pantalla[indice], MARGEN) == 0:
                            erro.play()
                        producto_candidato = ""
                    
                        producto = dameProducto(lista_productos, MARGEN)
                        productos_en_pantalla = dameProductosAleatorios(producto, lista_productos, MARGEN)

                    else:
                        producto_candidato = ""  

        # Descomenar esto hace que no se repitan los productos en toda una sesion. Problema: A la doceava ronda nos quedamos sin productos.
        #  lista_productos = listaSinLosProductosAnteriores(lista_productos,productos_en_pantalla)

        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

        # Limpiar pantalla anterior
        screen.fill(COLOR_FONDO)

        # dibuja los nuevos parametros
        dibu(screen,productos_en_pantalla,producto,producto_candidato,puntos,segundos)
        lista_botones = asignar_botones(productos_en_pantalla,imagenVerde,producto)

        # actualiza cada boton asegurandose de que cada vez que el cursor pase por encima de un boton, sus letras cambien de color
        for boton in lista_botones:
            boton.changeColor(posicion_mouse)
            boton.update()
        
        pygame.display.update()  
        pygame.display.flip()
        
        if segundos <= 0:
            carrito_en_pantalla = mostrarCarrito(carrito)
            print(carrito_en_pantalla)
        
    while 1:
        # Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:

                pygame.quit()
                return


# Programa Principal ejecuta Main
if __name__ == "__main__":
    main()