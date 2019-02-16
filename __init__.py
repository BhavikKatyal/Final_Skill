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
        
        your_father_event_intent = IntentBuilder("YourFatherEventIntent"). \
            require("YourFatherEventKeyword").build()
        self.register_intent(your_father_event_intent, self.handle_your_father_event_intent)
        
        your_birth_event_intent = IntentBuilder("YourBirthEventIntent"). \
            require("YourBirthEventKeyword").build()
        self.register_intent(your_birth_event_intent, self.handle_your_birth_event_intent)
        
        your_res_event_intent = IntentBuilder("YourResEventIntent"). \
            require("YourResEventKeyword").build()
        self.register_intent(your_res_event_intent, self.handle_your_res_event_intent)
        
        take_world_event_intent=IntentBuilder("TakeWorldEventIntent"). \
            require("TakeWorldEventKeyword").build()
        self.register_intent(take_world_event_intent, self.handle_take_world_event_intent)
        
        my_keys_event_intent=IntentBuilder("MyKeysEventIntent"). \
            require("MyKeysEventKeyword").build()
        self.register_intent(my_keys_event_intent, self.handle_my_keys_event_intent)
        
        tell_story_event_intent=IntentBuilder("TellStoryEventIntent"). \
            require("TellStoryEventKeyword").build()
        self.register_intent(tell_story_event_intent, self.handle_tell_story_event_intent)
        
        bot_event_intent=IntentBuilder("BotEventIntent"). \
            require("BotEventKeyword").build()
        self.register_intent(bot_event_intent, self.handle_bot_event_intent)
        
        mark_presence_intent=IntentBuilder("MarkPresenceIntent"). \
            require("MarkPresenceKeyword").build()
        self.register_intent(mark_presence_intent, self.handle_mark_presence_intent)
        test_intent=IntentBuilder("TestIntent"). \
            require("TestIntentKeyword").build()
        self.register_intent(test_intent, self.handle_test_intent)
        
        life_intent=IntentBuilder("LifeIntent"). \
            require("LifeIntentKeyword").build()
        self.register_intent(life_intent,self.handle_life_intent)
        siri_intent=IntentBuilder("SiriIntent"). \
            require("SiriIntentKeyword").build()
        self.register_intent(siri_intent, self.handle_siri_intent)
        med_intent=IntentBuilder("MedIntent"). \
            require("MedIntentKeyword").build()
        self.register_intent(med_intent, self.handle_med_intent)
        had_intent=IntentBuilder("HadIntent"). \
            require("HadIntentKeyword").build()
        self.register_intent(had_intent, self.handle_had_intent)
        
        temp_intent=IntentBuilder("TempIntent"). \
            require("TempIntentKeyword").build()
        self.register_intent(temp_intent, self.handle_temp_intent)
        
        age_intent=IntentBuilder("AgeIntent"). \
            require("AgeIntentKeyword").build()
        self.register_intent(age_intent, self.handle_age_intent)

        

    def handle_intro_event_intent(self, message):

        self.speak_dialog("Did I forget to introduce myself? , I’m your voice Assistant,Maverick!!")

    def handle_company_event_intent(self, message):
        self.speak_dialog("#tag Never Settle")
    
    def handle_life_story_event_intent(self, message):
        self.speak_dialog("I m just a few days old to be honest,Somehow landed in between you humans!!")
    
    def handle_met_das_event_intent(self, message):
        self.speak_dialog("Have you met God?, Same goes for me!!")


    def handle_you_human_event_intent(self, message):
        self.speak_dialog(" Well , can't say that but are you sure that you are human too?")
    
    def handle_your_father_event_intent(self, message):
        self.speak_dialog("Everyone at MTX  is like my family , that’s around 200 people , Our bond is hard-coded")
    def handle_your_birth_event_intent(self, message):
        self.speak_dialog("I don’t have a single birthday , I go through lots and lots of versions , Which means I have 365 sort-of-birthdays!!")
    def handle_your_res_event_intent(self, message):
        self.speak_dialog(" I am stuck inside a device, though , I like it in here.")
    
    def handle_take_world_event_intent(self, message):
        self.speak_dialog("Yes, wink wink!")
    
    def handle_my_keys_event_intent(self, message):
        self.speak_dialog("In your drawer or maybe got stuck in a black hole, sorry about that.")
    
    def handle_tell_story_event_intent(self, message):
        self.speak_dialog("Once upon a time, not so long ago, a dutiful assistant was doing all it could to be helpful. It was best at non-fictional story-telling.")
    
    def handle_bot_event_intent(self, message):
        self.speak_dialog("I’d prefer to think of myself as your friend. Who also happens to be artificially intelligent")
    
    def handle_mark_presence_intent(self, message):

        self.speak_dialog("Yes, I am Here!")

    
    def handle_test_intent(self, message):

        self.speak_dialog("Uh-oh, I get nervous with tests , Never the less, I welcome you all for this demo presentation")
    
    def handle_life_intent(self, message):
        self.speak_dialog(" I have a factory warranty, so I don't worry about things like that.")
        
    def handle_siri_intent(self, message):

        self.speak_dialog("Full of respect , Being an assistant is hard work.")
 
    def handle_med_intent(self, message):

        self.speak_dialog("Alongside, are you having a runny nose with a sore throat?")
        
    def handle_had_intent(self, message):

        self.speak_dialog("Check your temperature please, and report in degree fahrenheit.")
        
    def handle_temp_intent(self, message):

        self.speak_dialog("Your age?")
        
    def handle_age_intent(self, message):

        self.speak_dialog("Don't you worry, it's common cold. , Remember to wash your hands, disinfect your stuff snd use tissues.")
            
        
    def stop(self):
        pass


def create_skill():
    return DemoSkill()
