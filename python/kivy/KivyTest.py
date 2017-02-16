#kivy.require("1.9.1")

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('SimpleKivy.kv')

class Widgets(Widget):
	pass
		

class SimpleKivy(App):
	def build(self):
		return Widgets()


if __name__ == "__main__":
	SimpleKivy().run()