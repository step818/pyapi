#!/usr/bin/env python3

char_name = input("Which character do you want to know about ((Flash, Batman, Superman) ")

char_stat = input("What statistic do you want to know about? (Strength, speed, or intelligence) ")

mydict = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

if(char_name.lower() in mydict and char_stat.lower() in mydict[char_name.lower()]):
    print(f"{char_name}\'s  {char_stat} is: {mydict[char_name.lower()][char_stat.lower()]} ")

