import sys


messages = ["Welcome to Socks and Shirts!", #Code: 0
 "What is your name? ", #Code: 1
 "Thank you, ", #Code: 2
 "How can we assist you today?\n\t1) Order shirts\n\t2) Questions\n\t3) Complaints\n"] #Code: 3
def getPreloadedMessages(messageCode):
 global messages
 return messages[messageCode]
