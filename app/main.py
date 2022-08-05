import kivy
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
import numpy as np
import matplotlib.pyplot as plt
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


def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return np.array([int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3)])


def loadColors():
    color_dict = {}
    color_dict["a"] = hex_to_rgb("fa5050")/255
    color_dict["b"] = hex_to_rgb("b85cab")/255
    color_dict["c"] = hex_to_rgb("d7f58c")/255
    color_dict["d"] = hex_to_rgb("7281cc")/255
    color_dict["e"] = hex_to_rgb("75f244")/255
    color_dict["f"] = hex_to_rgb("bfff80")/255
    color_dict["g"] = hex_to_rgb("71b49d")/255
    color_dict["h"] = hex_to_rgb("ffdfcc")/255
    color_dict["i"] = hex_to_rgb("ffffff")/255
    color_dict["j"] = hex_to_rgb("d9f0fa")/255
    color_dict["k"] = hex_to_rgb("e67b57")/255
    color_dict["l"] = hex_to_rgb("ffa666")/255
    color_dict["m"] = hex_to_rgb("ff0084")/255
    color_dict["n"] = hex_to_rgb("ff0090")/255
    color_dict["o"] = hex_to_rgb("363636")/255
    color_dict["p"] = hex_to_rgb("202fd4")/255
    color_dict["q"] = hex_to_rgb("6e6e6e")/255
    color_dict["r"] = hex_to_rgb("ff861c")/255
    color_dict["s"] = hex_to_rgb("ffeb54")/255
    color_dict["t"] = hex_to_rgb("ffed63")/255
    color_dict["u"] = hex_to_rgb("945934")/255
    color_dict["v"] = hex_to_rgb("6e4226")/255
    color_dict["w"] = hex_to_rgb("693f26")/255
    color_dict["x"] = hex_to_rgb("9c9c9c")/255
    color_dict["y"] = hex_to_rgb("e0b392")/255
    color_dict["z"] = hex_to_rgb("8c4818")/255
    color_dict["å"] = hex_to_rgb("9e0000")/255
    color_dict["ä"] = hex_to_rgb("ff7878")/255
    color_dict["ö"] = hex_to_rgb("5e5e5e")/255
    return color_dict


def mixColors(dominant_color, recessive_color, ratio):
        return dominant_color - (dominant_color - recessive_color)/ratio


def getWordColor(input_str, color_dict):
    max_chars = 4
    ratio = 2
    current_color = color_dict[input_str[0].lower()]
    for i in range(1,len(input_str)):
        next_color = color_dict[input_str[i].lower()]
        current_color = mixColors(current_color, next_color, ratio^(i-1))
        if i == max_chars - 1:
            break
    return current_color


class BoxLayoutApp(BoxLayout): #class for layout
    
    color_dict = loadColors()
    start_str = "a"
    red_color_start, green_color_start, blue_color_start = getWordColor(start_str.lower(), color_dict)
    
    red_color_input = red_color_start
    green_color_input = green_color_start
    blue_color_input = blue_color_start

    text_input_str = StringProperty(start_str)
    
    def on_text_validate(self, widget):
            self.red_color_output, self.green_color_output, self.blue_color_output = getWordColor(widget.text.lower(), self.color_dict)
            self.text_input_str = widget.text


class MainWidget(Widget): #class for widget
    pass


class SynestesiaViewer(App):
    pass


"""synestesiaViewer = SynestesiaViewer()
synestesiaViewer.run()
"""







# TEST BENCH
color_dict = loadColors()
test_array = np.array([1,1,1])
plt.plot(test_array)
plt.show()