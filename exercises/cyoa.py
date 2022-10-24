"""This game simulates the Oregan Trail."""
__author__ = "730480357"

from random import randint

player: str = ""
points: int = 0
day_number: int = 0
alive: bool = True
move_day: int = 0

food: int = 0
medicine: int = 0
spare_parts: int = 0
provisions: int = 0

FOOD: str = "\U0001F373"
MEDICINE: str = "\U0001F489"
SPARE_PARTS: str = "\U0001F5C3"
CALAMITY: str = "\U0000203C"
C_FOOD: str = "\U0001F623"
C_MEDICINE: str = "\U0001F912"
C_SPARE_PARTS: str = "\U0001F62C"
DEAD: str = "\U00002620"


def main() -> None:
    """Entryway to the program."""
    greet()
    provisions_initialization()
    decision: int = 0
    global points
    while alive:
        if move_day == 12:
            print(f"{player} has arrived safely in Oregan!")
            quit()
        decision = int(input(f"Does {player} move forward(1), rest(2), or quit the game(3)? "))
        if decision != 1 and decision != 2 and decision != 3:
            decision = int(input(f"\n\nYou did not enter a valid character! \n\nDoes {player} move forward(1), rest(2), or quit the game(3)? "))
        if decision == 1:
            move(points)
        elif decision == 2:
            rest()
        elif decision == 3:
            quit()


def greet() -> None:
    """Greets the player and explains the game to them."""
    print("Welcome to Oregan Trail!")
    global player
    player = input("What is your name? ")


def provisions_initialization() -> None:
    """This function allows the player to decide the combination of provisions they will be taking with them during the gameplay loop."""
    global food
    global medicine
    global spare_parts
    global provisions
    print(f"Before they embark on their journey, {player} needs to stock up on provisions!\n{player} can take 7 units worth of provisions.\nThey are: {FOOD}Food\n           {MEDICINE}Medicine\n           {SPARE_PARTS} Spare Parts")
    while provisions != 7:
        food = (int(input(f"{FOOD}How many units of food does {player} take? ")))
        medicine = (int(input(f"{MEDICINE}How many units of medicine does {player} take? ")))
        spare_parts = (int(input(f"{SPARE_PARTS}How many units of spare parts does {player} take? ")))
        provisions = food + medicine + spare_parts
        if provisions != 7:
            print(f"\n{player} did not pack 7 units of provisions for their trip! They must repack for their own wellbeing!\n")
    print(f"\n{player} is ready to embark on their journey to Oregan!\n")


def move(internal: int) -> int:
    """Function defining what happens on a day when the player moves, including potential calamities."""
    global day_number
    global food
    global medicine
    global spare_parts
    global points
    global alive
    global move_day
    print(f"\n------Day {day_number}-----\n\n{player} sets out for the day.\n ")
    daily_odds: int = randint(1, 4)
    if daily_odds == 1:
        print(f"The day is uneventful and {player} makes camp at sundown.")
    elif daily_odds == 2 and food == 0:
        alive = False
    elif daily_odds == 2:
        print(f"{CALAMITY}{C_FOOD}{FOOD}{player}'s food is stolen by scavengers! Food units - 1. {FOOD}{C_FOOD}{CALAMITY}\n")
        food -= 1
        internal += 1
    elif daily_odds == 3 and medicine == 0:
        alive = False
    elif daily_odds == 3:
        print(f"{CALAMITY}{C_MEDICINE}{MEDICINE}{player} has cholera! Medicine units - 1. {MEDICINE}{C_MEDICINE}{CALAMITY}\n")
        medicine -= 1
        internal += 1
    elif daily_odds == 4 and spare_parts == 0:
        alive = False
    elif daily_odds == 4:
        print(f"{CALAMITY}{C_SPARE_PARTS}{SPARE_PARTS}{player}'s wagon is stuck in a ditch! Spare parts units - 1. {SPARE_PARTS}{C_SPARE_PARTS}{CALAMITY}\n")
        spare_parts -= 1
        internal += 1
    if not alive:
        print(f"{DEAD}{player} Died!{DEAD}")
        quit()
    if alive:
        day_number += 1
    move_day += 1
    print(f"{player} has {food} units of food, {medicine} units of medicine and {spare_parts} units of spare parts.\n")
    return internal
    

def rest() -> None:
    """Function defining what happens on a rest day."""
    global day_number
    global food
    global medicine
    global spare_parts
    global points
    global alive
    decision: int = 0
    print(f"-----Day {day_number}-----\n\n{player} rests for the day.")
    daily_odds: int = randint(1, 20)
    """Nothing Happens."""
    if daily_odds > 0 and daily_odds < 10:
        print(f"{player} has a day full of rest and relaxation and falls asleep at sunset with a smile on their face.")
        """Player resupplies provisions."""
    if daily_odds >= 10 and daily_odds < 20:
        decision = int(input(f"{player} stops at a homestead to resupply. \nThey are allowed one unit of either: {FOOD}Food(1) \n                                     {MEDICINE}Medicine(2)\n                                     {SPARE_PARTS}Spare Parts(3)\n"))
        if decision != 1 and decision != 2 and decision != 3:
            decision = int(input(f"\n\nYou did not enter a valid character!\n\n{player} makes a stop at a homestead to resupply. \nThey are allowed one unit of either: {FOOD}Food(1) \n                                     {MEDICINE}Medicine(2)\n                                     {SPARE_PARTS}Spare Parts(3)\n"))
            if decision == 1:
                food += 1
            elif decision == 2:
                medicine += 1
            elif decision == 3:
                spare_parts += 1
    """Player death to discourage too much resting."""
    if daily_odds == 20:
        alive = False
        print(f"The Sun inexplicably turns into a black hole, sucking the Earth into it and killing {player} in the process!")
    if not alive:
        print(f"{DEAD}{player} Died!{DEAD}")
        quit()
    if alive:
        day_number += 1
    print(f"\n{player} has {food} units of food, {medicine} units of medicine and {spare_parts} units of spare parts.\n")


def quit() -> None:
    """Ends game."""
    global alive
    print(f"Goodbye! Thanks for playing! \nPlayer name: {player}\nDays elapsed: {day_number}\nCalamities survived: {points}")
    alive = False


if __name__ == "__main__":
    main()