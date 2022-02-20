import random
import time
import webbrowser
while True:
    sites = random.choice(["youtube.com"])
    visit = "https://{}".format(sites)
    webbrowser . open(visit)
    seconds = (1)
    time.sleep(seconds)