# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Dict, Text, Any, List, Union, Optional
import logging
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, EventType
from parsing import (
    parse_duckling_time_as_interval,
    parse_duckling_time,
    get_entity_details,
)

logger = logging.getLogger(__name__)

class ActionFaqs(Action):
    """Returns the chitchat utterance dependent on the intent"""

    def name(self):
        return "action_faqs"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message["intent"].get("name")
        print(tracker.latest_message)
        
        if "FAQ" in intent:
            dispatcher.utter_message(template = f"utter_"+ intent)
        return []