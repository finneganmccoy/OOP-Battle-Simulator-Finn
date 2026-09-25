from goblin import Goblin
from hero import Hero

ARENA_NAME = "The Bronze Heptagon"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    goblin2 = Goblin("Grobble", health=200)
    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")
    hero = Hero(name="Ghero", health=300)
    print(f"But {hero.name} has answered the call")


if __name__ == "__main__":
    main()
