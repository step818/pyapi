#!/usr/bin/env python3

import requests



def main():
    mars = requests.get("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY").json()
    
   # camera = input("Which camera would you like data from? (FHAZ, RHAZ, MAST, CHECMCAM, NAVCAM): ").upper()
    
    print(mars["photos"])

    print(f"All the photos from camera: {camera} ")
    for photo in mars['photos']:
        if(photo['camera']['name'] == camera):
          print("Rover: " + photo['rover']['name'])
          print("Date: " + photo['earth_date'])
          print(photo['img_src'])







if __name__ == '__main__':
    main()
