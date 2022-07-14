# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount

import requests


#john wick mm num
MM_NUM = 310193917

class EchoBot(ActivityHandler):


    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("Hello and welcome!")

    async def on_message_activity(self, turn_context: TurnContext):
        header = {'Authorization': 'Basic Z2VuZXN5c2FkbWluLUkzOiFnZW5lc3lzIzI4'}
        query = {'intentId': 'greet', 'mm_num': MM_NUM, 'language': 'en', 'sessionId': '0', 'sessionVars': 'null'}
        response = requests.post('http://localhost:8080/benefits/livekinnect/admin/processIntentOptionGenesysCloud', headers=header, json=query)

        message = response.json()['message']
        return await turn_context.send_activity(
            MessageFactory.text(message)
        )
