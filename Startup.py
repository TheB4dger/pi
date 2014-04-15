#!/usr/bin/env python3
import sys # pssibly remove?
import subprocess
from time import sleep
import pifacecad

UPDATE_INTERVAL = 1 #seconds

if __name__ == "__main__":
	cad = pifacecad.PiFaceCAD()
	cad.lcd.blink_off()
	cad.lcd.cursor_off()

	if "clear" in sys.argv:
		cad.lcd.clear()
		cad.lcd.display_off()
		cad.lcd.backlight_off()
	else:
		cad.lcd.backlight_on()
		cad.lcd.write("Om..")
		sleep(UPDATE_INTERVAL)
		cad.lcd.write("nom..")
		sleep(UPDATE_INTERVAL)
		cad.lcd.write("nom!")