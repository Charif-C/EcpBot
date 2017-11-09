
import os
import sys
from Response import *
from API import *

print("Dire Bonjour pour commencer \n")

def main():
    
    ai =API()

    while True:
        user_message= ''
        while len(user_message)==0:
            print(u"> ", end=u"")
            user_message=input()

        rep=Response(ai._get_json_response(user_message))
        try:
            _result = rep.result
            _action = rep.result.action
            _intent = rep.result.metadata.intentName
        except:
            pass
        if _intent == "AuRevoir":
            print("Au revoir !")
            break

        actionIncomplete = rep.result.actionIncomplete
        contexts = rep.result.contexts

        if len(contexts)>0 :
            context = contexts[0]
        else:
            context=None

        print(u"< %s" % rep.result.fulfillment.speech)


if __name__ == '__main__':
    main()