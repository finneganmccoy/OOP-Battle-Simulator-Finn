from goblin import Goblin


ARENA_NAME = "The Iron Circle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblins = [Goblin("Gribble"), Goblin("Greeble")]
    

    print(f"{goblins[0].name} enters the arena with {goblins[0].health} health.")
    print(f"{goblins[1].name} enters the arena with {goblins[1].health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
