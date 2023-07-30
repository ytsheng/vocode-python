import os
from dotenv import load_dotenv

load_dotenv()
from vocode.streaming.telephony.hosted.outbound_call import OutboundCall

# from vocode.streaming.telephony.conversation.outbound_call import OutboundCall
from vocode.streaming.telephony.config_manager.redis_config_manager import (
    RedisConfigManager,
)
from vocode.streaming.models.agent import ChatGPTAgentConfig
from vocode.streaming.models.telephony import CallEntity, TwilioConfig

from vocode.streaming.models.message import BaseMessage


from speller_agent import SpellerAgentConfig
from dotenv import load_dotenv
load_dotenv()

import vocode
vocode.api_key = os.getenv("VOCODE_API_KEY")
# vocode.api_key = "5b4b0afa4b2b57edff08c99cb3f1961f"
# vocode.api_key = "4474f93ae1fb3d25acf82e6dc8ea3c57"
BASE_URL = os.environ["BASE_URL"]

def main():
# async def main():
    config_manager = RedisConfigManager()

    # outbound_call = OutboundCall(
    #     base_url=BASE_URL,
    #     to_phone="+17348347849",
    #     from_phone="+18339232093",
    #     config_manager=config_manager,
    #     # agent_config=SpellerAgentConfig(generate_responses=False),
    #      agent_config=ChatGPTAgentConfig(
    #         initial_message=BaseMessage(text="Hello!"),
    #         prompt_preamble="Have a pleasant conversation about life",
    #     ),
    #     twilio_config=TwilioConfig(
    #         account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
    #         auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    #     ),
    #     synthesizer_config=None,
    # )
    call = OutboundCall(
        recipient=CallEntity(
            phone_number="+17348347849",
        ),
        caller=CallEntity(
            phone_number="+18339232093",
        ),
        agent_config=ChatGPTAgentConfig(
            initial_message=BaseMessage(text="Hello!"),
            prompt_preamble="Have a pleasant conversation about life",
        ),
        twilio_config=TwilioConfig(
            account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
            auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
        )
    )
    call.start()
    input("Press enter to start call...")
    # await outbound_call.start()
    call.end()

if __name__ == "__main__":
    # import asyncio
    # asyncio.run(main())
    main()
