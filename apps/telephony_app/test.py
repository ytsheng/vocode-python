import os
from vocode.streaming.telephony.hosted.outbound_call import OutboundCall
from vocode.streaming.models.agent import ChatGPTAgentConfig
from vocode.streaming.models.telephony import CallEntity, TwilioConfig
from vocode.streaming.models.message import BaseMessage

from dotenv import load_dotenv
load_dotenv()

import vocode
vocode.api_key = os.getenv("VOCODE_API_KEY")

if __name__ == '__main__': 
    call = OutboundCall(
        recipient = CallEntity(phone_number = "+17348347849"),  # Replace with the number you want to call to
        caller = CallEntity(phone_number = "+18339232093"),  # Replace with the number you want to call from
        agent_config = ChatGPTAgentConfig(
            initial_message = BaseMessage(text = "Hello!"),  # Starting message of the call
            prompt_preamble = "Have a pleasant conversation about life",  # The conversation context 
        ),
        twilio_config = TwilioConfig(
            account_sid = os.getenv("TWILIO_ACCOUNT_SID"),
            auth_token = os.getenv("TWILIO_AUTH_TOKEN"),
        )
    )
    call.start()
    input("Press enter to end the call...")
    call.end()