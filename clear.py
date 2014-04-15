#!/usr/bin/env python3
import sys
import subprocess
import pifacecad

cad = pifacecad.PiFaceCAD()
lcd = cad.lcd
lcd.backlight_off()
lcd.clear()
lcd.display_off()