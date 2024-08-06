import pyautogui
import keyboard
import time
import subprocess

# Path to AltServer executable, it might be installed in another path in your case
altserver_path = r'C:\Program Files (x86)\AltServer\AltServer.exe'

# iOS Credentials of AltStore
email = '' # example: 'name.surname123'
domain = '' # example: 'gmail.com'
password = '' # example: 'password'

# Function to start AltServer
def open_altserver():
    subprocess.Popen(altserver_path)
    time.sleep(2)  # Wait for AltServer to open

# Function to click on an icon specified by image
def find_img(img_path, confidence=0.9):
    location = pyautogui.locateOnScreen(img_path, confidence=confidence)
    if location is not None:
        center = pyautogui.center(location)
        pyautogui.click(center)
    else:
        print(f"Image {img_path} not found.")

# Function to enter credentials
def enter_credentials():
    pyautogui.press('tab')
    pyautogui.write(email)
    keyboard.write('@')
    pyautogui.write(domain)
    pyautogui.press('tab')
    pyautogui.write(password)
    pyautogui.press('enter')

# Execute functions in the desired order
open_altserver()
time.sleep(1)  # Wait for AltServer to fully start
find_img('hidden_icon.png', confidence=0.9)
time.sleep(0.5)
find_img('altserver_icon.png', confidence=0.9)
time.sleep(0.5)
find_img('install_altstore_button.png', confidence=0.9)
time.sleep(0.5)  # Wait for the iPhone selection window to appear
find_img('iphone_button.png', confidence=0.9)
time.sleep(0.5)  # Wait for the credentials entry window to appear
enter_credentials()