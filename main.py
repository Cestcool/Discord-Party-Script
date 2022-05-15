from warnings import catch_warnings
import pyautogui
import time

print("How many character do you want to print ?")

user_input = 0
try:
    user_input = int(input("> "))
except:
    print("You must enter a number")

for i in range(user_input):
    pyautogui.press("q")

pyautogui.press("enter")