from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Iron Circle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblins = [Goblin("Gribble"), Goblin("Greeble")]
    hero = Hero("PLAYER1")

    print(f"{goblins[0].name} enters the arena with {goblins[0].health} health.")
    print(f"{goblins[1].name} enters the arena with {goblins[1].health} health.")
    print("But no hero has answered the call... yet.\n...")
    print(f"Nevermind I was wrong. Introducing... {hero.name}!")
    hero.attack(goblins[0])


if __name__ == "__main__":
    main()
