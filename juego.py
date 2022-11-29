#METODO SALIR
def terminar():
    print('ahora te sales del juego xdddd')
#METODO DEL JUEGO
def juego():
    print('ahora empezaría el juego')
#METODO DEL MENU
def menu():
    print(   "______ _                           _     _               _    _____" +                                    
          "\n | ___ (_)                         (_)   | |             | |  |____ |" +                                    
          "\n | |_/ /_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |      / /   ___ _ __    _ __ __ _ _   _  __ _ "+
          "\n | ___ | |/ _ | '_ \ \ / / _ | '_ \| |/ _` |/ _ \   / _` | |      \ \  / _ | '_ \  | '__/ _` | | | |/ _` |"+
          "\n | |_/ | |  __| | | \ V |  __| | | | | (_| | (_) | | (_| | |  .___/ / |  __| | | | | | | (_| | |_| | (_| |"+
          "\n \____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_|  \____/   \___|_| |_| |_|  \__,_|\__, |\__,_|"+
          "\n                                                                                               __/ |     "+
          "\n                                                                                               |___/     "+
          "\n 1. Juego 2.Instrucciones 3.Salir'"
         )
    seleccion = input('Selecciona un apartado del menú introduciendo su número asociado \n')
    try:
        seleccion = int(seleccion)
        if seleccion == 1:
            juego()
        elif seleccion == 2:
            instrucciones()
        elif seleccion == 3:
            terminar()
        else:
            print('Por favor selecciona una opción valida \n')
            return menu()
    except ValueError:
                    print('Por favor selecciona una opción valida \n')
                    menu()
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
            menu()
        while(selecion_inst != 1):
            print('Selecciona una opción valida \n')
            instrucciones()
    except ValueError:
                    print('por favor selecciona una opción valida \n')
                    instrucciones()

menu()
def x():
    print('X   X'+
        '\n  X  '+
     '\nX  X' )
