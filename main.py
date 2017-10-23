import random
import kivy
from kivy.clock import Clock
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty)
from kivy.vector import Vector


class ScrollerGame(Widget):
	player = ObjectProperty(None)
	obstical1 = ObjectProperty(None)

	def update(self, dt):
		if self.player.y < self.y:  # If ball touches the bottom of screen
			self.player.velocity_y = 0
		else:
			self.player.velocity_y = -1
		self.player.move(dt)
		self.obstical1.scroll(self.player.velocity_x)
		print(self.player.pos)

	def on_touch_down(self, touch):
		if touch.x >= self.player.center_x:
			self.player.velocity_x = 2

	def on_touch_up(self, touch):
		if touch.x >= self.player.center_x:
			self.player.velocity_x = 0

class Player(Widget):
	MAX_VELOCITY_X = 10
	velocity_x = NumericProperty(0)
	velocity_y = NumericProperty(0)
	velocity = ReferenceListProperty(velocity_x, velocity_y)

	def move(self, dt):
		if self.velocity_x > 0:
			self.velocity_x += 2 * dt
		if self.velocity_x > self.MAX_VELOCITY_X:
			self.velocity_x = self.MAX_VELOCITY_X
		self.pos = Vector(0, self.velocity_y) + self.pos


class Obstical(Widget):
	LEFT_OFFSET = 10
	
	def scroll(self, scroll_dist):
		if self.pos[0] > 0 - self.LEFT_OFFSET:
			self.pos = Vector(-1 * scroll_dist, 0) + self.pos
		else:
			self.pos = Vector(
				self.parent.width + random.randint(0, self.parent.width), 15)

class ScrollerApp(App):
	def build(self):
		game = ScrollerGame()
		Clock.schedule_interval(game.update, 1.0/30.0)
		return game

if __name__ == '__main__':
	ScrollerApp().run()