# Returns random post titles to RandomVoat.py

import random


# Grab 10 random lines from scraper dump file
sentencePool = random.sample(list(line.rstrip('\n') for line in open('/home/pi/RandomVoat/postTitles.txt')), 10)
                                                                     
def main():

    run = True
    
    while run:
        totalPost = [random.choice(sentencePool),
                     random.choice(sentencePool),
                     random.choice(sentencePool)]
        
        joinedPost = ' '.join(totalPost)
        charCount = len(joinedPost)

        # check for twitter's 140 char max
        if charCount <= 140:
            return joinedPost
            run = False


main()
