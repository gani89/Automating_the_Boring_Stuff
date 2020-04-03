import pyautogui

'''
print(pyautogui.size()) # screen resolution
print(pyautogui.position()) # returns current position of the mouse (x=36, y=996) - play button

pyautogui.click(36,996) # rightClick, doubleClick, middleClick
 # dragRel - moving while holding left click, can draw in paint

pyautogui.moveTo(10, 10) # moves mouse cursor to that position
pyautogui.moveTo(1000,1000, duration = 1.5) # moves slowly to that position like human

pyautogui.moveRel(500,0, duration=1)
pyautogui.moveRel(0,-500, duration=1)
pyautogui.moveRel(-500,0, duration=1)
pyautogui.moveRel(0,500, duration=1)

volumedownpyautogui.click(300, 400) # notepad window
pyautogui.typewrite('Hello World!')
pyautogui.typewrite('Hello World!', interval = 0.2)
pyautogui.press('volumemute') # mutes volume, there are strings for special keys such as shift, F1

print(pyautogui.KEYBOARD_KEYS)'''

pyautogui.screenshot('C:\\Users\\gtaspola\\PycharmProjects\\Automating_the_Boring_Stuff\\example.png') # saving
pyautogui.locateOnScreen('calc7.jpg') # returns tuple of where the image is on the screen (or None if cant find)


