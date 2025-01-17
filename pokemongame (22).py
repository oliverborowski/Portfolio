#OLIVER BOROWSKI

import random
pokemon_level = 0
pokemon_name = " "
evolution_names = {
    "Bulbasaur": ["Bulbasaur", "Ivysaur", "Venusaur"],
}

def evolve_pokemon():
    global pokemon_level, pokemon_name#allows the reader to evolve when the reach a high enough level
    if pokemon_name == "Bulbasaur" and pokemon_level >= 10:
        pokemon_name = "Ivysaur"
        print(f"{pokemon_name} has evolved into Ivysaur!")

    elif pokemon_name == "Ivysaur" and pokemon_level >= 20:
        pokemon_name = "Venusaur"
        print(f"{pokemon_name} has evolved into Venusaur!")
def display_pokemon():
    global pokemon_name, pokemon_level
    print(f"Current Pokémon: {pokemon_name}")
    print(f"Current Level: {pokemon_level}")
def game():
    global pokemon_name, pokemon_level
    print("Select your Pokemon:")
    print("1. Bulbasaur")
    print("2. Charmander")
    print("3. Squirtle")

    choice = input("Enter the number of your choice: ")
    if choice == '1':
        pokemon_name = "Bulbasaur"
    else:
        print("Invalid choice. Defaulting to Bulbasaur.")
        pokemon_name = "Bulbasaur"

    while True: #gives the user options on what they would like to do each day 
        print("\nMenu:")
        print("1. Train (Increase level by 1)")
        print("2. Gym Battle (Increase level by 2 if win, 0 if lose)")
        print("3. Display Pokémon Info")
        print("4. Exit")

        option = input("Select an option: ")

        if option == '1':
            pokemon_level += 1
            print("You trained your Pokemon! Level increased by 1.")#defines each function by giving the pokemon a level up for not
            evolve_pokemon()
        elif option == '2':
            if random.choice([True, False]):
                pokemon_level += 2
                print("Your Pokemon won the gym battle! Level increased by 2.")
            else:
                print("Your Pokemon lost the gym battle! No level increase.")
            evolve_pokemon()
        elif option == '3':
            display_pokemon()
        elif option == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")
#Main
game()
