import pyautogui 
import time 
import random 


#for this code to work right click on screen and make sure display settings, Scale and Layout are set to 150%


# Locate Jagex Launcher icon on desktop
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\RSicon.png', confidence=0.8)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 2 seconds
    pyautogui.moveTo(center_x, center_y, 2, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a double-click
    pyautogui.doubleClick()

    time.sleep(5)
else:
    print("Jagex launcher not found.")















# Locate PLAY button on JAGEX LAUNCHER
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\play.png', confidence=0.8)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 1 seconds
    pyautogui.moveTo(center_x, center_y, 0.5, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a single click
    pyautogui.click()

    time.sleep(30)
else:
    print("Jagex Play button not found.")
















# Locate clicktoswitch button on RUNLITE
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\clicktoswitch.png', confidence=0.5)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 1 seconds
    pyautogui.moveTo(center_x, center_y, 0.5, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a single click
    pyautogui.click()

    time.sleep(5)

else:
    print("World Switcher Not found.")














# Locate world worldnumber button on RUNLITE
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\world433.png', confidence=0.7)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 1 seconds
    pyautogui.moveTo(center_x, center_y, 0.5, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a single click
    pyautogui.click()

    time.sleep(3)

else:
    print("img not found.")




























    # Locate world world433 button on RUNLITE
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\playnow.png', confidence=0.5)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 1 seconds
    pyautogui.moveTo(center_x, center_y, 1, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a single click
    pyautogui.click()

    time.sleep(10)

else:
    print("img not found.")












    # Locate click to play
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\clicktoplay.png', confidence=0.7)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 1 seconds
    pyautogui.moveTo(center_x, center_y, 0.5, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a single click
    pyautogui.click()

else:
    print("img not found.")


