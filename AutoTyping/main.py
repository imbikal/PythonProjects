import pyautogui
import time

while True:
    time.sleep(3)
    pyautogui.typewrite("K cha")
    pyautogui.press('Enter')

#So what happens is after we click run immediately check where we want to send message put cursor over there, then in every 3 seconds gap message is sent. Here typewrite writes the message and 'Enter'is automatically pressed

""" 

# Set the number of repetitions
num_repeats = 100

for _ in range(num_repeats):
    time.sleep(3)  # Sleep for 3 seconds before typing
    pyautogui.typewrite("K cha", interval=0.1)  # Adjust the typing speed if needed
    pyautogui.press('Enter')

print("Done typing 100 times!") 

"""