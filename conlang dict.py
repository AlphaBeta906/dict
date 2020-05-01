#IF JOINING PLS COMMIT NEWEST ONE!!! 
import time as t
print ("Altanio Conlang Dictionary Ver. 1 Alpha 1")
import socket as s
name = s.gethostbyname()
IP = s.gethostname(name)
if IP = 192.168.5.101:
    print ("Hello Master Alpha")
else:
    print ("Hello Guest")
t.sleep(2)
a = {"people": "Alta", "land": "Garda", "sea": "Souhl", "city": "Altagarda", "crop": "Wazha",}
words = ["people", "land", "sea", "city", 'crop']
while True:
    question = input("Word? P.S: Do not make it any character upper")
    #NOTE TO SELF: FIX BIG UPPER OR LOWER
    t.sleep(2)
    if question in words:
        question = question.lower()
        print (a[question] + " is " + question)
    elif question == "E":
        print ("Ended")
        break
    else:
        print ("Not in dict")
#LOOP GOOD :D
