def menu():
    print(   "______ _                           _     _               _   _____" +                                    
          "\n | ___ (_)                         (_)   | |             | | |____ |" +                                    
          "\n | |_/ /_  ___ _ ____   _____ _ __  _  __| | ___     __ _| |     / /   ___ _ __    _ __ __ _ _   _  __ _ "+
          "\n | ___ | |/ _ | '_ \ \ / / _ | '_ \| |/ _` |/ _ \   / _` | |     \ \  / _ | '_ \  | '__/ _` | | | |/ _` |"+
          "\n | |_/ | |  __| | | \ V |  __| | | | | (_| | (_) | | (_| | | .___/ / |  __| | | | | | | (_| | |_| | (_| |"+
          "\n \____/|_|\___|_| |_|\_/ \___|_| |_|_|\__,_|\___/   \__,_|_| \____/   \___|_| |_| |_|  \__,_|\__, |\__,_|"+
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
            print('por favor selecciona una opción valida')
            return menu()
    except ValueError:
                    print('por favor selecciona una opción valida')
                    menu()

def instrucciones():
    print('Bienvenido al tres en raya versión python, el típico juego porteado a python.' +
          '\n Para comenzar una nueva partida selecciona en el menú principal la opcción uno "jugar"' +
          '\n a continuación selecciona tu y tu oponente las fichas que quereis usar, el juego comienza.' +
          '\n Ir, por turnos, escogiendo como se indica en la pequeña interfaz de texto el sitio en el que'+
          '\n quereís poner vuestras fichas, la partida acaba cuando uno de los dos rivales consigue 3 tres'+
          '\n fichas consecutivas en raya. !Buena suerte¡ \n '
        )
    def sleccion_instr():      
        selecion_inst = int(input('introduce 1 para volver al menú principal \n'))
        if selecion_inst == 1:
            menu()
        else:
            print('por favor selecciona 1 para volver al menu principal')
            return sleccion_instr()
    sleccion_instr()


def terminar():
    print('ahora te sales del juego xdddd')

def juego():
    print('ahora empezaría el juego')

menu()
