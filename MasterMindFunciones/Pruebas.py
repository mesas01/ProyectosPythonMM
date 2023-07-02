import os
import random

from pokeLoad import get_all_pokemons


def get_player_profile(pokemon_list):
    return {
        "player_name": input("Cual es tu nombre?: "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)],
        "combats": 0,
        "pokeball": 4,
        "life_potion": 2,
    }


def any_player_pokemon_lives(player_profile):
    return sum([pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]]) > 0


def get_pokemon_info(pokemon):
    return "{} | Type: {}| lvl: {} | hp {}/{}".format("".join(pokemon["name"]),
                                                      "/".join(pokemon["type"]),
                                                      pokemon["level"],
                                                      pokemon["current_health"],
                                                      pokemon["base_health"])


def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("\nEscoge el pokemon con el que deseas batallar\n")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index, get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cuál eliges? "))]


        except (ValueError, IndexError):
            print("Opción inválida")


def capture_with_pokeball(player_profile, enemy_pokemon):
    probability = None
    if player_profile["pokeball"] >= 1:
        print("\nLa vida de el {} que deseas atrapar es {} y su tipo es {}\n".format(enemy_pokemon["name"],
                                                                                     enemy_pokemon["current_health"],
                                                                                     enemy_pokemon["types"]))
        player_profile["pokeball"] -= 1
        if enemy_pokemon["current_health"] > 50:
            probability = random.randint(1, 10)
        elif enemy_pokemon["current_health"] > 20:
            probability = random.randint(1, 5)
        elif enemy_pokemon["current_health"] > 5:
            probability = random.randint(1, 2)
        elif enemy_pokemon["current_health"] == 1:
            probability = 1
        if probability == 1:
            player_profile["pokemon_inventory"].append(enemy_pokemon)
            print("\nHas obtenido a {} su vida es {} y su tipo {}\n".format(enemy_pokemon["name"],
                                                                            enemy_pokemon["current_health"],
                                                                            enemy_pokemon["types"]))
        else:
            print("No ha sido posible capturarlo.")
    else:
        print("No posees pokeballs")


def cure_pokemon(player_profile, player_pokemon):
    if player_profile["life_potion"] >= 1:
        print("Ahora vas a aumentar la vida de {} en 50, recuerda que solo puedes llegar a 100".format(
            player_pokemon["name"]))
        player_profile["life_potion"] -= 1
        if player_profile["current_health"] >= 1:
            player_pokemon["current_health"] += 50
            if player_pokemon["current_health"] > 100:
                player_pokemon["current_health"] = player_profile["base_health"]
            print("{} ha recuperado vida, ahora su vida es {}".format(player_pokemon["name"],
                                                                      player_pokemon["current_health"]))
    else:
        print("No posees pociones")


def choose_attack(attacks):
    chosen_attack = None

    while chosen_attack is None:
        for attack in attacks:
            print("*{}".format(get_attack_info(attack)))
        chosen_attack = int(input("\n¿Con que quieres atacar?(0-4): "))
    try:
        return attacks[chosen_attack]
    except (TypeError, IndexError, ValueError):
        print("\nEse ataque no esta disponible para ese pokemon...")


def get_attack_info(pokemon_attack):
    return "{} | type: {} | damage: {}".format(pokemon_attack["name"],
                                               pokemon_attack["type"],
                                               pokemon_attack["damage"])


def player_attack(player_pokemon, enemy_pokemon, attacks):
    chosen_attack = choose_attack(attacks)
    enemy_pokemon["current_health"] -= chosen_attack["damage"]
    print("\n{} ataca con {}".format(player_pokemon["name"], chosen_attack["name"]))
    print("{} recibe {} de daño\n".format(enemy_pokemon["name"], chosen_attack["damage"]))


def enemy_attack(player_pokemon, enemy_pokemon):
    attack = random.choice(enemy_pokemon["attacks"])
    player_pokemon["current_health"] -= attack["damage"]
    print("\n{} ataca con {}".format(enemy_pokemon["name"], attack["name"]))
    print("{} recibe {} de daño\n".format(player_pokemon["name"], attack["damage"]))


def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_experience"] += points

        while pokemon["current_experience"] > 20:
            pokemon["current_experience"] -= 20
            pokemon["level"] += 1
            pokemon["curren_health"] = pokemon["base_health"]
            print("Tu {} ha subido de nivel".format(get_pokemon_info(pokemon)))


def fight(player_profile, enemy_pokemon):
    print("----PREPARATE COMIENZA LA BATALLA----")
    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    print("\nPokemons: {} VS {}".format(get_pokemon_info(player_pokemon),
                                        get_pokemon_info(enemy_pokemon)))
    attacks = [random.choice(player_pokemon["attacks"]) for a in range(5)]
    os.system("cls")

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        while action not in ["A", "P", "L", "C"]:
            action = input("\nQue deseas hacer?: [A]ttack,[P]okeball,[L]ife potion,[C]hange pokemon: ")
        if action == "A":
            player_attack(player_pokemon, enemy_pokemon, attacks)


        elif action == "P":

            capture_with_pokeball(player_profile, enemy_pokemon)
        elif action == "L":

            cure_pokemon(player_profile, player_pokemon)
        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)

        enemy_attack(player_pokemon, enemy_pokemon)

        if player_pokemon == 0 and any_player_pokemon_lives(player_profile):
            player_pokemon = choose_pokemon(player_profile)
        if player_pokemon["current_health"] <= 0:
            player_pokemon["current_health"] = 0
            print("\nHa ganado {}".format(enemy_pokemon["name"]))
            player_profile["pokemon_inventory"].remove(player_pokemon)
            print(
                "\n{} perdió, {} fue removido de tu inventario".format(player_pokemon["name"], player_pokemon["name"]))
            break
        if enemy_pokemon["current_health"] <= 0:
            enemy_pokemon["current_health"] = 0
            print("\n--HAS GANADO ESTE COMBATE, FELICIDADES--\n")
            input("Presiona [ENTER] para pelear el siguiente combate...")
            break
    assign_experience(attack_history)

    print("----HA TERMINADO LA BATALLA----")
    print("Presiona START para continuar")
    os.system("cls")


def item_lottery(player_profile):
    chance = random.randint(1, 2)
    if chance == 1:
        print("\nTe has ganado una pokebola\n")
        player_profile["pokeball"] += 1
    else:
        print("\nTe has ganado un pocion\n")
        player_profile["life_potion"] += 1


def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile, enemy_pokemon)
        item_lottery(player_profile)

    print("Has perdido en el combate numero {}".format(player_profile["combats"]))


if __name__ == "__main__":
    main()