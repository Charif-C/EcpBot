
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
        
        result = rep.result
        action = rep.action
        intent = rep.intent

        if intent == "AuRevoir":
            print("Au revoir !")
            break

        actionIncomplete = rep.actionIncomplete
        contexts = rep.contexts

        if len(contexts)>0 :
            context = contexts[0]
        else:
            context=None

        print(u"< %s" % rep.speech)

        if action is not None:
            if action == u"send_message":
                parameters = rep.parameters

                text = rep.text
                message_type = rep.message_type
                parent = rep.parent

                print (
                    'text: %s, message_type: %s, parent: %s' %
                    (
                        text if text else "null",
                        message_type if message_type else "null",
                        parent if parent else "null"
                    )
                )

                if not actionIncomplete:
                    print(u"...Sending Message...")
                    break


if __name__ == '__main__':
    main()