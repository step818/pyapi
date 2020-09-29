#!/usr/bin/env python3
import argparse, socket
from datetime import datetime

heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

def printHero(heroInput, statInput):
    print(f"{heroInput}\'s {statInput}")



if __name__ == '__main__':
    heroes = {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}
    parser = argparse.ArgumentParser(description='Find out about (flash batman supermen)')
    parser.add_argument('char_name', choices=heroes.key(), help='which role to play')
    parser.add_argument('char_stat', choices=heroes['flash'].keys(), metavar='STAT', default='speed', help='Pick a stat from [speed, strength, spue']) 
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')
args = parser.parse_args()
printHero = heroes[args.role]
print(printHero(args.p))

