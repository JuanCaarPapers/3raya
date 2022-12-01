
import pandas as pd
import numpy as np
import sys

def titulo():
    print(   "______ _                           _     _               _    _____" +                                    
          "\n | ___ (_)                         (_)   | |             | |  |____ |" +                                    
          "\n | |_/ /_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |      / /   ___ _ __    _ __ __ _ _   _  __ _ "+
          "\n | ___ | |/ _ | '_ \ \ / / _ | '_ \| |/ _` |/ _ \   / _` | |      \ \  / _ | '_ \  | '__/ _` | | | |/ _` |"+
          "\n | |_/ | |  __| | | \ V |  __| | | | | (_| | (_) | | (_| | |  .___/ / |  __| | | | | | | (_| | |_| | (_| |"+
          "\n \____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|  \____/   \___|_| |_| |_|  \__,_|\__, |\__,_|"+
          "\n                                                                                               __/ |     "+
          "\n                                                                                               |___/     "
        )

#METODO DEL MENU
def menu():
    try:
        opcion = int(input('\n 1. Juego 2.Instrucciones 3.Salir\nSelecciona un apartado del menú introduciendo su número asociado \n'))
    except ValueError:
        print('\nPor favor selecciona una opción valida')
        return menu()
    else:
        if(opcion == 1 or opcion == 2 or opcion == 3):
            return opcion
        else: 
            return menu()

#METODO SALIR
def terminar():
    print('ahora te sales del juego xdddd')
    sys.exit()



#METODO INSTRUCCIONES
def instrucciones():
    print('Bienvenido al tres en raya versión python, el típico juego porteado a python.' +
          '\n Para comenzar una nueva partida selecciona en el menú principal la opcción uno "jugar"' +
          '\n a continuación selecciona tu y tu oponente las fichas que quereis usar, el juego comienza.' +
          '\n Ir, por turnos, escogiendo como se indica en la pequeña interfaz de texto el sitio en el que'+
          '\n quereís poner vuestras fichas, la partida acaba cuando uno de los dos rivales consigue 3 tres'+
          '\n fichas consecutivas en raya. !Buena suerte¡ \n '
        )
    try: 
        selecion_inst = int(input('introduce 1 para volver al menú principal \n'))
        if selecion_inst == 1:
            titulo()
            menu()
        while(selecion_inst != 1):
            print('Selecciona una opción valida \n')
            instrucciones()
    except ValueError:
        print('por favor selecciona una opción valida \n')
        instrucciones()

#SELECCION DE PIEZA

def selec_pieza():
    print('Bienvenidos al tres en raya, jugador 1 selecciona una pieza:'+
          '\n Según la pieza elegida, el jugador 2 jugará con la restante.'+
          '\n             1: X  2: O \n')
    seleccion = int(input('introduce la pieza con la que quieres jugar, 1 o 2 \n'))
    if seleccion == 1:
        return 'X'
    elif seleccion == 2: 
        return 'O'

#METODO TABLERO
   
def rellenar_tablero(figura):
    fila = (input('¿Qué fila quieres rellenar?'))
    columna = input('¿Qué columna quieres rellenar?').upper()

    #Para la fila 1
    if fila == '1' and columna == 'A':
        fila1[0] = figura
    elif fila == '1' and columna == 'B':
        fila1[1] = figura
    elif fila == '1' and columna == 'C':
        fila1[2] = figura

    #Para la fila 2
    elif fila == '2' and columna == 'A':
        fila2[0] = figura
    elif fila == '2' and columna == 'B':
        fila2[1] = figura
    elif fila == '2' and columna == 'C':
        fila2[2] = figura

    #Para la fila 3 
    elif fila == '3' and columna == 'A':
        fila3[0] = figura
    elif fila == '3' and columna == 'B':
        fila3[1] = figura
    elif fila == '3' and columna == 'C':
        fila3[2] = figura

#BUCLE FOR PARA DETECTAR LA VICTORIA DE UN JUGADOR
def evalua(figura):
    tab = [fila1.copy(), fila2.copy(), fila3.copy()]
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if tab[i][j] != figura:
                tab[i][j] = ''

    if figura == 'X':
        #print('EVALUA: ',tab in victoria_x)
        return tab in victoria_x
    else:
        #print('EVALUA: ',tab in victoria_O)
        return tab in victoria_O

#METODO DE JUEGO
def juego():
    jug1 = selec_pieza() 
    if jug1 == 'X':
        jug2 = 'O'
    else:   
        jug2 = 'X'
    tablero = pd.DataFrame([fila1,fila2,fila3],columns=['A','B','C'],index=['1','2','3'])
    print(tablero)
    while(True):
        rellenar_tablero(jug1)
        tablero = pd.DataFrame([fila1,fila2,fila3],columns=['A','B','C'],index=['1','2','3'])
        print(tablero)
        if(evalua(jug1)):
            break
        rellenar_tablero(jug2)
        tablero = pd.DataFrame([fila1,fila2,fila3],columns=['A','B','C'],index=['1','2','3'])
        print(tablero)
        if(evalua(jug1)):
            break
    if evalua(jug1):
        print('ha ganao j1')
    else:
        print('ha ganao j2')


#LISTAS PARA EL TABLERO
fila1 = ['','','']
fila2 = ['','','']
fila3 = ['','','']

#LISTAS DE POSIBILIDADES DE VICTORIAS PARA COMPARAR Y DETECTAR CON EVAL 
victoria_x = [
    [['X','X','X'],['','',''],['','','']],
    [['','',''],['X','X','X'],['','','']],
    [['','',''],['','',''],['X','X','X']],
    [['X','',''],['X','',''],['X','','']],
    [['','X',''],['','X',''],['','X','']],
    [['','','X'],['','','X'],['','','X']],
    [['X','',''],['','X',''],['','','X']],
    [['','','X'],['','X',''],['X','','']]]

victoria_O = [
    [['O','O','O'],['','',''],['','','']],
    [['','',''],['O','O','O'],['','','']],
    [['','',''],['','',''],['O','O','O']],
    [['O','',''],['O','',''],['O','','']],
    [['','O',''],['','O',''],['','O','']],
    [['','','O'],['','','O'],['','','O']],
    [['O','',''],['','O',''],['','','O']],
    [['','','O'],['','O',''],['O','','']]]

titulo()

#BUCLE PRINCIPAL
while(True):
        opcion = menu()
        if opcion == 1:
            juego()
        elif opcion == 2:
            instrucciones()
        elif opcion == 3:
            terminar()
else:
    print('Por favor selecciona una opción valida \n')
    menu()
    rellenar_tablero()