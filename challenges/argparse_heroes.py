#!/usr/bin/env python3

import argparse, socket
from datetime import datetime
import sys

args = sys.argv

hero= {"flash":{"speed": "fastest", "intelligence": "lowest", "strength": "lowest"}, "batman":{"speed": "slowest", "intelligence": "highest", "strength": "money"}, "superman":{"speed": "fast", "intelligence": "average", "strength": "strongest"}}

char_name = args[1]
char_stat = args[2]

if char_name in hero and char_stat in hero[char_name]:
    print(f"{char_name}\'s {char_stat} is: {hero[char_name][char_stat]}")

