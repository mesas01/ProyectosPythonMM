# Jefe_final.py**************************************************************#
#                                                                            #
#                                     Jefe_final                             #
#                                                                            #
#                       This code was designed in order to solve a exam      #
#                       for Master Mind Academy for the first part of        #
#                       the python course                                    #
#                                                                            #
#                        DEVELOPED BY: Santiago Mesa (COL)                   #
#                                      mesasantiago5@gmail.com               #
#                                                                            #
#                        Bogota, D.C., December 24th, 2020.                  #
#                                                                            #
#          Copyright (C): Santiago Mesa                                      #
#                        Bogota - Colombia - South America                   #
#                                                                            #
# ***************************************************************************#

import random

llave_inglesa = False
bandera = True
examen_final = '\nPrograma final para la primera parte del curso\n'
print(examen_final + '°' * len(examen_final))

print('''Hola espadachin, lastimoamente te atraparon en tu ultima   
mision y te encuentras dentro de una prision Rusa, tu 
deber es escapar sano y salvo con los planos de los 
bunkers nucleares, buena suerte y elije sabiamente.\n''')

input('Presiona <enter> para continuar')
print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
print('''Estas aturdido no ves casi nada pero te encuentras una
llave inglesa rota, no apretara ningun tornillo pero 
hey es roja... la llevas contigo?\n''')

while bandera:
    opcion = input('Si --> S / No --> N : ')
    print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    if opcion == 'S':
        llave_inglesa = True
        print('Decidiste llevar la llave, tal vez sea nuestro unico amigo')
        input('\nPresiona <enter> para continuar')
        print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        bandera = False
    elif opcion == 'N':
        llave_inglesa = False
        print('Decidiste no llevarla, igualmente estaba rota quien la necesitaria? pff paso')
        input('\nPresiona <enter> para continuar')
        print('|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
        bandera = False
    else:
        print('No escogiste una opcion valida, intenta de nuevo')
        bandera = True

print('''Bien, ya te recuperaste, bueno... lo suficiente para 
hallar una salida, hay 2 opciones una ventilacion y un 
hoyo en el suelo, en ninguno se puede ver que hay del otro lado. ¿cual escoges?''')
bandera = True

while bandera:
    opcion = input('\nVentilacion --> V / hoyo --> H : ')
    print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
    if opcion == 'V':
        print('''Esto esta muy estrecho, apenas cabes pero distingues 
una luz en la lejania, avanzas un poco mas y te das 
cuenta que estas a 200 metros de altura, ¿saltas a la nieve? a lo mejor amortigua tu caida\n''')

        while bandera:
            opcion = input('Saltar --> S / No hacerlo --> N : ')
            print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||°')
            if opcion == 'S':
                print('''Vas a saltar, estas decidido, UNO... DOS.. TREEEE OH OH\n
te resbalaste justo antes de saltar y estas cayendo, 
al vacio tratas corregir tu trayectoria y caer en la
nieve pero !BOOOM¡ caiste en el lago congelado, has 
muerto agente, tu pais lo lamenta...\n
Adios''')
                input('\nPresiona <enter> para continuar')
                print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                exit()

            elif opcion == 'N':
                print('''Tienes razon, es muy arriesgado, mejor deberiamos volver OH-OH AHHHHH te resbalaste
                 y estÃ¡s cayendo sin control alguno, no puedes ver nada, estas a pundo de chocar pero...
                 ¿que pasa? caiste en la nieve por alguna razon, sobreviviste, felicidades!!! puedes escapar.''')

                print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                print('''\nLlegaste a tu pais a salvo, te preguntan por los planos, pero no los tienes, eres 
                una decepcion, por ti los rusos nos atacan mandando misiles, moriremos todos...''')
                input('\nPresiona <enter> para continuar')
                exit()
            else:
                print('No escogiste una opcion valida, intenta de nuevo')
                bandera = True

    elif opcion == 'H':
        print('''Escogiste el hollo, tienes que saltar, 1... 2... 3... caiste un piso pero un guardia 
        te vio, rapido!!! hay que noquearlo si tan solo tuvieros algo duro...''')
        input('\nPresiona <enter> para continuar')
        print('\nÂ°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°Â°')

        if llave_inglesa:
            print('''Uff menos mal trajiste la llave, rapido! noquealo... bien hecho podemos continuar''')
            input('\nPresiona <enter> para continuar')
            print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
            print('''Ahora que el guardia esta noqueado puedes intercambiar atuendos con el, no se parecen
             mucho, pero podria funcionaar.''')
            opcion = input('¿Deseas cambiar de atuendos?\n '
                           'Si --> S / No --> N: ')
            while bandera:
                if opcion == 'S':
                    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                    print('''Rapido puede que alguien te vea, sal ahora de la oficina del guardia''')
                    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                    input('\nPresiona <enter> para continuar')
                    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                    print('''Sales de la ofina y te encuentras con un monton de guardias, por suerte nadie 
                    socializa mucho y no saben que escapaste, te aproximas a la puerta de la oficina de planos
                    pero esta encriptada con una super operacion aritmetica y solo tienes un intento\n''')

                    print('(2 * 5/8 + 78 - 77 + 214 - ', random.randint(1, 10), ') * 0 + 1')
                    operacion = int(input('Respuesta: '))
                    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                    if operacion == '1':
                        print('''Correcto, pero como los guardias saben que eres un genio te tendieron una 
                        trampa, se activaron las armas... estas muerto''')
                        input('\nPresiona <enter> para continuar')
                        print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                        exit()
                    else:
                        print('''Que inteligente, seguro que si respondias esa dificilisima operacion
                        iban a a saber que eras tu ya que aqui nadi es es un genio... hurra, se abrio la puerta
                        toma los planos y hulle silenciosamente''')
                        print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                        print('ultima decicion, hay 2 puertas la trasera y la frontal, por cual sales')
                        opcion = input('Principal --> P / Trasera --> T: ')
                        if opcion == 'P':
                            print('''Es muy arriesgado, pero como eres un super agente salir por la puerta grande es lo 
                            tuyo Felicidades, Salvaste al mundo entero, eres un heroe, te dan la llave del
                            pais y seras recordado por siempre''')
                            exit()

                        else:
                            print('''La puerta pequenia esta bien, pero no era una puerta a la libertad, estan los 
                            perros Se ven enojados y no tienes proteccion, casi lo logras, pero no esta vez.... 
                            suerte''')
                            exit()

                elif opcion == 'N':
                    print('''El tiempo corre, no hay que perder tiempo, de igual manera te pueden reconocer
                    y te meterian en maxima seguridad y no queremos eso''')
                    print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')
                    input('\nPresiona <enter> para continuar')
                    print('Sales y oh oh el pasillo esta¡ lleno de guardias, solo te reconocen por la ropa, corre'
                          '\n no alcanzaste a escapar, ahora estas en maxima seguridad, buen intento, espia...')
                    exit()
                else:
                    print('No escogiste una opcion valida, intenta de nuevo')
                    bandera = True

        else:
            print('''OH-OH Â¿NO TRAJISTE LA LLAVE?!!! ya valiÃ³... el guardia viene hacia aca, 
            le intentas dar un golpe pero te derriba, ahora etas en maxima seguridad, no volveras
            a ver la luz del dia...''')
            exit()

    else:
        print('No escogiste una opcion valida, intenta de nuevo')
        bandera = True
