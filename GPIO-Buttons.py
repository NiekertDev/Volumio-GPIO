from gpiozero import Button
from subprocess import check_call
from signal import pause

# Edit these variables to match the corresponding pin

mainpin = 17
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
   print("Toggle button pressed")
   check_call(["volumio", "toggle", "&"])
   print("\n")

def previous():
   print("Previous button pressed")
   check_call(["volumio", "previous"])
   print("\n")

def next():
   print("Next button pressed")
   check_call(["volumio", "next"])
   print("\n")

def volumedown():
   print("Volume down button pressed")
   check_call(["volumio", "volume", "minus"])
   print("\n")

def volumeup():
   print("Volume up button pressed")
   check_call(["volumio", "volume", "plus"])
   print("\n")

def volumefull():
   print("Volume full button pressed")
   check_call(["volumio", "volume", "100"])
   print("\n")

def volumemute():
   print("Mute button pressed")
   check_call(["volumio", "volume", "mute"])
   print("\n")

def halt():
   print("Halt button pressed")
   check_call(["sudo", "halt"])
   print("\n")

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
