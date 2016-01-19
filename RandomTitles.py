# Returns random post titles to RandomVoat.py

import random


# Grab 50 random lines from scraper dump file
sentencePool = random.sample(list(line.rstrip('\n') for line in open('/home/pi/RandomVoat/postTitles.txt')), 50)
                                                                     
def main():

    run = True
    
    while run:
        totalPost = [random.choice(sentencePool),
                     random.choice(sentencePool),
                     random.choice(sentencePool)]
        
        # check for title duplications
        if compareChoices(totalPost):
            joinedPost = ' '.join(totalPost)
            charCount = len(joinedPost)

        # check for twitter's 140 char max
        if charCount <= 140:
            return joinedPost
            run = False

def compareChoices(post):

    noDuplicates = False

    for i in range(1,len(post)):
        if post[i] != post[i-1]:
            noDuplicates = True

    return noDuplicates

	    
main()
