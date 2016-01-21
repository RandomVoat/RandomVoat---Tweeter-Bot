# Returns random post titles to RandomVoat.py

import random
import subprocess

FILE = [line.rstrip('\n') for line in open('/home/pi/RandomVoat/postTitles_revise.txt')]
EVEN = [0,2,4,6,8,10,12,14,16,18,20]
CMD = "ruby /home/pi/RandomVoat/scraper_voat_revise.rb"

def main():

    randomSelect = random.choice(EVEN)
    nextLine = randomSelect + 1
    
    subprocess.call(CMD, shell=True)

    title = FILE[randomSelect]
    href = FILE[nextLine]
    
    if len(title) <= 110:
        status = (title + ' - ' + href)
    else:
        status = (title[:110] + '... - ' + href)

    return status


main()

