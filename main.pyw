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
import os




def download_wallpaper(number):
  global download_status
  try:
    for name in range(number):
      url = f'https://picsum.photos/{get_monitors()[0].width}/{get_monitors()[0].height}'
      response = requests.get(url)
      jpg_url = response.url
      # URL of the image
      image_url = jpg_url  # the URL you got

      # Path to save the image
      image_path = os.path.join(os.path.expanduser('~'), 'Desktop\\Wallpapers\\', f'{name}.jpg')

      # Download the image from the URL
      urllib.request.urlretrieve(image_url, image_path)
    return True
  except:
    return False


def change_wallpaper():
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\Wallpapers\\")
  files = os.listdir()
  name = random.choice(files)
  try:
    # Use ctypes to change the wallpaper
    image_path = os.path.join(os.path.expanduser('~'), 'Desktop\\Wallpapers\\', f'{name}')
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
    os.remove(image_path)
  except:
    pass

def check_wallpaper(less_than):
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\Wallpapers\\")
  files = os.listdir()
  if len(files) < less_than:
    for i in files:
      os.rename(i, f'{i}-{i}')

    download_status = download_wallpaper(20)
    return download_status


if __name__ == '__main__':
  # Just to make sure that you have a wallpaper in the desktop where all the wallpapers are going to be stored.
  os.chdir(f"{os.path.expanduser('~')}\\Desktop\\")
  if "Wallpapers" in os.listdir():
    os.mkdir("Wallpapers")


  print("Sleeping for 2 minutes;")
  time.sleep(120)

  # Running it for the first time to download files
  check_wallpaper(20)

  schedule.every().hour.do(change_wallpaper)
  while True:
    check_wallpaper(5)
    schedule.run_pending()
    time.sleep(59)
