''' 
Eric West
Erictwitter
python 2.7.9

For this app you will need to import the python-twitter library using pip install.
you will also need to be a registered twitter developer to recieve oAuth information to access twitters API information.
I have privided the url below to become a twitter developer. All you need to do is login wiht your twitter account
and create a new app to recieve oAuth information. 

The program will ask you for your twitter username ie: @ewest861 then a web browser should open
with a color coded copy of your last tweet. Your username should be blue, 
any other  users should be red and hastags should be green.

'''

from twitter import * # used pip install python-twitter https://pypi.python.org/pypi/python-twitter
import re
import webbrowser, os.path

#You will need to register as a twitter developer to retrieve twitter information, or you can use my information below
#https://apps.twitter.com/      Create a new app and use tokens to access the API information
# --- oAuth Information -----------------------------------------------

OAUTH_TOKEN		    = '416427187-A3oD0gOAH6IBhg84niZSXBMAyfroaLqfk3YouvFA'
OAUTH_SECRET		= 'svtmBTyb89PisVRD8zTkinPDx6qj6fmi7Fx9pSF5uBtV1'
CONSUMER_KEY		= 'JGERP3dT2xx1yxWNpeGEEFPsD'
CONSUMER_SECRET	    = 'nYd5wtWEuwXWp5rGZLKo2iQzhx1e99ndfaSHmELVsnG91JtMOx'

# ---------------------------------------------------------------------

class Erictwitter:
#initializes the oAuth information and  defines cnstants for the colors
    def __init__(self,OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET):

        # Some color constants for formatting
        self.BLUE		= '<font color = "blue">'
        self.GREEN		= '<font color = "green">'
        self.RED		= '<font color = "red">'
        self.MAGENTA	= '<font color = "magenta">'
        self.ENDCOLOR	= '</font>'

        # Some regex pattern compilations for coloring usernames and hashtags
        self.reUser 	= re.compile(r"(?<=^|(?<=[^a-zA-Z0-9-\.]))@([A-Za-z_]+[A-Za-z0-9_]+)")
        self.reHashtag	= re.compile(r"(?<=^|(?<=[^a-zA-Z0-9-\.]))#([A-Za-z_]+[A-Za-z0-9_]+)")
        # Setup Twitter API
        self.t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
# retrieves the last tweet  from the user and assins the colors to the appropiate symbols
#uses an excption handler to let the user know if anything goes wrong
    def printLastTweet(self, username):

        try:
            timeline = self.t.statuses.user_timeline(screen_name=username,count=1)

            return '\n'.join({self.BLUE + '@' + tweet['user']['screen_name'] + self.ENDCOLOR + ": "
                             + re.sub(self.reUser, self.RED + r'@\1' + self.ENDCOLOR,
                                      re.sub(self.reHashtag, self.GREEN + r'#\1' + self.ENDCOLOR,tweet['text']))
                             for tweet in timeline})
        except:
            print 'There was a problem getting tweets for ' + username + '. Please try again!'

#tells the user to input twitter username then plugs in all the inputs for all methods
if __name__ == "__main__":

    username = raw_input("Enter a twitter @ username:")
    ct = Erictwitter(OAUTH_TOKEN,OAUTH_SECRET,CONSUMER_KEY,CONSUMER_SECRET)
    ct.printLastTweet(username)

#creates a webfile
webFile = file('pythonout.html', 'w')

#Use multiple write methods to create the tags that make up the webpage
webFile.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">''')
webFile.write('''<html>''')
webFile.write('''<head>''')
webFile.write('''<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />''')
webFile.write('''<title>EricTwitter</title>''')
webFile.write('''</head>''')
webFile.write('''<body style="background-color:#CCC">''')
webFile.write('''<h1>''' + ct.printLastTweet(username) + '''</h1>''')
webFile.write('''</body>''')
webFile.write('''</html>''')

#open the file automatically 
webbrowser.open("file:///" + os.path.abspath("pythonout.html"))

#close the webfile
webFile.close()



