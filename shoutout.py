# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:

# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce:

# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry
# Note: If you are not using windows, try to figure out how to do the same thing using some other package

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

names=["Ali","Fahad","Haider"]
for name in names:
    speaker.Speak(f"shoutout to{name}")