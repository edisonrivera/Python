from tabnanny import check
import PySimpleGUI as sg

"""layout = [[sg.Text("Hola"), sg.Input("")],
        [sg.Text("Hola de nuevo")],
        [sg.Button("Push me")]]"""

def return_layout():
    size_button = (5,2)
    lista = [[
            sg.Button(button_text = "-",size = size_button,key = f"-{0}-"), 
            sg.Button("-",size = size_button,key = f"-{1}-"),
            sg.Button("-",size = size_button,key = f"-{2}-"),
        ],
        [
            sg.Button("-",size = size_button,key = f"-{3}-"),
            sg.Button("-",size = size_button,key = f"-{4}-"),
            sg.Button("-",size = size_button,key = f"-{5}-"),
        ],
        [
            sg.Button("-",size = size_button,key = f"-{6}-"),
            sg.Button("-",size = size_button,key = f"-{7}-"),
            sg.Button("-",size = size_button,key = f"-{8}-"),
        ]]
    return lista

def start_game(layout):
    PLAYER_ONE = "X"
    PLAYER_TWO = "O"
    ac_player = PLAYER_ONE
    deck = [0,0,0,0,0,0,0,0,0]
    window = sg.Window("Demo Passwords",layout,"""margins=(250,250)""")
    while True:
        event,values = window.read()
        print(event,"->")
        if event == sg.WIN_CLOSED:
            break
        if window.Element(event).ButtonText == "-":
            deck = check_deck(event,deck,ac_player)
            window.Element(event).Update(text = ac_player)
            ac_player = PLAYER_ONE if ac_player == PLAYER_TWO else PLAYER_TWO
    window.close() 

def check_deck(event,deck,ac_player):
    index = int(event.replace("-",""))
    deck[index] = ac_player
    print(deck)
    return deck

if __name__ == "__main__":
    layout = return_layout()
    start_game(layout)