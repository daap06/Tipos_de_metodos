import random
from modulos.personajes import Personaje

class Jugar:
    
    @staticmethod
    def juego():
        print("¡Bienvenido a Gran Fantasía!\n")
        nombre_personaje = input("Ingrese nombre de su personaje : \n")
        personaje1 = Personaje(nombre_personaje)  
        print(personaje1.estado)
        orco = Personaje("Orco")
        print(orco.estado)
        
        opcion_juego = Personaje.enfrentamiento_con_orco(personaje1, orco)
        
        while opcion_juego == "1":
            resultado_ataque = random.uniform(0,1) <= personaje1.probabilidad(orco)
            if resultado_ataque:
                print("¡Le has ganado al orco, felicidades!")
                print(f"¡Recibirás 50 puntos de experiencia!")
                personaje1.calcular_exp_niv(50)
                orco.calcular_exp_niv(-30)
                print(personaje1.estado)
                print(orco.estado)
            else:
                print("¡Oh no! ¡El orco te ha ganado!")
                print("¡Has perdido 30 puntos de experiencia!")
                personaje1.calcular_exp_niv(-30)
                orco.calcular_exp_niv(50)
                print(personaje1.estado)
                print(orco.estado)
            opcion_juego = Personaje.enfrentamiento_con_orco(personaje1, orco)
                
        if opcion_juego == "2":
            print("¡Has huido! El orco ha quedado atrás.")
        else:
            print("Debe ingresar un valor comprendido entre 1 y 2.")