#printStuff
import sys
sys.path.append("../Controllers")

import messageFetcher

name = ""

def startClient():
  print messageFetcher.fetchMessage(0)
  global name
  name = raw_input(messageFetcher.fetchMessage(1)).rstrip()
  return name
def getUserInput():
  global name
  mytxt = raw_input(name + ': ').rstrip()
  return mytxt