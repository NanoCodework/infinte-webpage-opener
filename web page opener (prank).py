import random
import time
import webbrowser
while True:
    #any site can be add for reference iam using youtube.coms
    sites = random.choice(["youtube.com"])
    visit = "https://{}".format(sites)
    webbrowser . open(visit)
    seconds = (1)
    time.sleep(seconds)