class Personaje:
    
    def __init__(self, nombre, nivel = 1, experiencia = 0) -> None:
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        
    @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXPERIENCIA: {self.experiencia}\n"
    
    # Aca cambio los valores obtenidos del property.
    @estado.setter
    def estado(self, nombre, nivel, experiencia):
        self.nombre = nombre
        self.nivel = nivel
        self.experiencia = experiencia
        
        
    def calcular_exp_niv(self,experiencia):
        # Aumento experiencia en función de si es positiva.
        if experiencia >= 0:
            self.experiencia += experiencia
            self.nivel += self.experiencia //100 #Divido entre 100 la experiencia para obtener los niveles que subió el personaje.
            self.experiencia %= 100 #El residio sera el valor de la experiencia restante.
        else:
            #En caso de ser negativa la experiencia del personaje
            if self.nivel > 1 or self.experiencia > 0:
                self.experiencia += experiencia
                while self.experiencia < 0:
                    # self.experiencia += 100
                    self.nivel -= 1
                    if self.nivel < 1:
                        self.nivel = 1
                        self.experiencia = 0
                        
    #Sobrecarga de menor que.                  
    def __lt__(self, otro_personaje):
        return self.nivel < otro_personaje.nivel 

    #Sobrecarga de mayor que.
    def __gt__(self, otro_personaje):
        return self.nivel > otro_personaje.nivel   
    
    #Sobrecarga de igual que.
    def __eq__(self, otro_personaje):
        return self.nivel == otro_personaje.nivel      
    
    #Metodo de la instancia para calcular probabilidad de un personaje.
    def probabilidad(self, otro_personaje):
        if self.nivel > otro_personaje.nivel:
            return 0.66
        elif self.nivel < otro_personaje.nivel:
            return -0.33
        else:
            return 0.50
        
    def enfrentamiento_con_orco(personaje,orco):
        probabilidad = personaje.probabilidad(orco)
        print(f"""¡Oh no!, ¡Ha aparecido un Orco!
            Con tu nivel actual, tienes {probabilidad*100}% de ganarle al Orco.
            
            Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
            Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.""")
        
        eleccion = input("""¿Qué deseas hacer?
                        1. Atacar
                        2. Huir
                        """)
        return eleccion


