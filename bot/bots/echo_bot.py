from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

import requests
import re

class EchoBot(ActivityHandler):

    def __init__(self):
        self.message_idx = 1
        self.mm_num = 310193917 
        self.chatSessionId = 0


    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
         def parse_html_response(message):
            message.replace("<br/>", "\n")
            message.replace("<p>", "\n")
            message.replace("<li>", "\n")
            message = re.sub("<(.*?)>", "", message)
            return message
        
        header = {'Authorization': 'Basic Z2VuZXN5c2FkbWluLUkzOiFnZW5lc3lzIzI4'}
        query = {
                    'utterance': turn_context.activity.text,
                    # 'utterance': 'hello',
                    'mm_num': '310193917', 
                    'language': 'en', 
                    'sessionId': '0', 
                    'sessionVars': 'null'
                }
        response = requests.post('http://localhost:8080/benefits/livekinnect/admin/processIntentOptionGenesysCloud', headers=header, json=query)

        # print('response data:')
        # print(response)
        # print(response.json())

        message = response.json()['message']

        return await turn_context.send_activity(
            MessageFactory.text(message)
        )
