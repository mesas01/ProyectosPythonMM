import PySimpleGUI as sg


def ask_names():
    layout = [[sg.Text("¿Quién juega con la X?"), sg.InputText()],
              [sg.Text("¿Quién juega con la O?"), sg.InputText()],
              [sg.Button("OK", key="-ok-")]]
    window = sg.Window("Demo", layout, margins=(100, 100))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "-ok-":
            if values[0] != "" and values[1] != "":
                p_1_n, p_2_n = values[0], values[1]
                window.close()
                return p_1_n, p_2_n


def load_game(button_size, current_player):
    layout = [[[sg.Button("", key="-{}-".format(i * 3 + n + 1), size=button_size) for n in range(3)] for i in range(3)],
              [sg.Text("Es el turno de {}".format(current_player), key="-current-")],
              [sg.Button("Empezar de nuevo", key="-restart-")]]
    window = sg.Window("Demo", layout, margins=(100, 100))
    return window


def play_game(player_1, player_2):
    button_size = (7, 3)
    ONE = "X"
    TWO = "O"
    patterns = (("-1-", "-2-", "-3-"), ("-3-", "-6-", "-9-"), ("-9-", "-8-", "-7-"), ("-7-", "-4-", "-1-"),
                ("-1-", "-5-", "-9-"), ("-3-", "-5-", "-7-"),
                ("-2-", "-5-", "-8-"), ("-4-", "-5-", "-6-"))
    current_player = player_1

    window = load_game(button_size, current_player)
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "-restart-":
            n = 1
            window.Element("-current-").update("Es el turno de {}".format(current_player))
            for button in range(9):
                window.Element("-{}-".format(n)).update("")
                n += 1

        elif window.Element(event).ButtonText == "":
            if current_player == player_1:
                current = ONE
            else:
                current = TWO
            window.Element(event).update(text=current)
            for pattern in patterns:
                total = 0
                for number in pattern:
                    if window.Element(number).ButtonText == current:
                        total += 1
                if total == 3:
                    break

            if total == 3:
                window.close()
                next = winner_screen(current_player)
                if next == "-again-":
                    play_game(player_1, player_2)
                elif next == "-restart-":
                    main()
                else:
                    break
            else:
                if current_player == player_1:
                    current_player = player_2
                else:
                    current_player = player_1
                window.Element("-current-").update("Es el turno de {}".format(current_player))


def winner_screen(current_player):
    layout = [[sg.Text("EL GANADOR ES {}".format(current_player.upper()))],
              [sg.Button("Volver a jugar", key="-again-")],
              [sg.Button("Cambiar de jugadores", key="-restart-")]]
    window2 = sg.Window("Demo", layout, margins=(100, 100))
    while True:
        event, values = window2.read()
        if event == sg.WINDOW_CLOSED:
            break
        window2.close()
        return event


def main():
    try:
        player_1, player_2 = ask_names()
    except TypeError:
        quit()
    play_game(player_1, player_2)


if __name__ == "__main__":
    main()