import time
import webbrowser

i = 0
print("This program started at " + time.ctime())
while i <= 3:

    time.sleep(20)
    webbrowser.open("https://www.youtube.com/watch?v=hzExWz7KP5M")

    i = i + 1