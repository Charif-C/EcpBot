
import os
import sys
import json
from Response import Response
from API import  API

print("Dire Bonjour pour commencer \n")

def main():
    
    ai =API()

    while True:
        user_message= ''
        while len(user_message)==0:
            print(u"> ", end=u"")
            user_message=input()

        rep=Response(ai._get_json_response(user_message))
        
        result = rep._get_result
        action = rep._get_action
        intent = rep._get_intent

        if intent == "AuRevoir":
            print("Au revoir !")
            break

        actionIncomplete = rep.get_actionIncomplete
        contexts = rep._get_contexts

        if len(contexts)>0 :
            context = contexts[0]
        else:
            context=None

        print(u"< %s" % rep.speech)

        if action is not None:
            if action == u"send_message":
                parameters = rep._get_parameters

                text = rep._get_text
                message_type = rep._get_message_type
                parent = rep._get_parent

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