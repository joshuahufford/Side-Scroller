import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image

class Picture(Image):
	pass

class ScrollerGame(Widget):
	def __init__(self):	
		self.add_widget(Picture(source='assets/white_cloud.png'))

class ScrollerApp(App):
	def build(self):
		return ScrollerGame()

if __name__ == '__main__':
    ScrollerApp().run()