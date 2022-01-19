import sys
import pyautogui
import time
# Import sys for saving image files, pyautogui for control of mouse movements, and time to allow program pauses

time.sleep(0.5)

print("Running autocompleter...")
print("Finding hint button...")

# screen = pyautogui.screenshot()                             # Take a screenshot for finding buttons


def findButtons():

    hintLocation = pyautogui.locateOnScreen("hint2.png", confidence=0.6)     # Search for the hint button on the screen
    if hintLocation:                                        # If the button is found...
        print("Hint button found!")                         # Debugging
        pyautogui.moveTo(hintLocation)                      # Move cursor to location of hint button
        pyautogui.click()                                   # I ain't explaining this one for you
    else:
        print(hintLocation)
        print("Hint button not found! Make sure the website is open and the hint button is visible")
        
    print("Finding ok button...")
    time.sleep(0.05)
    okLocation = pyautogui.locateOnScreen("okWhite3.png", confidence=0.75)    # Find ok button on screen
    if okLocation:                                          # If the button is found...
        print("ok button found!")  
        print(okLocation)
        pyautogui.moveTo(okLocation)                        # Move cursor to location of ok button
        pyautogui.click()                                   # You can figure this one out
        finishWebsite(hintLocation, okLocation)
    else:
        print(okLocation)                                   # debugging
        print("Hint button not found, are you on the right website?")
    time.sleep(5)                                           # Pause program for 5 seconds so user can read the error message
    sys.exit()                                              # Close the program

def finishWebsite(hintLocation, okLocation):
    count = 0
    while count < 500:
        pyautogui.moveTo(hintLocation)                      # Move cursor to location of hint button
        pyautogui.click()
        print("hintClicked")
        pyautogui.moveTo(okLocation)                      # Move cursor to location of hint button
        pyautogui.click()
        print("ok clicked")
        count += 1
    
    

findButtons()                                               # Call the function to find buttons


    

