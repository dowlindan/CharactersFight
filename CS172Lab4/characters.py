# Purpose: The Character class is a base class for a character in a video game, and two derived classes are included
# Author: Dan Dowlin
# Version: 4/27/2023

# This class defines a generic Character
# It includes attributes and many implemented methods, in addition to an abstract
# methods __str__ and react
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS Character CLASS ####
class Character(ABC):
    @abstractmethod
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage):
        self.__name = name
        self.__health = maxHealth
        self.__description = description
        self.__weaponName = weaponName
        self.__weaponDamage = weaponDamage

    @abstractmethod
    def __str__(self):
        pass
    
    @abstractmethod
    def react(self):
        pass
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description
    
    def getWeaponName(self):
        return self.__weaponName
    
    def getWeaponDamage(self):
        return self.__weaponDamage
    
    def attack(self, enemy):
        enemy.takeDamage(self.__weaponDamage)
    
    def takeDamage(self, amount):
        self.__health -= amount
    
    def getHealth(self):
        return self.__health
    
    
class Monster(Character):
    def __init__(self, name, description, maxHealth , weaponName, weaponDamage, motivation):
        Character.__init__(self, name, description, maxHealth, weaponName, weaponDamage)
        self.__motivation = motivation
        
    def __str__(self):
        string = self.getName() + " is a " + self.getDescription()
        string += "\nWeapon: " + self.getWeaponName()
        string += "\nCurrent Health " + str(self.getHealth())
        string += "\nMotivation: " + self.getMotivation()
        return string
    
    def react(self):
        return self.getName() + " laughs maniacally."
    
    def getMotivation(self):
        return self.__motivation

class Hero(Character):
    def __init__(self, name, description, maxHealth, weaponName, weaponDamage, defenseName):
        Character.__init__(self, name, description, maxHealth, weaponName, weaponDamage)
        self.__defenseName = defenseName
        self.__isDefending = False
        
    def __str__(self):
        string = "Our hero" + self.getName() + " is a " + self.getDescription()
        string += "\nWeapon: " + self.getWeaponName()
        string += "\nDefense: " + self.getDefenseName()
        string += "\nCurrent Health " + str(self.getHealth())
        string += "\nDefense Status: " + str(self.isDefending())
        return string
        
    def react(self):
        return self.getName() + " charges bravely."
        
    def getDefenseName(self):
        return self.__defenseName
    
    def isDefending(self):
        return self.__isDefending
    
    def defend(self):
        self.__isDefending = True
        
    def takeDamage(self, amount):
        if self.__isDefending:
            amount *= 0.5
            self.__isDefending = False
        
        super().takeDamage(amount)
