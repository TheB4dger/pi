#!/usr/bin/env python3

import pifacecad
import time

MenuText = "1: Welcome 2:GS\n3:Clock [4/5]:BL"

def update_pin_text(event):
	event.chip.lcd.write(str(event.pin_num))
	choice = event.pin_num
	if choice == 0:
		cad.lcd.clear()
		cad.lcd.write("Welcome Selected")
		time.sleep(5)
#		import subprocess
#		p = subprocess.Popen(["sysstart"])
#		output, err = p.communicate()
		cad.lcd.clear()
		cad.lcd.backlight_on()
		cad.lcd.write(MenuText)
	if choice == 1:
		cad.lcd.clear()
		cad.lcd.write("GSL countdown\nselected")
		time.sleep(5)
#		import subprocess
#		p = subprocess.Popen(["GSL2014"])
#		output, err = p.communicate()
		cad.lcd.clear()
		cad.lcd.backlight_on()
		cad.lcd.write(MenuText)
	if choice == 2:
		cad.lcd.clear()
		cad.lcd.write("Current time: \n")
		cad.lcd.write(time.ctime())
		time.sleep(5)
		cad.lcd.clear()
		cad.lcd.write(MenuText)
	if choice == 3:
		cad.lcd.backlight_on()
	if choice == 4:
		cad.lcd.backlight_off()

cad = pifacecad.PiFaceCAD()
cad.lcd.backlight_on()
cad.lcd.write("Pi menu, Use the \n buttons")
time.sleep(2)
cad.lcd.clear()
cad.lcd.write(MenuText)

listener = pifacecad.SwitchEventListener(chip=cad)
for i in range(6):
	listener.register(i, pifacecad.IODIR_FALLING_EDGE, update_pin_text)
listener.activate()
