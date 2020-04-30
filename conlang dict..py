#IF JOINING PLS COMMIT NEWEST ONE!!! 
import time as t
print ("Altanio Conlang Dictionary Ver. 1 Alpha 1")
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
    elif question == "end" or "END":
        print ("Ended")
        break
    else:
        print ("Not in dict")
#LOOP GOOD :D
