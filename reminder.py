

# app to open webrowser
import webbrowser

import time


num_breaks = 3
i = 0

while i < num_breaks:
    #time.sleep(7200)
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=oTz93Y-qeq0")

    i += 1
