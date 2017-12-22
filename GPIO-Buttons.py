from gpiozero import Button
from subprocess import check_call
from signal import pause

# Edit these variables to match the corresponding pin

mainpin = 2
previouspin = 23
nextpin = 22
voldownpin = 24
voluppin = 25

main = Button(mainpin, hold_time=2)
previousbutton = Button(previouspin, hold_time=2)
nextbutton = Button(nextpin, hold_time=2)
voldown = Button(voldownpin, hold_time=2)
volup = Button(voluppin, hold_time=2)


def toggle():
   print("toggled")
   check_call(["volumio", "toggle", "&"])


def previous():
   print("previous")
   check_call(["volumio", "previous"])


def next():
   print("next")
   check_call(["volumio", "next"])

def volumedown():
   print("volumedown")
   check_call(["volumio", "volume", "minus"])

def volumeup():
   print("volumeup")
   check_call(["volumio", "volume", "plus"])

def volumefull():
   print("volumefull")
   check_call(["volumio", "volume", "100"])

def volumemute():
   print("mute")
   check_call(["volumio", "volume", "mute"])

def halt():
   print("halt")
   check_call(["sudo", "halt"])

main.when_pressed = toggle
main.when_held = halt

previousbutton.when_pressed = previous

nextbutton.when_pressed = next

voldown.when_pressed = volumedown
voldown.when_held = volumemute

volup.when_pressed = volumeup
volup.when_held = volumefull

print("Ready")

pause()
