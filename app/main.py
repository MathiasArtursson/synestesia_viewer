import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('1.9.0') #play around if it does not work on your phone

class MyRoot(BoxLayout):

    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 100))


class SynestesiaViewer(App):

    def build(self):
        return MyRoot()


synestesiaViewer = SynestesiaViewer()
synestesiaViewer.run()