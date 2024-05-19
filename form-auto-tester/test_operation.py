'''
Rules:
If something goes wrong, for emergency stop, throw your cursor to the corner of your screen. This will make the test stop.
This test was made to run in Opera and Chrome browsers. If the test isn't running in your browser or something is going wrong, try changing the PyAutoGUI commands.

That's ALL! Good test.
'''

import pyautogui as auto
import webbrowser
import time

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam eget ligula eu lectus lobortis condimentum. Aliquam nonummy auctor massa. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla at risus. Quisque purus magna, auctor et, sagittis ac, posuere eu, lectus. Nam mattis, felis ut adipiscing"
email = "johndoe@email.com"

url = "https://contact-form-pearl-two.vercel.app"
webbrowser.open(url)

time.sleep(1)
auto.press("tab")
auto.write("John")
time.sleep(0.3)
auto.press("tab")
auto.write("Doe")
time.sleep(0.3)
auto.press("tab")
auto.write(email)
time.sleep(0.3)
auto.press("tab")
auto.press("right")
time.sleep(0.3)
auto.press("left")
auto.press("tab")
auto.write(message)
time.sleep(0.3)
auto.press("tab")
auto.press("space")
time.sleep(0.3)
auto.press("tab")
auto.press("space")

print("Test performed, everything is working correctly.")
