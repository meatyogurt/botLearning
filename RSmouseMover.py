import pyautogui 
import time 
import random 


# Locate RuneLite icon
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\RSicon.png', confidence=0.8)

if result is not None:
    # Convert the Box object to standard integers
    center = pyautogui.center(result)
    
    # Convert NumPy int64 to regular Python int
    center_x = int(center.x)
    center_y = int(center.y)
    
    print(f"Center of the image: ({center_x}, {center_y})")
    
    # Move the mouse to the center of the image over 3 seconds
    pyautogui.moveTo(center_x, center_y, 3, pyautogui.easeOutQuad)

         # Wait for a quarter of a second (250 milliseconds)
    time.sleep(.25)
    
    # Perform a double-click
    pyautogui.doubleClick()

    time.sleep(30)
else:
    print("Image not found.")











# Locate Existing Users button
result = pyautogui.locateOnScreen(r'C:\Users\User\Desktop\mouseMoverImages\ExistingUser.png', confidence=0.8)

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
    
    # Perform a single click
    pyautogui.click()

else:
    print("Image not found.")





# Function to simulate human-like typing with a slightly uneven speed
def human_like_typing(text):
    for char in text:
        pyautogui.write(char)
        time.sleep(random.uniform(0.03, 0.1))  # Random interval between 30ms to 100ms

# Your username and password
username = "yourUsername"
password = "yourPassword"

# Type the username with uneven but fast human-like speed
human_like_typing(username)

# Press Enter after typing the username
pyautogui.press('enter')

# Small pause before typing the password
time.sleep(0.5)

# Type the password with uneven speed
human_like_typing(password)

# Optionally press Enter after typing the password
pyautogui.press('enter')






#while True:  # this loop prints the mouse location in the console 
    #x, y = pyautogui.position()
    #print(f"Mouse position: ({x}, {y})")
    #time.sleep(1)