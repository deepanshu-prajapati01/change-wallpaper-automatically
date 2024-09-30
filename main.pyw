'''
Code by - Deepanshu

Github: Deepanshu-prajapati01
Instagram: deepanshu_prajapati01


'''
import random
from screeninfo import get_monitors
import requests
import schedule
import time
import ctypes
import urllib.request
from datetime import datetime
import os

# THIS ONE WILL BE USED IN CASE TO PRESERVE FILES IN CASE THERE IS NO INTERNET! -
# JUST TO MAKE SURE THAT WE DON'T RAN OUT OF WALLPAPERS

internet_available = False


def download_wallpaper(number):
  global download_status
  try:
    for i in range(number):
      url = f'https://picsum.photos/{get_monitors()[0].width}/{get_monitors()[0].height}'
      response = requests.get(url)
      jpg_url = response.url
      # URL of the image
      image_url = jpg_url  # the URL you got

      # Path to save the image
      image_path = os.path.join(os.path.expanduser('~'), 'Desktop\\Wallpapers\\', f"{datetime.now().strftime("%Y-%m-%d %H-%M-%S.%f")}.jpg")

      # Download the image from the URL
      urllib.request.urlretrieve(image_url, image_path)
      print(f"Downloading wallpaper - {i}")
    return True
  except:
    return False


def change_wallpaper():
  global internet_available
  print("Checking the stock of wallpapers!")
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\Wallpapers\\")
  print(os.getcwd())
  files = os.listdir()
  name = random.choice(files)
  newName = 'currentWallpaper.jpg'
  
  
  
  # THIS WILL DELETE THE APPLIED WALLPAPER ONLY IF THERE IS INTERNET OR THERE IS ENOUGH STOCK.
  # ELSE IT WON'T DO ANYTHING.
  try:
    if internet_available:
      os.remove(newName)
      print(f"Wallpaper changed to - {name+1}")
  except:
    print(f"No wallpaper found with the name - {newName}")
  finally:
    # rename the wallpaper to the new name - 'currentWallpaper'
    os.rename(name, newName)
    name = newName  
  
  try:
    # Use ctypes to change the wallpaper
    image_path = os.path.join(os.path.expanduser('~'), 'Desktop\\Wallpapers\\', f'{name}')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    print("Wallpaper changed successfully!")


  except:
    pass

def check_wallpaper(less_than):
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\Wallpapers\\")
  files = os.listdir()
  if len(files) <= less_than:
    return download_wallpaper(20)
  else:
    return True


if __name__ == '__main__':
  # Just to make sure that you have a wallpaper in the desktop where all the wallpapers are going to be stored.
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\")
  if not "Wallpapers" in os.listdir():
    os.mkdir("Wallpapers")

  # MAKE IT SLEEP FOR 10 seconds SO ON STARTUP IT DON'T MAKE EXTRA BURDEN
  print("Sleeping for 10 seconds;")
  # time.sleep(10)

  # Running it for the first time to download files
  if check_wallpaper(20):
    internet_available = True
    
  # temp check 
  change_wallpaper()

  schedule.every().hour.do(change_wallpaper)
  while True:
    if check_wallpaper(5):
      internet_available = True
    else:
      internet_available = False

    schedule.run_pending()
    time.sleep(59)
