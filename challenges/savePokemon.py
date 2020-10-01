#!/usr/bin/env python3

import requests
import wget

#Function 3
def wget_pic(imagelink):
    filename = imagelink.split('/')[-1]
    url = imagelink
    wget.download(url, '/home/student/static/' + filename)


#Function 1
def api_pull():
    choice = input("What pokemon would you like a picture of? ").lower()
    pokeball = "https://pokeapi.co/api/v2/pokemon/"
    chosen = requests.get(pokeball + choice).json()
    return chosen


#Function 2
def api_slice(json2python):
    poke_pic = json2python['sprites']['front_default']
    return poke_pic

def main():
    wget_pic(api_slice(api_pull()))

if __name__ == "__main__":
    main()
