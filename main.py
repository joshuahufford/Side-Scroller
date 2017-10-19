import kivy
from kivy.clock import Clock
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty)
from kivy.uix.floatlayout import FloatLayout


class ScrollerGame(Widget):
	player = ObjectProperty(None)

	def update(self, dt):
		self.player.move(dt)

	def on_touch_down(self, touch):
		if touch.x >= self.player.center_x:
			self.player.velocity_x = 2
			print("2")

class Player(Widget):
	def move(self, dt):
		print("moved")


class MainApp(App):
	def build(self):
		game = ScrollerGame()
		Clock.schedule_interval(game.update(), 1.0/60.0)
		return game

if __name__ == '__main__':
	MainApp().run()