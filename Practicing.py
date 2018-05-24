# Basic Web Crawler By MohamadKh75
# Animated Loading by Andrew Clark (Found the code in StackOverFlow)
# **********

import itertools
import threading
import time
import sys
import requests
from bs4 import BeautifulSoup
import codecs


print("\n\tEnter the BASE url:  -  \"git.ir\" is a good example!")
print("1. MUST BE the template (/page/) - DO NOT enter http://")
print("2. Type it! (DO NOT paste url!\n")

ask = input()
print('\n')

fw = codecs.open("info.txt", 'a', 'utf-8')
fw.write("##########\n")
fw.write("Source: " + ask + '\n')
fw.write(time.strftime("%Y.%m.%d - %I:%M:%S (%p)"))
fw.write("\n##########\n\n")


done = False


def spider(max_pages = 2):
    page = 1

    while page <= max_pages:
        url = "http://" + ask + str(page)
        # url = "http://git.ir/page/" + str(page)
        source = requests.get(url)
        plain_txt = source.text
        target = BeautifulSoup(plain_txt, "html.parser")

        for link in target.findAll('img', {'class': "attachment-full size-full wp-post-image"}):
            href = str(link.get("src"))
            title = str(link.get('alt'))

            fw.write(title + '\n')
            fw.write(href + '\n\n')

        page += 1


def animate():
    for c in itertools.cycle(['', '.', '..', '...']):
        if done:
            break
        sys.stdout.write('\rLoading' + c)
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write('\rDone!     ')


t = threading.Thread(target=animate)
t.start()

spider(2)

fw.write('\n' * 5)
fw.close()

time.sleep(3)
done = True