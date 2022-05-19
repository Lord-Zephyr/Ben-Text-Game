# first = input("First: ")
# second = input("Second: ")
# sum = float(first) + float(second)
# print("Sum: " + str(sum))

import random 

# function to restart game
def play_again():
      while True:
        again = input("Thank you again for playing this game, would you like to try again? (y/n) ")
        if again not in {"y","n"}:
            print("please enter valid input")               
        elif again == "n":
            return "Thank you for playing, bye!"
        elif again == "y":
            # call function to start the calc again
            return main() 
# dungeon
def dungeon():
    print("You open the trap door to discover a dark cellar.")
    sure = input("Are you sure you want to continue? (y/n) ")
    if sure.lower() == 'y':
        print("You feel brave today. Maybe too brave.")
        print("A vile stench enters your nose.")
        print("Maybe I shouldn't have gone in here.")
        back = input("Keep going? (y/n) ")
        if back.lower() == 'y':
            print("You continue forward.")
            print("Eventually you come across a door with light peering out from beneath it.")
            door = input("Open the door? (y/n): ")
            if door.lower() == 'y':
                print("You open the door.")
                print("The light blinds you.")
                print("You walk towards the light.")
                print("You hear a voice calling to you.")
                print("\"ah yes a new test subject has arrived\"")
                print("Would you like to turn ba--")
                print("\"It's too late now\"")
                print("Your vision goes black.")
                print("You feel a piercing pain in your chest.")
                print("...")
                print("...")
                print("...")
                print("You have died?")
                print("Congratulations, you made it to the end of the demo. This is the farthest you can get for now.")
                print("Thank you for playing :)")
                play_again()

            elif door.lower() == 'n':
                print("You decide whatever is in here isn't worth it.")
                print("You head home.")
                play_again()
            else:
                print("bro please just put the right input it's annoying af to have to code in this fail safe everytime fuck you")
                play_again()


        elif back.lower() == 'n':
            print("You decide whatever is in here isn't worth it.")
            print("You head home.")
            play_again()
        else:
            print("bro please just put the right input it's annoying af to have to code in this fail safe everytime fuck you")
            play_again()
        
    elif sure.lower() == 'n':
        print("Guess you don't feel adventurous today.")
        print("You head home.")
        play_again()
    else:
        print("If you can't press a simple y or n you don't deserve to continue :)")
        play_again()


# main                      
def main():
    decision = input("Would you like to play (y/n): ")
    if decision.lower() == 'n':
        print("Fuck off then")
    elif decision.lower() == 'y':
        print("Welcome to the game!")
        print("You stumble across a dead body.")
        print("Option 1: Loot it")
        print("Option 2: Move on")
        print("Option 3: Bury it")
        option = int(input("What do you do? (1/2/3): "))
    if option != {1, 2, 3}:
        print("Yeah buddy learn to use a computer you fuck")
        play_again()
    else:
        print("Bruh you're dumb")
        play_again()
    if option == 1:
        loot = random.randrange(1,20)
        print("Rolling for loot: " + str(loot))
        if loot <= 10:
            print("You find nothing but filth.")
            print("While you attempt to loot the corpse, you realize it's not a corpse at all.")
            print("Catching you by surprise, the \'corpse\' kills you instantly")
            print("I got lazy, you got unlucky. You're dead.")
            play_again()
        else:
            print ("You eye a dagger sticking from the corpse's thorax")
            dagger = input("Would you like to take the dagger? (y/n): ")
            if dagger.lower() == 'y':
                print("You obtained an obsidian dagger")
                print("Rolling for stats:")
                attack = random.randrange(1,10)
                durability = random.randrange(1,3)
                print("Attack: " + str(attack))
                print("Durability: " + str(durability))
                print("Suddenly the corpse awakens and rushes you.")
                print("Rolling for initiative: ")
                init_player = random.randrange(1,20)
                init_corpse = random.randrange(1,20)
                print("Corpse init: " + str(init_corpse))
                print("Player init: " + str(init_player))
                corpse_damage = random.randrange(1,10)
                player_health = 10
                corpse_health = 10
                if init_player > init_corpse:
                    print("You're able to dodge the corpse's attack.")
                    print("You strike the corpse with your dagger.")
                    corpse_health -= attack
                    while player_health > 0 and corpse_health > 0:
                        if player_health > 0 and corpse_health > 0:
                            print("The corpse returns a blow.")
                            player_health -= corpse_damage
                            print("Player health: " + str(player_health))
                            print("You defend yourself.")
                            corpse_health -= attack
                            print("Corpse health: " + str(corpse_health))
                else:
                    while player_health > 0 and corpse_health > 0:
                        print("The corpse strikes you before you can react.")
                        player_health -= corpse_damage
                        print("Player health: " + str(player_health))
                        if player_health > 0 and corpse_health > 0:
                            print("You attempt to defend yourself with the dagger.")
                            corpse_health -= attack
                            print("Corpse health: " + str(corpse_health))
                if player_health <= 0:
                    print("The corpse wins, you have died")
                    play_again()
                else:
                    print("You manage to win the fight, congratulations.")
                    durability -= 1
                    print("Dagger durability: " + str(durability))
                    if durability <= 0:
                        print("Your dagger has broken.")
                    print("Player health: " + str(player_health))
                    rest = input("Would you like to rest? (y/n) ")
                    if rest.lower() == 'y':
                        print("You attempt to rest.")
                        luck = random.randrange(1,20)
                        print("Rolling for luck: " + str(luck))
                        if luck <= 10:
                            print("You awake restlessly in the night to red eyes staring over you.")
                            print("Is this a dream?")
                            print("You feel a warm sensation pooling from you abdomen.")
                            print("You fall back asleep. Permanently.")
                            play_again()
                        else:
                            print("You manage to sleep through the night.")
                            heal = random.randrange(1,10)
                            print("Rolling for heal: ")
                            print("Health restored: " + str(heal)) 
                            player_health += heal    
                            print("You notice a trap door in the ground.")
                            trap_door = input("Would you like to enter? (y/n): ")
                            if trap_door.lower() == 'y':
                                dungeon()
                            elif trap_door.lower() == 'n':
                                print("Guess you don't feel adventurous today.")
                                print("You head home.")
                                play_again()
                            else:
                                print("If you can't press a simple y or n you don't deserve to continue :)")
                                play_again()
                    elif rest.lower() == 'n':
                        print("You notice a trap door in the ground.")
                        trap_door = input("Would you like to enter? (y/n): ")
                        if trap_door.lower() == 'y':
                            dungeon()
                        elif trap_door.lower() == 'n':
                            print("Guess you don't feel adventurous today.")
                            print("You head home.")
                            play_again()
                        else:
                            print("If you can't press a simple y or n you don't deserve to continue :)")
                            play_again()
                    else:
                        print("it's really not that hard")
                        play_again()


                    
            elif dagger.lower() == 'n':
                print("You move on with nothing.")
                print("You find a house with a light on.")
                house = input("Go inside? (y/n): ")
                if house.lower() == 'y':
                    print("Something smells awful.")
                    print("Suddenly your face feels hot.")
                    print("What's happening????")
                    print("The world goes blank.")
                    print("You hear breathing!")
                    print("Void.")
                    print("You have died?")
                elif house.lower() == 'n':
                    print("Something feels off. You move on.")
                    print("You decide to rest outside")
                    print("Rolling for rest")
                    rest = random.randrange(1,10)
                    print("Rolling for rest: ")
                    print("Rest: " + str(rest))
                    print("End of demo for now. You haven't won, but you haven't lost either")

            else:
                "bro seriously u dumb"
                play_again()
    if option == 2:
        print("You move on with nothing")
        print("You have a lurking sense something is behind you")
        print("Roll for perception: ")
        perception  = random.randrange(1,20)
        print("Perception: " + str(perception))
        if perception <= 5:
            print("Suddenly everything goes black. You have died.")
            play_again()
        elif perception == range(6, 12):
            print("You turn around to the darkness behind you. Suddenly a dagger pierces your heart.")
            print("You have died.")
            play_again()
        elif perception == range(13,19):
            print("You hear something behind you and attempt to run")
            print("Running through the darkness you find a trench and hide")
            print("Suddenly everthing goes red")
            print("You walked into the wrong home")
            print("You have died")
            play_again()
        else:
            print("You dodge at the perfect time and survive the initial attack")
            print("You attempt to defend yourself.")
            print("Rolling for win: ")
            win = random.randrange(1,2)
            print("Win: " + str(win))
            if win == 1:
                print("You lose the fight honorably, but horribly.")
                print("You have died.")
                play_again()
            else:
                print("You win the fight miraculously, but not without consequences.")
                print("You eventually bleed out.")
                play_again()
    if option == 3:
        print("You dig a six foot grave for the corpse.")
        print("You move to pick up the body.")
        print("You realize they aren't dead.")
        print("Rolling for luck: ")
        luck = random.randrange(1,20)
        print("Luck: " + str(luck))
        if luck <= 10:
            print("The corpse bites your neck, you have died.")
            play_again()
        elif luck >= 10:
            print("You manage to throw the corpse.")
            fight_or_flight = input("Fight or run? (f/r): ")
            if fight_or_flight.lower() == 'f':
                print("You attempt hand to hand combat with the corpse.")
                print("The corpse exsanguinates you.")
                print("gg")
                play_again()
            elif fight_or_flight.lower() == 'r':
                print("Rolling for agility: ")
                agility = random.randrange(1,20)
                print("Agility: " + str(agility))
                if agility <= 10:
                    print("You trip. The corpse stomps your neck.")
                    play_again()
                if agility >= 10:
                    print("You outrun the corpse, you have survived this level. For now.")
                    print("You win the demo!")
                    play_again()
            elif fight_or_flight != {'f', 'r'}: 
                print("yeah that's not f or r")
                play_again()

main()
            

            