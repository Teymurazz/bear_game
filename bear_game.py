import random
import secrets
from constants_bear import *

bears_body_part = ["HEAD", "HEART", "HAND", "BODY"]
player_hp = PLAYER_MAX_HP
bear_hp = BEAR_MAX_HP
print("The game is started. Try to be alive!")

while player_hp > 0 and bear_hp > 0:
    player_choice = secrets.choice(bears_body_part)
    bear_choice = random.randint(MIN_BEAR_DAMAGE_HP, MAX_BEAR_DAMAGE_HP)

    if player_choice == "HEAD":
        player_damage = SWORD_DAMAGE_HP * HEAD_DAMAGE_COEF
    elif player_choice == "HEART":
        player_damage = SWORD_DAMAGE_HP * HEART_DAMAGE_COEF
    elif player_choice == "HAND":
        player_damage = SWORD_DAMAGE_HP * HAND_DAMAGE_COEF
    else:
        player_damage = SWORD_DAMAGE_HP *  BODY_DAMAGE_COEF
        continue    
    
    bear_hp -= player_damage
    player_hp -= bear_choice
    
    if player_hp < 20:
        print("Drink RED BULL")
        player_hp+=50
        print("Congratulations! Now you're again strong")

    print(f"you've attecked the {player_choice}. You've made a {player_damage} to bear.")
    print(f"Bear's remain power is {bear_hp}")
    print(f"the bear has attacked you and make {bear_choice} damage for you")
    print(f"Your remain power is {player_hp}")

if PLAYER_MAX_HP > 0:
    print(PLAYER_WIN_TITLE)
else:
    print(PLAYER_LOSE_TITLE)




