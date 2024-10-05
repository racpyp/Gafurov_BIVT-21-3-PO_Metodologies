from Gafurov_brain_games.engine import run_game
from Gafurov_brain_games.games import lcm, progression


def main():
    print("Choose a game:")
    print("LCM. Least Common Multifple")
    print("GP. Geometric Progression")

    user_choice = input("Your choice: ")

    if user_choice == "LCM":
        run_game(lcm)
    elif user_choice == "GP":
        run_game(progression)
    else:
        print("Oops! Invalid choice. Please try again")

if __name__ == "__main__":
    main()