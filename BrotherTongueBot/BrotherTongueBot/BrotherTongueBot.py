
import os
import sys
import json
from Response import Response
from API import  API

# e5dc21cab6df451c866bf5efacb40178


print("Dire Bonjour pour commencer \n")

TimeOut = 10 #secondes

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
                parameters = result['parameters']

                text = parameters.get('text')
                message_type = parameters.get('message_type')
                parent = parameters.get('parent')

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