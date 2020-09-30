import pyautogui as py
import pandas as pd
from time import sleep

whatsapp_api = "https://api.whatsapp.com/send?phone=91"  # whatsapi
hello = "Hey, "
message = "This is to remind you that the C/C++ workshop is tomorrow at 3:30pm. Location will be given out soon (Most probably SL 2,3 Lab in N-building, 1st floor). Do confirm if you'll be attending the workshop :D\n\nSee you tomorrow!"

# Countdown to start the bot
def timer():   #setting up timer
    for x in range(5, 0, -1):
        print(x)
        time.sleep(1)

def sendMessage(num, name): # send message
    api = whatsapp_api + str(num)
    final = hello + name + "!\n" + message
    print(api, name)
    
    # New Tab
    py.hotkey('ctrl', 't')
    sleep(1)
    
    # Type URL
    py.typewrite(api, interval = 0.01)
    py.press('enter')
    sleep(3)
    
    # Click on Message button
    py.click(680, 360)
    sleep(15)
    
    # Enter the message
    py.typewrite(final, interval = 0.01)
    py.press('enter')
    sleep(5)
    
    # Close the window
    py.hotkey('ctrl', 'w')
             

if __name__ == "__main__":
    timer()
    excel = pd.read_excel("New.xlsx")  //reading excel file
    numbers = excel['Number'].tolist()
    names = excel['Name'].tolist()
    ctr = 0
    for num, name in zip(numbers, names):
        sendMessage(num, name)
        ctr += 1
        if ctr == 30:
            break
            
    # Minimize all windows on completion
    py.hotkey('win', 'm')
    
