## control your computer
from pyautogui import typewrite,hotkey,click
from subprocess import Popen
from time import sleep
file=open('泽神牛逼.txt','w')

file.close()

Popen(['start','泽神牛逼.txt'],shell=True)
sleep(0.5)

typewrite('!nide diannao yijing beiwo kongzhile !',0.2)
typewrite(['enter'])
typewrite("!woshi nibaba !",0.2)
hotkey('ctrl','s')