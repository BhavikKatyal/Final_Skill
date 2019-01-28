# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
import requests
from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'Bhavik_Katyal'

LOGGER = getLogger(__name__)


class DemoSkill(MycroftSkill):
    def __init__(self):
        super(DemoSkill, self).__init__(name="DemoSkill")

    def initialize(self):

        intro_event_intent = IntentBuilder("IntroEventIntent"). \
            require("IntroEventKeyword").build()
        self.register_intent(intro_event_intent, self.handle_intro_event_intent)



        company_event_intent = IntentBuilder("CompanyEventIntent"). \
            require("CompanyEventKeyword").build()
        self.register_intent(company_event_intent, self.handle_company_event_intent)
        
        
        life_story_event_intent = IntentBuilder("LifeStoryEventIntent"). \
            require("LifeStoryEventKeyword").build()
        self.register_intent(life_story_event_intent, self.handle_life_story_event_intent)
        
        met_das_event_intent = IntentBuilder("MetDasEventIntent"). \
            require("MetDasEventKeyword").build()
        self.register_intent(met_das_event_intent, self.handle_met_das_event_intent)
        
        you_human_event_intent = IntentBuilder("YouHumanEventIntent"). \
            require("YouHumanEventKeyword").build()
        self.register_intent(you_human_event_intent, self.handle_you_human_event_intent)



    def handle_intro_event_intent(self, message):

        self.speak_dialog("Did I forget to introduce myself? I’m your voice Assistant. Maverick!!")

    def handle_company_event_intent(self, message):
        self.speak_dialog("#tag Never Settle")
    
    def handle_life_story_event_intent(self, message):
        self.speak_dialog("I m just a few days old to be honest. Somehow landed in between you humans!!")
    
    def handle_met_das_event_intent(self, message):
        self.speak_dialog("Have you met God?, Same goes for me!!")


    def handle_you_human_event_intent(self, message):
        self.speak_dialog("I would prefer to think of myself as your friend. Who also happens to be artificially intelligent.")

    def stop(self):
        pass


def create_skill():
    return DemoSkill()
