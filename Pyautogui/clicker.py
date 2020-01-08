import pyautogui
import keyboard
from time import sleep

clicar = False
while True:
	if keyboard.is_pressed('q'):
		break
	if keyboard.is_pressed('Enter'):
		clicar = True

	if clicar:
		pyautogui.tripleClick()
		if keyboard.is_pressed('Esc'):
			clicar = False
		if keyboard.is_pressed('q'):
			breakq
