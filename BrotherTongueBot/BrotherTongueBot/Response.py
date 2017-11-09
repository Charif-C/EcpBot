class Response:
    """description of class"""
    def __init__(self, response):
        """Constructeur de notre classe"""

        self.result =  response['result']
        self.action = response['result'].get('action')
        self.intent = response['result']["metadata"].get('intentName')
        self.actionIncomplete = response['result'].get('actionIncomplete', False)
        self.contexts = response['result'].get('contexts')    
        self.parameters = self.result['parameters']
        self.text = self.result['parameters'].get('text')
        self.message_type = self.result['parameters'].get('message_type')
        self.parent = self.result['parameters'].get('parent')
        self.speech = response['result']['fulfillment']['speech']