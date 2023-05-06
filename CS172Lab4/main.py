# Purpose: Simulates a battle in a video game
# Author: Dan Dowlin
# Version: 4/27/2023
from characters import Monster, Hero
import random

# This function has two Characters fight
# it returns the winner or None on a tie
def monster_battle(h1, m1):
   
    print("Starting Battle Between")
    print(m1.getName() + ": " + m1.getDescription())
    print(h1.getName() + ": " + h1.getDescription())
    
    attacker = random.choice([m1, h1])
    defender = (h1 if attacker == m1 else m1)
        
    print(attacker.getName() + " goes first.")
    
    #Loop until someone is unconsious (health < 1) or choose to stop
    stop = False
    while( m1.getHealth() > 0 and h1.getHealth() > 0 and not stop ):
        
        #It will be nice for output to record the damage done
        before_health = defender.getHealth()            

        #Check if the attacker is a monster
        if(isinstance(attacker, Monster)):
            #check if defender is defending, if so print out info about the defense
            if(defender.isDefending()):
                print("Our hero is defending with", defender.getDefenseName(), "!")
                       
            print(attacker.react())
            #Have the attacker attack.
            attacker.attack(defender)
            print_results(attacker, defender, attacker.getWeaponName(), before_health - defender.getHealth())
            #Call the print_results function with the necessary info.


        else:
            # Ask the user for the next action: attack, defend, or stop.
            action = input('Pick one of these (a)ttack, (d)efend, or sto(p): ')
        
            #Based on the input, either attack, defend, or end loop
            #If they chose to attack, have the attacker react, attack and then
            #call the print_results function with the necessary info.
            if action == 'a':
                print(attacker.react())
                attacker.attack(defender)
                print_results(attacker, defender, attacker.getWeaponName(), attacker.getWeaponDamage())
            elif action == 'd':
                attacker.defend()
            else:
                stop = True

        temp = attacker
        attacker = defender
        defender = temp
        

    #Print out who won.
    #Return who won.
    print("Battle is over. let's see who has won...")
    if attacker.getHealth() <= 0 and defender.getHealth() <= 0:
        print("The battle is tied!")
    elif attacker.getHealth() <= 0:
        print(defender.getName() + " is victorious!")
        return defender.getName()
    else:
        print(attacker.getName() + " is victorious!")
        return attacker.getName()
    
    
    
#This function prints the status updates
def print_results(attacker, defender, attack, hchange):
    res = attacker.getName() + " used " + attack
    res += " on " + defender.getName() + "\n"
    res += "The attack did " + str(hchange) + " damage."
    print(res)
    print(attacker.getName() + " at " + str(attacker.getHealth()))
    print(defender.getName() + " at " + str(defender.getHealth()))

#----------------------------------------------------
if __name__=="__main__":
    #Every battle should be different, so we need to
    #start the random number generator somewhere "random".
    #With no input Python will set the seed
    random.seed(0)
   
    #Get Monster's name, description, maxHealth, weaponName, weaponDamage, and motivation from the user here.
    #Instantiate a Monster using that info. Note that weaponDamage should be a floating point number.
    
    monsterName = input("Enter monster's name: ")
    monsterDescription = input("Enter monster's description: ")
    monsterHealth = int(input("Enter a number for monster's health: "))
    monsterWeapon = input("Enter monster's weapon name: ")
    monsterDamage = float(input("Enter monster's weapon damage (as a number): "))
    monsterMotivation = input("Enter monster's motivation: ")
        
    myMonster = Monster(monsterName, monsterDescription, monsterHealth, monsterWeapon, monsterDamage, monsterMotivation)
    
    ######TODO######    
    #Get the Hero's name,description, maxHealth, weaponName, weaponDamage, defenseName from the user here.
    #Instantiate a Hero using that info. Note that weaponDamage should be a floating point number.
    heroName = input("Enter hero's name: ")
    heroDescription = input("Enter the hero's description: ")
    heroHealth = int(input("Enter a number for the hero's health: "))
    heroWeapon = input("Enter hero's weapon name: ")
    heroDamage = float(input("Enter hero's weapon damage (as a number): "))
    heroDefense = input("Enter the hero's defense name: ")

    myHero = Hero(heroName, heroDescription, heroHealth, heroWeapon, heroDamage, heroDefense) #this should be an instance of your Hero class

    winner = monster_battle(myHero, myMonster)
