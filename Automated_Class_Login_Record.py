# Imports
import pyautogui
import time
from pywinauto import Application

# Set Google Chrome directory
chrome_dir = r'"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'

# Start Google Chrome and point to URL
chrome = Application(backend='uia')
chrome.start(chrome_dir + ' --force-renderer-accessibility --start-maximized ' '[REDACTED-URL]')

# Sleep for five seconds waiting for connection
time.sleep(5)

# Login
pyautogui.typewrite('Guest\n', interval=0.1)

# Click mute button
pyautogui.click(x=X_COORD, y=Y_COORD, button='left')

# Click maximize button
pyautogui.click(x=X_COORD, y=Y_COORD, button='left')

# Start recording application


# Click record full screen button


# Sleep for one hour, thirty minutes (Time of recording) - MIGHT NEED TO ADD SECONDS BEFORE RECORDING STARTS
time.sleep(5400)

# Stop recording (Combination of keys - or specific key)


# Save recording - MIGHT NEED TO WAIT FOR COMPILATION TIME


# Close chrome


# Close recording application

