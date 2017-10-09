"""
Name: Stephen Ohl
Date:
Brief Project Description:
A program that keeps a record of songs the user has learnt
and a record of songs to learn
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):
    def build(self):
        self.title = "Songs to learn 2.0"
        self.root = Builder.load_file('app.kv')
        return self.root

SongsToLearnApp().run()
