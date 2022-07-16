import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import random

kivy.require('1.9.0') #play around if it does not work on your phone

class BoxLayoutExample(BoxLayout): #class for layout
    pass
"""    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A") #input arguments same as properties in kivy-file
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
"""

class BoxLayoutApp(BoxLayout): #class for layout
    
    text_input_str = StringProperty("Colored word here")

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class MainWidget(Widget): #class for widget
    pass

class SynestesiaViewer(App):
    pass


synestesiaViewer = SynestesiaViewer()
synestesiaViewer.run()

def mixColors(dominant_color,recessive_color,ratio):
    return dominant_color - (dominant_color - recessive_color)/ratio

def loadColors():
    color_dict = {}
    color_dict["a"] = "fa5050"
    color_dict["b"] = "b85cab"
    color_dict["c"] = "d7f58c"
    color_dict["d"] = "7281cc"
    color_dict["e"] = "75f244"
    color_dict["f"] = "bfff80"
    color_dict["g"] = "71b49d"
    color_dict["h"] = "ffdfcc"
    color_dict["i"] = "ffffff"
    color_dict["j"] = "d9f0fa"
    color_dict["k"] = "e67b57"
    color_dict["l"] = "ffa666"
    color_dict["m"] = "ff0084"
    color_dict["n"] = "ff0090"
    color_dict["o"] = "363636"
    color_dict["p"] = "202fd4"
    color_dict["q"] = "6e6e6e"
    color_dict["r"] = "ff861c"
    color_dict["s"] = "ffeb54"
    color_dict["t"] = "ffed63"
    color_dict["u"] = "945934"
    color_dict["v"] = "6e4226"
    color_dict["w"] = "693f26"
    color_dict["x"] = "9c9c9c"
    color_dict["y"] = "e0b392"
    color_dict["z"] = "8c4818"
    color_dict["å"] = "9e0000"
    color_dict["ä"] = "ff7878"
    color_dict["ö"] = "5e5e5e"
    return color_dict