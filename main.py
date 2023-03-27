#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#########################################################################################
#Title: main.py
#Author: Douglas T.
#Creation Date: 03/25/2023
#Description: The main file for the Score a Bowling Game App
#
#Changelog:
#Name:          Date:       Change:
# Douglas T.    03/25/2023  Initial version
#########################################################################################

import kivy
import backend

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import FocusBehavior

class BowlingGame(FloatLayout):
    pass

class BowlingApp(App):
    def build(self):
        return BowlingGame()

if __name__ == '__main__':
    BowlingApp().run()
