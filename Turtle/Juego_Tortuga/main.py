import turtle 
from Acciones import Screen,Player,Settings,Game

if __name__ == "__main__":
    #Root
    root = Screen()
    root.attrs()

    #Player One
    player_one = Player()
    player_one.attrs_player("white")
    player_one.move_player("up")

    #Player Two
    player_two = Player()
    player_two.attrs_player("green")
    player_two.move_player("down")

    #Settings
    name_turtle_one = Settings()
    name_turtle_two = Settings()

    #Init game 
    acu_1 = acu_2 = 0
    controlador_turnos = 0
    while acu_1 <= 28 and acu_2 <= 28:
        iniciar = Game(str(name_turtle_one), str(name_turtle_two))
        pasos = iniciar.calcular(controlador_turnos)
        if controlador_turnos % 2 == 0:
            player_one.avanzar(pasos)
            print("-> FIRST: ",acu_1)
            acu_1 += pasos
        else:
            player_two.avanzar(pasos)
            print("-> SECOND: ",acu_2)
            acu_2 += pasos
        controlador_turnos += 1
        
    #Finish Root
    turtle.done()