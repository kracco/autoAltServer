This project (for lazy people) provides a Python script to automate the opening of AltServer and the entry of your Apple account credentials. The goal is to simplify the process of installing and managing AltStore on an iOS device.

**Important Note:** This script is intended for demonstration purposes and may not be perfect for all users. It was created by a programming novice and might require adjustments to fit different system configurations. Any tips are appreciated!

### Features

- Automatically launches AltServer.
- Interacts with AltServer's user interface to install AltStore.
- Enters Apple account credentials via automated GUI interaction.

### Prerequisites

To run this script, you'll need:
- [Python](https://www.python.org/downloads/) installed on your system.
- The `pyautogui` module for simulating GUI interactions.

### Usage

The script will perform the following actions:
- Launch AltServer.
- Click the necessary icons to start the AltStore installation (based on iPhone, probably if you use another idevice you should take a screenshot of what AltServer recognize as connected to your PC and change the image in "iphone_button.png").
- Enter your Apple account credentials (you MUST edit the .py file adding your email address, email domain and password).

### Run the script
You can make a very simple script in .cmd to open your .py based on where you have placed the code, open a now note and write:

`python "...\autoAltServer.py"`

where instead of `...` you should insert the path where "autoAltServer.py" is located.
After that, rename the .txt into .cmd and you are done!
